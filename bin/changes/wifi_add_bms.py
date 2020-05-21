#!/usr/bin/env python
import sys
sys.path.append(r'/home/dan/python35/trigger35')

from trigger.cmds import ReactorlessCommando
from trigger.tacacsrc import get_device_password
from twisted.internet import reactor, defer
from twisted.python import log


def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result

def printResults(cmd):
    for c_id, c_info in cmd.results.items():
        for key in c_info:
            print("DEV: {}   CMD: {}\n{}".format(c_id, key.decode('utf-8'),
                                                 c_info[key].decode('utf-8')))


##
class Int_Gig1(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/1',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]

   
class Int_Gig3(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/3',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]


class Int_Gig4(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/4',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]


class Int_Gig5(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/5',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]


class Int_Gig6(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/6',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]


class Int_Gig7(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/7',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]


class Int_Gig10(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/10',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]


class Int_Gig12(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/12',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]



class Int_Gig13(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/13',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]

    
class Int_Gig18(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/18',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]


class Int_Gig19(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/19',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]


class Int_Gig22(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/22',
        b'switchport trunk allowed vlan add 208',
        b'exit',
        b'copy running-config startup-config',
    ]


if __name__ == '__main__':
        
    l_int_1 = ['c-cns-l4-002', 'c-cns-l5-002', 'c-cns-l1-003', 'c-cns-l3-002', 'c-cns-l6-002', ]
    l_int_3 = ['c-cns-l7-002', ]
    l_int_4 = ['c-cns-l2-001', 'c-cns-l4-001', 'c-cns-l3-001', 'c-cns-l7-002', ]
    l_int_5 = ['c-cns-l8-004', ]
    l_int_6 = ['c-cns-l8-004', 'c-cns-g-002', 'c-cns-l1-001', ]
    l_int_7 = ['c-cns-l8-004', ]
    l_int_10 = ['c-cns-g-002', 'c-cns-l7-001', ]
    l_int_12 = ['c-cns-l7-001', 'c-cns-b1-002', ]
    l_int_13 = ['c-cns-b2-002', 'c-cns-b1-001', ]
    l_int_18 = ['c-cns-g-004', 'c-cns-l8-001', 'c-cns-g-001', ]
    l_int_19 = ['c-cns-l8-001', ]
    l_int_22 = ['c-cns-m-001', ]

    c1 = Int_Gig1(l_int_1)
    c2 = Int_Gig3(l_int_3)
    c3 = Int_Gig4(l_int_4)
    c4 = Int_Gig5(l_int_5)
    c5 = Int_Gig6(l_int_6)
    c6 = Int_Gig7(l_int_7)
    c7 = Int_Gig10(l_int_10)
    c8 = Int_Gig12(l_int_12)
    c9 = Int_Gig13(l_int_13)
    c10 = Int_Gig18(l_int_18)
    c11 = Int_Gig19(l_int_19)
    c12 = Int_Gig22(l_int_22)
    
    instances = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, ]

    deferreds = []
    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)

    d.addBoth(stop_reactor)
    reactor.run()
    
    for i in instances:
        printResults(i)
