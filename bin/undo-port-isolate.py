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
#log.startLogging(sys.stdout)


class showRun(Commando):
    """Execute 'show clock' on a list of Cisco devices."""

    def to_huawei(self, dev, commands=None, extra=None):
        vendors = ['huawei']
        self.creds = get_device_password('icntest')
        #print(self.creds)
        commands = ['config',
                    'undo isolate port 0/1/1',
                    'undo isolate port 0/1/2',
                    'undo isolate port 0/1/3',
                    'undo isolate port 0/1/4',
                    'undo isolate port 0/1/5',
                    'undo isolate port 0/1/6',
                    'undo isolate port 0/1/7',
                    'undo isolate port 0/1/8',
                    'undo isolate port 0/1/9',
                    'undo isolate port 0/1/10',
                    'undo isolate port 0/1/11',
                    'undo isolate port 0/1/12',
                    'undo isolate port 0/1/13',
                    'undo isolate port 0/1/14',
                    'undo isolate port 0/1/15',
                    'undo isolate port 0/1/16',
                    'undo isolate port 0/1/17',
                    'undo isolate port 0/1/18',
                    'undo isolate port 0/1/19',
                    'undo isolate port 0/1/20',
                    'undo isolate port 0/1/21',
                    'undo isolate port 0/1/22',
                    'undo isolate port 0/1/23',
                    'undo isolate port 0/1/24',
                    ]
        return commands

    
if __name__ == '__main__':
    device_list = [
        'AVDB-L1-WCHAIR-3',
        'AVDB-L1-BULKSTORE-2-4',
        'AVDB-L1-HOIST_9',
        'AVDB-GF-HOIST_1-2',
        'AVDB-L1-BULK_STORE-2-3',
        'AVDB-GF-HOIST-3-1',
        'AVDB-GF-HOIST_2',
        'AVDB-GF-ST6-REC1-1',
        'AVDB-L1-BULK-STORE-2-1',
        'AVDB-GF-HOIST_1-4',
        'AVDB-GF-STORE-7-1-1',
        'AVDB-L1-BULK-STORE-2-2',
        'AVDB-GF-BULK-STORE-1-1',
        'AVDB-GF-HOIST_3-2',
        'AVDB-GF-BULKSTORE-1-2',
        'AVDB-L1-HOIST_7',
        'AVDB-OLT-L1-HOIST-8',
        'AVDB-OLT-GF-HOIST-5',
        'AVDB-L1-HOIST_7',
        'AVDB-GF-ST6-REC1-2',
        'AVDB-L1-HOIST-8',
        'AVDB-GF-STORE-7-1-2',
        'AVDB-GF-HOIST-1-1',
        'AVDB-APT-COMMS-Room',
        'AVDB-APT-CLEANERS-STORE',
    ]
    
    shorun = showRun(devices=device_list,)
    shorun.run()

    printResults(shorun)
