#!/usr/bin/env python

from trigger.netdevices import NetDevices
from trigger import tacacsrc
nd = NetDevices()
print(len(nd))
dev = nd.find('fortinet')
print(dev)
print("TACACSSHIT")
tcrc = tacacsrc.Tacacsrc()
