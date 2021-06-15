#!/usr/bin/env python

import sys
import os

PATH = os.getenv('TRIGGER_PATH')
sys.path.append(PATH)

from trigger.cmds import Commando
from trigger.tacacsrc import get_device_password
from twisted.internet import reactor, defer
from twisted.python import log
from tools.pprint import printResults
from bin.ccare.switches import ccare_switches

#log.startLogging(sys.stdout)


class createVlan(Commando):
    """Execute 'show clock' on a list of Cisco devices."""

    def to_huawei(self, dev, commands=None, extra=None):
        vendors = ['huawei']
        self.creds = get_device_password('icntest')
        #print(self.creds)
        commands = ['config',
                    'vlan 250 smart',
                    'port vlan 250 0/0 1',
                    ]

        return commands


def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


if __name__ == '__main__':
    device_list = ['avdb-l1-hoist-8', #1-8
                   'avdb-apt-cleaners-store', #5,7
                   'avdb-gf-hoist-1-1', #1-13
                   'avdb-apt-comms-room', #1
                   'avdb-olt-gf-hoist-5', #1-10
                   'avdb-gf-store-7-1-1', #1,8,11
                   'avdb-gf-bulk-store-1-1', #7, 18-21
                   'avdb-l1-bulk-store-2-2', #1, 11, 24
                   'avdb-gf-hoist_2', #2-10
                   'avdb-gf-hoist_1-4', #1, 3-8
                   'avdb-gf-st6-rec1-1', #8,16
                   'avdb-l1-bulk-store-2-1', #7,24
                   'avdb-gf-hoist-3-1', #1-9,13
                   'avdb-l1-bulk_store-2-3',#1,6
                   'avdb-l1-hoist_9', #1-8
                   'avdb-l1-wchair-3',#1-3, 5-7
                   ]
    
    #c = createVlan(devices=device_list,)
    #c.run()

    instances = []
    crds = get_device_password('icntest')

    for i in device_list:
        c = getattr(ccare_switches, i.replace('-', '_'))
        sw = c([i], creds=crds)
        instances.append(sw)

    # Once every task has returned a result, stop the reactor
    deferreds = []

    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)

    d.addBoth(stop_reactor)
    reactor.run()

    for i in instances:
        printResults(i)
