#!/usr/bin/env python

from trigger.cmds import ReactorlessCommando

class avdb_l1_hoist_8(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/2 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/3 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 73 vlan 250 eth 0/1/4 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 74 vlan 250 eth 0/1/5 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 75 vlan 250 eth 0/1/6 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 76 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 77 vlan 250 eth 0/1/8 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                ] #1_8
        return cmds



class avdb_apt_cleaners_store(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/5 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',] #5,7
        return cmds


class avdb_gf_hoist_1_1(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/2 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/3 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 73 vlan 250 eth 0/1/4 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 74 vlan 250 eth 0/1/5 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 75 vlan 250 eth 0/1/6 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 76 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 77 vlan 250 eth 0/1/8 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 78 vlan 250 eth 0/1/9 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 79 vlan 250 eth 0/1/10 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 80 vlan 250 eth 0/1/11 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 81 vlan 250 eth 0/1/12 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 82 vlan 250 eth 0/1/13 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',]
        return cmds


class avdb_apt_comms_room(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',]
        return cmds


class avdb_olt_gf_hoist_5(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/2 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/3 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 73 vlan 250 eth 0/1/4 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 74 vlan 250 eth 0/1/5 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 75 vlan 250 eth 0/1/6 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 76 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 77 vlan 250 eth 0/1/8 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 78 vlan 250 eth 0/1/9 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 79 vlan 250 eth 0/1/10 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                ]
        return cmds

    
class avdb_gf_store_7_1_1(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/8 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/11 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                ]
        return cmds


class avdb_gf_bulk_store_1_1(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/18 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/19 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 73 vlan 250 eth 0/1/20 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 74 vlan 250 eth 0/1/21 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',]
        return cmds


class avdb_l1_bulk_store_2_2(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/11 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/24 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                ]
        return cmds


class avdb_gf_hoist_2(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 71 vlan 250 eth 0/1/2 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/3 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 73 vlan 250 eth 0/1/4 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 74 vlan 250 eth 0/1/5 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 75 vlan 250 eth 0/1/6 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 76 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 77 vlan 250 eth 0/1/8 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 78 vlan 250 eth 0/1/9 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 79 vlan 250 eth 0/1/10 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                ]
        return cmds


class avdb_gf_hoist_1_4(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 71 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/3 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 73 vlan 250 eth 0/1/4 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 74 vlan 250 eth 0/1/5 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 75 vlan 250 eth 0/1/6 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 76 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 77 vlan 250 eth 0/1/8 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                ]
        return cmds


class avdb_gf_st6_rec1_1(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 71 vlan 250 eth 0/1/8 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/16 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',]
        return cmds


class avdb_l1_bulk_store_2_1(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 71 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/24 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',]
        return cmds


class avdb_gf_hoist_3_1(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/2 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/3 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 73 vlan 250 eth 0/1/4 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 74 vlan 250 eth 0/1/5 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 75 vlan 250 eth 0/1/6 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 76 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 77 vlan 250 eth 0/1/8 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 78 vlan 250 eth 0/1/9 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 79 vlan 250 eth 0/1/13 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',]
        return cmds


class avdb_l1_bulk_store_2_3(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/6 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                ]
        return cmds


class avdb_l1_hoist_9(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/2 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/3 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 73 vlan 250 eth 0/1/4 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 74 vlan 250 eth 0/1/5 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 75 vlan 250 eth 0/1/6 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 76 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 77 vlan 250 eth 0/1/8 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                ]
        return cmds


class avdb_l1_wchair_3(ReactorlessCommando):
    def to_huawei(self, dev, commands=None, extra=None):
        cmds = ['config',
                'service-port 70 vlan 250 eth 0/1/1 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 71 vlan 250 eth 0/1/2 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 72 vlan 250 eth 0/1/3 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 74 vlan 250 eth 0/1/5 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 75 vlan 250 eth 0/1/6 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',
                'service-port 76 vlan 250 eth 0/1/7 multi-service user-vlan 250 tag-transform translate inbound traffic-table index 7 outbound traffic-table index 7',]
        return cmds
