#!/usr/bin/env python

import sys
import os

PATH = os.getenv('TRIGGER_PATH')
sys.path.append(PATH)

from trigger.cmds import ReactorlessCommando
from trigger.tacacsrc import get_device_password
from twisted.internet import reactor, defer
from twisted.python import log
from tools.pprint import printResults
from bin.esnh.switches import device_list
#log.startLogging(sys.stdout)

class findMacAddress(ReactorlessCommando):
    """Execute on a list of devices."""

    def to_adtran(self, dev, commands=None, extra=None):
        cmds = ['show mac address-table | include '+self.commands]
        if dev.deviceType == 'OLT':
            self.creds = get_device_password('olt')
        else:
            self.creds = get_device_password('icnesnh')

        return cmds
    
    def to_juniper(self, dev, commands=None, extra=None):
        cmds = ['show ethernet-switching table | match '+self.commands]
        self.creds = creds=get_device_password('tor')
        return cmds

    def to_fortinet(self, dev, commands=None, extra=None):
        cmds = ['get system arp | grep '+self.commands]
        self.creds=get_device_password('esnh-icn-fwl')
        return cmds

    
            
def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


if __name__ == '__main__':

    #device_list = ['esnh-icn-fwl']
    c1 = findMacAddress(device_list, commands=sys.argv[1] )
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
