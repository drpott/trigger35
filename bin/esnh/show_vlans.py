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


class shVlans(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = ['show vlan brief']
        
        return cmds

    def to_juniper(self, dev, commands=None, extra=None):
        cmds = ['show vlans brief']
        self.creds = creds=get_device_password('esnh-swt-00')
        
        return cmds

    def to_fortinet(self, dev, commands=None, extra=None):
        cmds = [
            #'config vdom',
            #'edit ESNH-ICN',
            'get system interface'
        ]
        
        self.creds=get_device_password('esnh-icn-fwl')
        return cmds

    
def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


if __name__ == '__main__':

    dev_list = [
        'esnh-icn-fwl',
        'ESNH-BAS-B1-1A-02',
        'ESNH-BAS-G-1A-01',
        'ESNH-BAS-G-1A-02',
        'ESNH-BAS-B2-1A-02',
        'ESNH-BAS-B2-1A-01',
        'ESNH-BAS-B3-1A-02',
        'ESNH-BAS-B1-1B-01',
        'ESNH-BAS-B1-1B-02',
        'ESNH-BAS-B2-1B-01',
        'ESNH-BAS-G-1B-02',
        'ESNH-BAS-G-1B-01',
        'ESNH-BAS-MCR-B1-01',
        'ESNH-BAS-BLG1B-L8-01',
        'ESNH-BAS-BLG1A-L7-01',
        'ESNH-BAS-BLG1B-L7-01',
        'ESNH-BAS-BLG1B-L5-01',
        'ESNH-BAS-BLG1B-L2-01',
        'ESNH-BAS-BLG1-L2-01',
        'ESNH-BAS-BLG1-L3-01',
        'ESNH-BAS-BLG1-L7-01',
    ]


    c1 = shVlans(dev_list,)
    
    instances = [c1,]
    # Once every task has returned a result, stop the reactor
    deferreds = []

    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)

    d.addBoth(stop_reactor)
    reactor.run()

    for i in instances:
        printResults(i)
