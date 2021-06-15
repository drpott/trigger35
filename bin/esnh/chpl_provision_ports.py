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
            "vlan 100",
            "name OIP",
            "vlan 2222",
            "name BBWIFI",
            "vlan 101",
            "name VoIP",
            "vlan 102",
            "name BLGMGMTLAN",
            "vlan 103",
            "name SecurityLAN",
            "vlan 104",
            "name ReceptionLAN",
            "vlan 105",
            "name AccessControl",
            "vlan 106",
            "name CCTV",
            "vlan 107",
            "name INTERCOM",
            "vlan 108",
            "name ELEC",
            "vlan 109",
            "name BMS",
            "vlan 110",
            "name EMS",
            "vlan 111",
            "name HYDRLCS",
            "vlan 112",
            "name VerticalTransport",
            "vlan 113",
            "name Fire",
            "vlan 114",
            "name DigitalSignage",
            "vlan 115",
            "name PeopleCounting",
            "vlan 116",
            "name SmartLockers",
            "vlan 117",
            "name CARPARK",
            "vlan 118",
            "name WasteMetering",
            "vlan 119",
            "name VisitorManagement",
            "vlan 120",
            "name Landscape",
            "vlan 121",
            "name Lighting",
            "vlan 122",
            "name EVCharging",
            "vlan 123",
            "name ELECKEYCAB",
            "vlan 124",
            "name BikeCounter",
            "vlan 125",
            "name EMRGLIGHT",
        ]
        return cmds


class configSave(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [ "copy run start", ]
        return cmds

            
def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result


if __name__ == '__main__':

    dev_list = [
        "chpl-fwl-01",
        "chpl-core-01",
        "chpl-tor-01",
        "chpl-tor-02",
        "CHPL-B3-SW1",
        "CHPL-B3-SW2",
        "CHPL-B3-SW3",
        "CHPL-B3-SW4",
        "CHPL-B3-SW5",
        ]

    c = shVlans(dev_list)
    cfg = configVlans(dev_list)
    
    c1 = asw1(['CHPL-B3-SW1'])
    c2 = asw2(['CHPL-B3-SW2'])
    c3 = asw3(['CHPL-B3-SW3'])
    c4 = asw4(['CHPL-B3-SW4'])
    c5 = asw5(['CHPL-B3-SW5'])
    c6 = chpl_fwl_01(['chpl-fwl-01'])
    
    instances = [c]
    
    # Once every task has returned a result, stop the reactor
    deferreds = []

    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)

    d.addBoth(stop_reactor)
    reactor.run()

    for i in instances:
        printResults(i)
