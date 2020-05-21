#!/usr/bin/env python
import sys
sys.path.append(r'/home/dan/python35/trigger35')

from trigger.cmds import ReactorlessCommando
from trigger.tacacsrc import get_device_password
from twisted.internet import reactor, defer
from twisted.python import log




class Fortinet(ReactorlessCommando):
    commands = [
        'config system interface',
        'edit vlan216',
        'set vdom root',
        'set ip 192.168.216.254 255.255.255.0',
        'set allowaccess ping',
        'set alias TLCtrl',
        'set role lan',
        'set interface x1',
        'set vlanid 216',
        'end',
        'config firewall address',
        'edit TLCTRLADDR',
        'set associated-interface vlan216',
        'set subnet 192.168.216.0 255.255.255.0',
        'end',
        'config firewall policy',
        'edit 0',
        'set name v210->v216',
        'set srcintf vlan210',
        'set dstintf vlan216',
        'set srcaddr h-192.168.210.50',
        'set dstaddr TLCTRLADDR',
        'set action accept',
        'set status enable',
        'set schedule always',
        'set service ALL',
        'set logtraffic all',
        'end',]


class Tor2(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    commands = ['configure',
                'set vlans v216 vlan-id 216'
                'set interfaces ge-0/0/23 unit 0 family ethernet-switching vlan members v216',
                'delete interfaces ge-0/0/23 unit 0 family ethernet-switching vlan members v205',
                'set interfaces ge-0/0/23 unit 0 family ethernet-switching vlan members v216',
                'commit']
    
    vendors = ['juniper']

    def to_juniper(self, dev, commands=None, extra=None):
        return self.commands
    

class Tor(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    commands = ['configure',
                'set interfaces xe-0/0/23 unit 0 vlan-id-list 216',
                'commit']

    def to_juniper(self, dev, commands=None, extra=None):
        return self.commands



##
class Int_Gig1(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/1',
        'no shutdown',
        'exit']


class Int_Gig2(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/2',
        b'shutdown',
        b'exit']

    
class Int_Gig3(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/3',
        'no shutdown',
        'exit']


class Int_Gig4(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/4',
        'no shutdown',
        'exit']


class Int_Gig5(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/5',
        'no shutdown',
        'exit']


class Int_Gig6(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/6',
        'no shutdown',
        'exit']


class Int_Gig7(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/7',
        'no shutdown',
        'exit']



class Int_Gig10(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/10',
        'no shutdown',
        'exit']


class Int_Gig12(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/12',
        'no shutdown',
        'exit']


class Int_Gig13(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/13',
        'no shutdown',
        'exit']


class Int_Gig15(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        b'configure terminal',
        b'interface gigabit 1/15-18',
        b'shutdown',
        b'exit']


class Int_Gig16(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/13',
        'no shutdown',
        'exit']

    
class Int_Gig18(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/18',
        'no shutdown',
        'exit']


class Int_Gig19(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/19',
        'no shutdown',
        'exit']


class Int_Gig22(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    vendors = ['cisco']
    commands = [
        'configure terminal',
        'interface gigabit 1/22',
        'no shutdown',
        'exit']


def printResults(cmd):
    for c_id, c_info in cmd.results.items():
        for key in c_info:
            print("DEV: {}   CMD: {}\n{}".format(c_id, key, c_info[key].decode('utf-8')))


def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


if __name__ == '__main__':
        
    #fw = ['fortinet']
    #tor = ['tor']
    #tor2 = ['tor2']

    #l_int_1 = ['c-cns-l4-002', 'c-cns-l5-002', 'c-cns-l1-003', 'c-cns-l3-002', 'c-cns-l6-002', ]
    l_int_2 = ['c-cns-l8-002']
    #l_int_3 = ['c-cns-l7-003', ]
    #l_int_4 = ['c-cns-l2-001', 'c-cns-l4-001', 'c-cns-l3-001', 'c-cns-l7-003', ]
    #l_int_5 = ['c-cns-l8-004', ]
    #l_int_6 = ['c-cns-l8-004', 'c-cns-g-002', 'c-cns-l1-001', ]
    #l_int_7 = ['c-cns-l8-004', ]
    #l_int_10 = ['c-cns-g-002', 'c-cns-l7-001', ]
    #l_int_12 = ['c-cns-l7-001', 'c-cns-b1-002', ]
    #l_int_13 = ['c-cns-b2-002', 'c-cns-b1-001', ]
    l_int_15_18 = ['c-cns-l8-004']
    #l_int_18 = ['c-cns-g-004', 'c-cns-l8-001', 'c-cns-g-001', ]
    #l_int_19 = ['c-cns-l8-001', ]
    #l_int_22 = ['c-cns-m-001', ]

    #c1 = Int_Gig1(l_int_1)
    c2 = Int_Gig2(l_int_2)
    #c3 = Int_Gig4(l_int_4)
    #c4 = Int_Gig5(l_int_5)
    #c5 = Int_Gig6(l_int_6)
    #c6 = Int_Gig7(l_int_7)
    #c7 = Int_Gig10(l_int_10)
    #c8 = Int_Gig12(l_int_12)
    #c9 = Int_Gig13(l_int_13)
    #c10 = Int_Gig18(l_int_18)
    #c11 = Int_Gig19(l_int_19)
    #c12 = Int_Gig22(l_int_22)
    c15_18 = Int_Gig15(l_int_15_18)
    
    #instances = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, ]
    instances = [c2, c15_18,]

    deferreds = []
    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)

    d.addBoth(stop_reactor)
    reactor.run()
    
    for i in instances:
        printResults(i)
