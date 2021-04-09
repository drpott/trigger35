#!/usr/bin/env python

import sys, os
#sys.path.append(r'/home/dpottumati/py-envs/trigger35/')
#below works now
sys.path.append(os.getenv('TRIGGER_PATH'))

from trigger.cmds import ReactorlessCommando
from trigger.tacacsrc import get_device_password
from twisted.internet import reactor, defer
from twisted.python import log
from tools.pprint import printResults

#MAC='00:24:45' # ADTRAN switches
#MAC='64:9f:f7' # KONE
#MAC='00:90:e8' # MOXA switches
#MAC='00:17:88:0b:6a:c6' # Philips lighting
#MAC='18:e8:29'  # Blinds AP-ACj Pro
#MAC='74:83:c2'  # Blinds AP-ACj Pro
#MAC='b8:27:eb:5e:77:fb'  # Blinds controller
#MAC='f4:0b:7f' #lighting controller vlan216
#MAC='54:ec:2f' # ruckus wifi aps
#MAC='1c:5f:2b' #smart lockers
#MAC=00:15:65:ab:19:34 #VOIP commander
#MAC='b6:0e'


class findMacAddress(ReactorlessCommando):
    """Execute on a list of devices."""

    def to_adtran(self, dev, commands=None, extra=None):
        cmds = ['show mac address-table | include '+self.commands]
        if dev.deviceType == 'OLT':
            self.creds = get_device_password('olt')
        return cmds
    
    def to_juniper(self, dev, commands=None, extra=None):
        cmds = ['show ethernet-switching table | match '+self.commands]
        self.creds = creds=get_device_password('tor')
        return cmds

    def to_fortinet(self, dev, commands=None, extra=None):
        cmds = ['get system arp | grep '+self.commands]
        self.creds=get_device_password('fortinet')
        return cmds
    
def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


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
        "fortinet",            "olt",
    ]
    
    c1 = findMacAddress(dev_list, commands=sys.argv[1] )
    instances = [c1]
    # Once every task has returned a result, stop the reactor
    deferreds = []
    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)

    d.addBoth(stop_reactor)
    reactor.run()

    for i in instances:
        printResults(i)
