#!/usr/bin/env python
import sys
sys.path.append(r'/home/dan/python35/trigger35')

from trigger.cmds import Commando
import sys


class showRun(Commando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [ b'conf t',
                 b'vlan 208',
                 b'name BMS',
                 b'exit',
                 b'interface 10GigabitEthernet 1/1',
                 b'switchport trunk allowed vlan add 208',
                 b'end',
                 b'copy running start']
    
    
if __name__ == '__main__':

    device_list = [
        "C-CNS-M-001",
        "C-CNS-B1-001",
        "C-CNS-B1-002",
        "C-CNS-G-001",
        "C-CNS-L3-002",
        "C-CNS-L7-002",
    ]
    
    shorun = showRun(devices=device_list)
    shorun.run() # Commando exposes this to start the event loop

    for c_id, c_info in shorun.results.items():
        for key in c_info:
            print("SWITCH: {} command: {}\n {}".format(c_id, key, c_info[key]))
