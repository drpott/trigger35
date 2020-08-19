#!/usr/bin/env python

import sys
sys.path.append(r'/home/dan/python35/trigger35')

"""
commando_reactorless.py - Running multiple Commando's in the same script
"""
import sys
sys.path.append(r'/home/dan/python35/trigger35')

from trigger.cmds import ReactorlessCommando
from trigger.tacacsrc import get_device_password
from trigger.netdevices import NetDevices
from twisted.internet import reactor, defer
from twisted.python import log

class diagDebug(ReactorlessCommando):
    """
    if fortigate is dropping packets debug packet flow can show the reason and how
    cpu is handling each packet
    """
    def to_fortinet(self, dev, commands=None, extra=None):
        self.creds=get_device_password('fortinet')
        commands = [b'diagnose debug enable', #disable
                    b'diagnose debug flow filter addr 220.233.199.237',
                    #b'diagnose debug flow filter port 4443',
                    b'diagnose debug flow trace start 100',
                    b'diagnose debug flow trace stop',

        ]
        return commands


def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


def printResults(cmd):
    for c_id, c_info in cmd.results.items():
        for key in c_info:
            print("DEV: {}   CMD: {}\n{}".format(c_id,
                                                 key.decode('utf-8'),
                                                 c_info[key].decode('utf-8')))


if __name__ == '__main__':

    #c1 = showUserSessionList(['fortinet'], commands=sys.argv[1].encode('utf-8') )
    c1 = diagDebug(['fortinet'], )
    instances = [c1]
    deferreds = []
    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)
    d.addBoth(stop_reactor)
    reactor.run()

    for i in instances:
        printResults(i)
