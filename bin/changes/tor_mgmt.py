#!/usr/bin/env python


import sys
sys.path.append(r'/home/dan/python35/trigger35')


from trigger.cmds import ReactorlessCommando
from trigger.tacacsrc import get_device_password
from twisted.internet import reactor, defer
from twisted.python import log


def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


class Tor1(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    commands = [b'configure',
                b'wildcard delete interfaces ge-0/0/1 unit 0 family ethernet-switching vlan members',
                b'wildcard delete interfaces ge-0/0/11 unit 0 family ethernet-switching vlan members',
                #'wildcard delete interfaces ge-0/0/6 unit 0 family ethernet-switching vlan members',
                b'set interfaces ge-0/0/1 unit 0 family ethernet-switching vlan members v201',
                b'set interfaces ge-0/0/11 unit 0 family ethernet-switching vlan members v202',
                #'set interfaces ge-0/0/6 unit 0 family ethernet-switching vlan members MGMT',
                b'commit']
    
    vendors = ['juniper']

    def to_juniper(self, dev, commands=None, extra=None):
        return self.commands


class Tor2(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    commands = [b'configure',
                b'wildcard delete interfaces ge-0/0/1 unit 0 family ethernet-switching vlan members',
                b'wildcard delete interfaces ge-0/0/3 unit 0 family ethernet-switching vlan members',
                b'wildcard delete interfaces ge-0/0/8 unit 0 family ethernet-switching vlan members',
                b'set interfaces ge-0/0/1 unit 0 family ethernet-switching vlan members v202',
                b'set interfaces ge-0/0/3 unit 0 family ethernet-switching vlan members v202',
                b'set interfaces ge-0/0/8 unit 0 family ethernet-switching vlan members v201',
                b'commit']
    
    vendors = ['juniper']

    def to_juniper(self, dev, commands=None, extra=None):
        return self.commands


def printResults(cmd):
    for c_id, c_info in cmd.results.items():
        for key in c_info:
            print("DEV: {}   CMD: {}\n{}".format(c_id, key,
                                                 c_info[key].decode('utf-8')))


    
if __name__ == '__main__':
        
    c_tor1 = Tor1(['tor1'], creds=get_device_password('tor'), )
    c_tor2 = Tor2(['tor2'], creds=get_device_password('tor'), )

    instances = [c_tor1, c_tor2]

    deferreds = []
    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)

    d.addBoth(stop_reactor)
    reactor.run()
    
    for i in instances:
        printResults(i)
