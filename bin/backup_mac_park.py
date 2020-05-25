#!/usr/bin/env python

import sys
sys.path.append(r'/home/dan/python35/trigger35')

"""
commando_reactorless.py - Running multiple Commando's in the same script
"""

from trigger.cmds import ReactorlessCommando
from trigger.tacacsrc import get_device_password
from trigger.netdevices import NetDevices
from twisted.internet import reactor, defer
from twisted.python import log


def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


class backMeUp(ReactorlessCommando):
    """Execute on a list of devices."""

    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [b'show running-config']
        self.timeout = 300
        if dev.deviceType == 'OLT':
            self.creds = get_device_password('olt')
            
        return cmds
    
    def to_juniper(self, dev, commands=None, extra=None):
        cmds = [b'show configuration | display set']
        self.timeout = 300
        self.creds = creds=get_device_password('tor')

        return cmds

    def to_fortinet(self, dev, commands=None, extra=None):
        cmds = [b'show']
        self.timeout = 300
        self.creds=get_device_password('fortinet')

        return cmds


if __name__ == '__main__':
    dev_list = [
        "C-CNS-M-001",         "C-CNS-M-002",         "C-CNS-M-003",
        "C-CNS-B1-001",        "C-CNS-B1-002",        "C-CNS-B2-001",
        "C-CNS-B2-002",        "C-CNS-G-001",         "C-CNS-G-002",
        "C-CNS-G-003",         "C-CNS-G-004",         "C-CNS-L1-001",
        "C-CNS-L1-003",        "C-CNS-L2-001",        "C-CNS-L2-002",
        "C-CNS-L3-001",        "C-CNS-L3-002",        "C-CNS-L4-001",
        "C-CNS-L4-002",        "C-CNS-L5-001",        "C-CNS-L5-002",
        "C-CNS-L6-001",        "C-CNS-L6-002",        "C-CNS-L7-001",
        "C-CNS-L7-002",        "C-CNS-L8-001",        "C-CNS-L8-002",
        "C-CNS-L8-003",        "C-CNS-L8-004",        "C-CNS-L8-005",
        "tor",                 "tor1",                "tor2",
        "olt",
        "fortinet",
    ]
    
    c1 = backMeUp(dev_list, max_conns=40)
    instances = [c1]

    # Once every task has returned a result, stop the reactor
    deferreds = []
    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)

    d.addBoth(stop_reactor)
    reactor.run()

    for c_id, c_info in c1.results.items():
        for key in c_info:
            print("DEV: {}   CMD: {}\n{}".format(c_id,
                                                 key.decode('utf-8'),
                                                 c_info[key].decode('utf-8')))
