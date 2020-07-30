#!/usr/bin/env python

import sys
sys.path.append(r'/home/dan/python35/trigger35')
from trigger.cmds import Commando

from twisted.python import log
#log.startLogging(sys.stdout)


class showRun(Commando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['adtran']
    commands = [b'show lldp neighb']
        
    
    
if __name__ == '__main__':
    device_list = [ 'c-cns-b2-002', 'c-cns-b1-001']
    """
    "C-CNS-M-001",
        "C-CNS-M-002",
        "C-CNS-M-003",
        "C-CNS-B1-001",
        "C-CNS-B1-002",
        "C-CNS-B2-001",
        "C-CNS-B2-002",
        "C-CNS-G-001",
        "C-CNS-G-002",
        "C-CNS-G-003",
        "C-CNS-G-004",
        "C-CNS-L1-001",
        "C-CNS-L1-003",
        "C-CNS-L2-001",
        "C-CNS-L2-002",
        "C-CNS-L3-001",
        "C-CNS-L3-002",
        "C-CNS-L4-001",
        "C-CNS-L4-002",
        "C-CNS-L5-001",
        "C-CNS-L5-002",
        "C-CNS-L6-001",
        "C-CNS-L6-002",
        "C-CNS-L7-001",
        "C-CNS-L7-002",
        "C-CNS-L8-001",
        "C-CNS-L8-002",
        "C-CNS-L8-003",
        "C-CNS-L8-004",
        "C-CNS-L8-005",]
    """
    
    shorun = showRun(devices=device_list)
    shorun.run() # Commando exposes this to start the event loop

    print(shorun.errors)
    for c_id, c_info in list(shorun.results.items()):
        for key in c_info:
            print(("SWITCH: {} command: {}\n {}".format(c_id, key.decode('utf-8'),
                                                        c_info[key].decode('utf-8'))))
