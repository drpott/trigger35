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


class configShaper(ReactorlessCommando):
    commands = [
        'shaper "ONT_2_1" 1@1/1/2.gpon',
        'per interface gpon 1/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_2_2" 2@1/1/2.gpon',
        'per interface gpon 2/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_2_3" 3@1/1/2.gpon',
        'per interface gpon 3/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_2_4" 4@1/1/2.gpon',
        'per interface gpon 4/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_2_5" 5@1/1/2.gpon',
        'per interface gpon 5/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_2_6" 6@1/1/2.gpon',
        'per interface gpon 6/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_2_7" 7@1/1/2.gpon',
        'per interface gpon 7/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_1_1" 1@1/1/1.gpon',
        'per interface gpon 1/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_1_2" 2@1/1/1.gpon',
        'per interface gpon 2/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_1_3" 3@1/1/1.gpon',
        'per interface gpon 3/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_1_4" 4@1/1/1.gpon',
        'per interface gpon 4/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_1_5" 5@1/1/1.gpon',
        'per interface gpon 5/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
        'shaper "ONT_1_6" 6@1/1/1.gpon',
        'per interface gpon 6/0/1@1/1/2.gpon channel 1',
        'rate 500000',
        'gpon channel assured-bandwidth 0',
        'gpon channel fixed-bandwidth 0',
        'min-rate 0',
        'no shutdown',
        'exit',
    ]

def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


if __name__ == '__main__':

    dev_list = ['esnh-olt-02',]


    c1 = configShaper(dev_list,)
    
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
