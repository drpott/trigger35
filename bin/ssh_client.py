#!/usr/bin/env python

from twisted.conch.ssh import transport, connection, userauth, channel, common
from twisted.internet import defer, protocol, stdio, reactor
from twisted.python import log

from trigger import tacacsrc, exceptions
from trigger.utils import network, cli
from trigger.twister import Interactor, stop_reactor, TriggerClientFactory, TriggerSSHPtyChannel, TriggerSSHConnection, TriggerSSHTransport
from trigger.netdevices import NetDevices
from trigger.conf import settings
import sys

log.startLogging(sys.stdout, setStdout=False)

#2 this gets called, buildProtocol in factory
class ClientCommandTransport(transport.SSHClientTransport):

    def __init__(self, command=''):
        self.command = command

    def verifyHostKey(self, pubKey, fingerprint):
        # in a real app, you should verify that the fingerprint matches
        # the one you expected to get from this server
        return defer.succeed(True)

    def dataReceived(self, data):
        """
        First, check for the version string (SSH-2.0-*).  After that has been
        received, this method adds data to the buffer, and pulls out any
        packets.
        @type data: L{bytes}
        @param data: The data that was received.
        """
        self.buf = self.buf + data
        if not self.gotVersion:
            if self.buf.find(b'\n', self.buf.find(b'SSH-')) == -1:
                return

            # RFC 4253 section 4.2 ask for strict `\r\n` line ending.
            # Here we are a bit more relaxed and accept implementations ending
            # only in '\n'.
            # https://tools.ietf.org/html/rfc4253#section-4.2
            lines = self.buf.split(b'\n')
            for p in lines:
                if p.startswith(b'SSH-'):
                    self.gotVersion = True
                    # Since the line was split on '\n' and most of the time
                    # it uses '\r\n' we may get an extra '\r'.
                    self.otherVersionString = p.rstrip(b'\r')
                    remoteVersion = p.split(b'-')[1]
                    if remoteVersion not in self.supportedVersions:
                        self._unsupportedVersionReceived(remoteVersion)
                        return
                    i = lines.index(p)
                    self.buf = b'\n'.join(lines[i + 1:])
        packet = self.getPacket()
        while packet:
            messageNum = ord(packet[0:1])
            self.dispatchMessage(messageNum, packet[1:])
            packet = self.getPacket()

    """
    def connectionSecure(self):
        self.requestService(
            PasswordAuth(self.factory.creds.username,
                         self.factory.creds.password,
                         ClientConnection(self.command))) #3 call client connection
    """

    def connectionSecure(self):
        self.requestService(
            PasswordAuth(self.factory.creds.username,
                         self.factory.creds.password,
                         self.factory.connection_class(self.command))) #3 call client connection


class PasswordAuth(userauth.SSHUserAuthClient):

    preferredOrder = [b'password', b'publickey', b'keyboard-interactive']
    
    def __init__(self, user, password, connection):
        userauth.SSHUserAuthClient.__init__(self, user, connection)
        self.password = password
        
    def getPassword(self, prompt=None):
        return defer.succeed(self.password)


#3 connection class TriggerSSHConnection
class ClientConnection(connection.SSHConnection):
    def __init__(self, cmd, *args, **kwargs):
        connection.SSHConnection.__init__(self)
        self.command = cmd
        
    def serviceStarted(self):
        self.openChannel(CommandChannel(self.command, conn=self))


class CommandChannel(channel.SSHChannel):
    name = 'session'
    
    def __init__(self, command, *args, **kwargs):
        channel.SSHChannel.__init__(self, *args, **kwargs)
        self.command = command
        self.factory = self.conn.transport.factory
                
    def channelOpen(self, data):
        #open pty channel here TriggerSSHPtyChannel
        self.conn.sendRequest(
            self, 'exec', common.NS(self.command), wantReply=True).addCallback(self._gotResponse)
        
    def _gotResponse(self, _):
        self.conn.sendEOF(self)
        
    def dataReceived(self, data):
        self.factory.results += data
        
    def closed(self):
        self.factory.deferred.callback(self.factory.results)


class ClientCommandFactory(protocol.ClientFactory):

    def old__init__(self, username, password, command):
        self.username = username
        self.password = password
        self.command = command

    def __init__(self, d, creds, command):
        self.deferred = d
        self.creds = tacacsrc.validate_credentials(creds)
        self.command = command
        self.connection_class = ClientConnection
        self.results = b''
        
    def buildProtocol(self, addr):
        protocol = ClientCommandTransport(self.command)
        protocol.factory = self
        
        return protocol

    
#1 this gets called in pty_connect
class TriggerSSHPtyClientFactory(TriggerClientFactory):
    """
    Factory for an interactive SSH connection.

    'action' is a Protocol that will be connected to the session after login.
    Use it to interact with the user and pass along commands.
    """
    
    def __init__(self, deferred, action, creds=None, display_banner=None, init_commands=None, device=None):
        self.protocol = TriggerSSHTransport #change this to your transport
        #self.protocol = ClientCommandTransport #2 this gets called by buildProtocol
        self.action = action #Interactor object 
        self.action.factory = self #point Interactor factory to this factory TriggerSSHPtyClientFactory
        self.device = device
        self.display_banner = display_banner
        self.channel_class = TriggerSSHPtyChannel
        self.connection_class = TriggerSSHConnection # my connection class, can be removed?
        #self.connection_class = ClientConnection
        self.commands = []
        self.command_interval = 0
        TriggerClientFactory.__init__(self, deferred, creds, init_commands)


def execute_cmd(srv, cmd, usr, pwd):
    d = defer.Deferred()
    from twisted.internet import reactor
    factory = ClientCommandFactory(d, (usr, pwd), cmd)
    reactor.connectTCP(srv, 22, factory)
    return d


def test_trigger():
    from twisted.internet import reactor
    
    nd = NetDevices()
    dev = nd.find('fortinet')
    d = defer.Deferred()
    creds = tacacsrc.get_device_password(dev.nodeName)
    factory = TriggerSSHPtyClientFactory(d, Interactor(), creds,
                                         display_banner=None,
                                         init_commands=None,
                                         device=dev)
    reactor.connectTCP(dev.nodeName, 22, factory)
    d.addCallback(lambda x: stop_reactor())
    cli.setup_tty_for_pty(reactor.run)

    
def test_normal():
    from twisted.internet import reactor

    server = b'1.1.1.1'
    command = b'get system info admin status'
    username = b'user'
    password = b'pass'

    def print_result(result):
        print("The results:")
        print(result.decode('utf-8'))

        
    d = execute_cmd(server, command, username, password)
    d.addCallbacks(print_result, print_result)
    d.addBoth(lambda x: stop_reactor())

    reactor.run()
    
if __name__ == '__main__':

    #test_normal()
    test_trigger()
"""
    server = b'1.1.1.1'
    command = b'get system info admin status'
    username = b'user'
    password = b'pass'
    factory = ClientCommandFactory(username, password, command)
    reactor.connectTCP(server, 22, factory)
    reactor.run()

"""

