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
from bin.esnh.switches.esnh_switches import *
from bin.esnh.switches.chapel_switches import *


class shVlans(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = ['show vlan brief']
        
        return cmds


class configVlans(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            "enable",
            "conf t",
            "vlan 201",
            "name CCTV",
            "vlan 202",
            "name INTRCM",
            "vlan 203",
            "name ACCSCTR",
            "vlan 204",
            "name EVCHARG",
            "vlan 205",
            "name BMS",
            "vlan 206",
            "name OIP",
            "vlan 207",
            "name HYDRLCS",
            "vlan 208",
            "name AIRCON",
            "vlan 209",
            "name CARPARK",
            "vlan 210",
            "name VOIP",
            "vlan 211",
            "name LIFTS",
            "vlan 212",
            "name WASTE",
            "vlan 213",
            "name SOLAR",
            "vlan 214",
            "name LITING",
            "vlan 215",
            "name DIGSNG",
            "vlan 216",
            "name AUDIOSPKR",
            "vlan 217",
            "name PPLCTNG",
            "vlan 218",
            "name IRRIGATION",
            "vlan 219",
            "name NOTICEBRD",
            "vlan 220",
            "name CMO",
            "vlan 2222",
            "name BBWIFI",
            "vlan 2223",
            "name PUBWIFI",
        ]
        return cmds


class configSave(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [ "copy run start", ]
        return cmds


class findMacAddress(ReactorlessCommando):
    """Execute on a list of devices."""

    def to_adtran(self, dev, commands=None, extra=None):
        cmds = ['show mac address-table | include '+self.commands]
        if dev.deviceType == 'OLT':
            self.creds = get_device_password('olt')

        return cmds
    
    def to_juniper(self, dev, commands=None, extra=None):
        cmds = ['show ethernet-switching table | match '+self.commands]
        self.creds = creds=get_device_password('tor')
        return cmds

    def to_fortinet(self, dev, commands=None, extra=None):
        cmds = ['get system arp | grep '+self.commands]
        self.creds=get_device_password('esnh-icn-fwl')
        return cmds

    
            
def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


if __name__ == '__main__':

    dev_list = [
        'ESNH-BAS-BLG1B-L7-01',
        'ESNH-BAS-BLG1B-L5-01',
        'ESNH-BAS-BLG1B-L2-01',
        'ESNH-BAS-G-01-02',
        'ESNH-BAS-G-01-01',
        'ESNH-BAS-B1-01',
        'ESNH-BAS-B1-01-2',
        'ESNH-BAS-B2-01',
        'ESNH-BAS-BLG1-L7-01',
        'ESNH-BAS-BLG1-L3-01',
        'ESNH-BAS-BLG1-L2-01',
        'ESNH-BAS-G-02-01',
        'ESNH-BAS-G-02-02',
        'ESNH-BAS-B1-02',
        'ESNH-BAS-B2-02',
        'ESNH-BAS-B2-01',
        'ESNH-BAS-B3-02',
        'ESNH-BAS-MCR-B1-01',]

    findmac = findMacAddress(dev_list, "00:24:45")
    c1 = shVlans(['ESNH-BAS-B1-02', 'ESNH-BAS-B1-01-2', 'ESNH-BAS-G-02-02'],)
    #c1 = configVlans(dev_list,)
    #c1 = shVlans(dev_list)

    c2 = ESNH_BAS_B3_1A_02(['ESNH-BAS-B3-02'])
    c3 = ESNH_BAS_B1_1B_01(['ESNH-BAS-B1-01'])
    c4 = ESNH_BAS_G_1B_02(['ESNH-BAS-G-01-02'])
    c5 = ESNH_BAS_G_1B_01(['ESNH-BAS-G-01-01'])
    c6 = ESNH_BAS_BLG1B_L7_01(['ESNH-BAS-BLG1B-L7-01'])
    c7 = ESNH_BAS_MCR_B1_01(['ESNH-BAS-MCR-B1-01'])
    c8 = ESNH_SWT_01(['ESNH-SWT-01'])
    c9 = ESNH_SWT_02(['ESNH-SWT-02'])
    c10 = ESNH_BAS_BLG1B_L5_01(['ESNH-BAS-BLG1B-L5-01'])
    c11 = ESNH_BAS_BLG1B_L2_01(['ESNH-BAS-BLG1B-L2-01'])
    c12 = ESNH_BAS_BLG1_L2_01(['ESNH-BAS-BLG1-L2-01'])
    c13 = ESNH_BAS_BLG1_L3_01(['ESNH-BAS-BLG1-L3-01'])
    c14 = ESNH_BAS_BLG1_L7_01(['ESNH-BAS-BLG1-L7-01'])

    c15 = esnh_bas_g_02_02(['esnh-bas-g-02-02'])

    c16 = esnh_bas_g_02_01(['esnh-bas-g-02-01'])

    c17 = esnh_bas_b1_01_2(['esnh-bas-b1-01-2'])
    c18 = esnh_bas_b1_02(['esnh-bas-b1-02'])

    c21 = esnh_bas_b2_01(['ESNH-BAS-B2-01'])
    c20 = ESNH_BAS_B2_02_01(['esnh-bas-b2-02'])
    c22 = esnh_bas_b3_01(['ESNH-BAS-B3-01'])
    cmo = esnh_bas_b1_cmo(['ESNH-BAS-B1-CMO'])
    cvlan = configVlans(['ESNH-BAS-B1-CMO'])
    cshvlan = shVlans(['ESNH-BAS-B1-CMO'])
    
    c = configSave(dev_list)

    instances = [cmo,]
    # Once every task has returned a result, stop the reactor
    deferreds = []

    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)

    d.addBoth(stop_reactor)
    reactor.run()

    for i in instances:
        printResults(i)
