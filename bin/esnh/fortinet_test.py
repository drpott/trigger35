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
    def to_fortinet(self, dev, commands=None, extra=None):
        cmds = [
            #'config vdom',
            #'edit ESNH-ICN',
            'get system admin'
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
