#!/usr/bin/env python

import sys
sys.path.append(r'/home/dan/python35/trigger35')
import json
from trigger.cmds import Commando

from twisted.python import log
#log.startLogging(sys.stdout)


class showPortSec(Commando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['adtran']
    commands = [b'show port-security interface GigabitEthernet *']
    
    
if __name__ == '__main__':
    device_list = [
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
    
    shorun = showPortSec(devices=device_list)
    shorun.run() # Commando exposes this to start the event loop

    """
    for c_id, c_info in list(shorun.results.items()):
        for key in c_info:
            print(("SWITCH: {} command: {}\n {}".format(c_id, key.decode('utf-8'),
                                                        c_info[key].decode('utf-8'))))
    """
    
    c = 'show port-security interface GigabitEthernet *'    
    for switch, cmd in shorun.parsed_results.items():
        for i in range(len(cmd[c]['violating'])):
            if cmd[c]['violating'][i] == int and cmd[c]['violating'][i] > 0:
                print('{}: Port: {}    Users: {}  Limit: {} Violating: {}  Violation: {}'.format(switch,
                                                                                             cmd[c]['port'][i],
                                                                                             cmd[c]['current'][i],
                                                                                             cmd[c]['limit'][i],
                                                                                             cmd[c]['violating'][i],
                                                                                             cmd[c]['violation'][i]))

    #print(json.dumps(shorun.parsed_results, indent=4))
