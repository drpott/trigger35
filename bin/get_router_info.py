#!/usr/bin/env python
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
from tools.pprint import printResults

class diagDebug(ReactorlessCommando):
    def to_fortinet(self, dev, commands=None, extra=None):
        self.creds=get_device_password('fortinet')
        commands = ['get router info routing-table database',
                    'diagnose sys sdwan health-check', #check sdwan ip sla probess\
                    'get router info kernel 17'] #show sdwan ip sla routes
        return commands


def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


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
