#!/usr/bin/env python

from trigger.cmds import ReactorlessCommando


class esnh_bas_b1_cmo(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1',
            'description BMS',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/2-4',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/5-6',
            'description AUDIOSPKR',
            'switchport mode access',
            'switchport access vlan 216',
            'int gig 1/7-15',
            'description CENTREMGMT',
            'switchport mode access',
            'switchport access vlan 220',
            'int gig 1/16',
            'description LIGHTING',
            'switchport mode access',
            'switchport access vlan 214',
            'int gig 1/17',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/18',
            'description HYDRAULIC',
            'switchport mode access',
            'switchport access vlan 207',
            'int gig 1/19',
            'description DIGSIGNAGE',
            'switchport mode access',
            'switchport access vlan 215',
            'int gig 1/20',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/21',
            'description VOIP',
            'switchport mode access',
            'switchport access vlan 210',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 205,202,216,220,214,201,207,215,210,2222,2223',
            'do copy run start',
        ]
        return cmds


class esnh_bas_b2_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-5',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/6',
            'description ACCESSCTRL',
            'switchport mode access',
            'switchport access vlan 203',
            'int gig 1/7-12',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/13-21',
            'description CARPARK',
            'switchport mode access',
            'switchport access vlan 209',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 201,202,203',
            'do copy run start',
        ]
        return cmds



class esnh_bas_b3_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-4',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/5',
            'description BMS',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/6-10',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/11',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/12-13',
            'description HYDRAULIC',
            'switchport mode access',
            'switchport access vlan 207',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 201,202,203',
            'do copy run start',

            'int 10gig 1/1',
            'switchport trunk allowed vlan add 202,203,215,217,2222,2223',
            'do copy run start',
        ]
        return cmds



class esnh_bas_g_02_02(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-8',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/9-12',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/13-16',
            'description DIGSIGNAGE',
            'switchport mode access',
            'switchport access vlan 215',
            'int gig 1/17',
            'description ACCESSCTRL',
            'switchport mode access',
            'switchport access vlan 203',
            'int gig 1/18-20',
            'description PPLCOUNT',
            'switchport mode access',
            'switchport access vlan 217',
            'int gig 1/21-22',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 202,203,215,217,2222,2223',
            'do copy run start',
            'do sh vlan',
        ]
        return cmds


class esnh_bas_g_02_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):

        cmds = [
            'enable',
            'conf t',
            'int gig 1/1',
            'description LIGHTING',
            'switchport mode access',
            'switchport access vlan 214',
            'int gig 1/2',
            'description BMS',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/3-20',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 201,205,214',
            'do copy run start',

            ]
        return cmds


class esnh_bas_b1_01_2(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-8',
            'description EVCHARG',
            'switchport mode access',
            'switchport access vlan 204',
            'int gig 1/9',
            'description BMS',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/10-11',
            'description HYDRAULIC',
            'switchport mode access',
            'switchport access vlan 207',
            'int gig 1/12',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 204,205,2222,2223',
            'do copy run start',
            'do show vlan',

            ]
        return cmds


class esnh_bas_b1_02(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-2',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/3',
            'description LIGHTING',
            'switchport mode access',
            'switchport access vlan 214',
            'int gig 1/4-6',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/7',
            'description ACCESSCTRL',
            'switchport mode access',
            'switchport access vlan 203',
            'int gig 1/8-18',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/19-20',
            'description CARPARK',
            'switchport mode access',
            'switchport access vlan 209',
            'int gig 1/21',
            'description PPLCOUNT',
            'switchport mode access',
            'switchport access vlan 217',
            'int gig 1/22',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 202,214,2222,2223,203,201,207,209,217,2222,2223',
            'do copy run start',
            'do sh vlan',
            ]
        return cmds


class esnh_bas_b2_02(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-8',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/9-20',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 202,201',
            'do copy run start',
            ]
        return cmds


class ESNH_BAS_B2_02_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-2',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/3-8',
            'description CARPARK',
            'switchport mode access',
            'switchport access vlan 209',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 2222,2223,209',
            'do copy run start',
        ]
        return cmds


##
class ESNH_BAS_BLG1B_L5_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-12',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/13',
            'description ACCESSCTRL',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/14',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 202,205',
            'do copy run start',
        ]
        return cmds


class ESNH_BAS_BLG1B_L2_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1',
            'description LIGHTING',
            'switchport mode access',
            'switchport access vlan 214',
            'int gig 1/2',
            'description AUDIOSPKR',
            'switchport mode access',
            'switchport access vlan 216',
            'int gig 1/3-12',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/13-17',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/18',
            'description DIGSIGNAGE',
            'switchport mode access',
            'switchport access vlan 212',
            'int gig 1/19',
            'description NOTICEBRD',
            'switchport mode access',
            'switchport access vlan 219',
            'int gig 1/20-22',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',

            'int 10gig 1/1',
            'switchport trunk allowed vlan add 201,202,214,216,219,2222,2223',

            'do copy run start',
            ]
        return cmds


class ESNH_BAS_BLG1_L7_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1',
            'description LIFTS',
            'switchport mode access',
            'switchport access vlan 211',
            'int gig 1/2',
            'description ACCESSCTRL',
            'switchport mode access',
            'switchport access vlan 203',
            'int gig 1/3',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/4-5',
            'description SOLAR',
            'switchport mode access',
            'switchport access vlan 213',
            'int gig 1/6-7',
            'description SOLAR',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/8-9',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/10',
            'description HYDRAULIC',
            'switchport mode access',
            'switchport access vlan 207',
            'int gig 1/11-18',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',

            'int 10gig 1/1',
            'switchport trunk allowed vlan add 201,202,203,205,207,213',

            'do copy run start',
            ]
        return cmds


class ESNH_BAS_BLG1_L3_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-21',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 202',
            'do copy run start',
            ]
        return cmds


class ESNH_BAS_BLG1_L2_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1',
            'description LIGHTING',
            'switchport mode access',
            'switchport access vlan 214',
            'int gig 1/2',
            'description ACCESSCTRL',
            'switchport mode access',
            'switchport access vlan 203',
            'int gig 1/3-20',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/21',
            'description NOTICEBRD',
            'switchport mode access',
            'switchport access vlan 219',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 202',
            'do copy run start',
            ]
        return cmds



class ESNH_BAS_B3_1A_02(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-5',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/6-8',
            'description ACCESSCTRL',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/9-16',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/17',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/18-19',
            'description HYDRAULIC',
            'switchport mode access',
            'switchport access vlan 207',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 201,202,205,207,2222,2223',
            'do copy run start',
            ]
        return cmds


class ESNH_BAS_B1_1B_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1-3',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/4',
            'description ACCESSCTRL',
            'switchport mode access',
            'switchport access vlan 203',
            'int gig 1/5',
            'description BMS',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/6-16',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/17',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/18-19',
            'description WASTE',
            'switchport mode access',
            'switchport access vlan 212',
            'int gig 1/20',
            'description LIGHTING',
            'switchport mode access',
            'switchport access vlan 214',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',
            'int 10gig 1/1',
            'switchport trunk allowed vlan add 201,202,203,205,212,214,2222,2223',
            
            'do copy run start',
            ]
        return cmds


class ESNH_BAS_G_1B_02(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1',
            'description LIGHTING',
            'switchport mode access',
            'switchport access vlan 214',
            'int gig 1/2',
            'description BMS',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/3-9',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/10-11',
            'description EVCHARGING',
            'switchport mode access',
            'switchport access vlan 204',
            'int gig 1/12',
            'description ACCESSCTRL',
            'switchport mode access',
            'switchport access vlan 203',
            'int gig 1/13-17',
            'description BBWIFI',
            'switchport mode trunk',
            'switchport trunk allowed vlan 5,2222,2223',
            'switchport trunk native vlan 5',
            'int gig 1/24',
            'switchport mode access',
            'switchport access vlan 5',

            'int 10gig 1/1',
            'switchport trunk allowed vlan add 201,203,204,205,2222,2223',

            'do copy run start',
            ]
        return cmds


class ESNH_BAS_G_1B_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'conf t',
            'int gig 1/1-4',
            'description INTERCOM',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/5-6',
            'description BMS',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/7-15',
            'description CCTV',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/16-17',
            'description HYDRAULIC',
            'switchport mode access',
            'switchport access vlan 207',
            'int gig 1/18-19',
            'description WASTE',
            'switchport mode access',
            'switchport access vlan 212',
            'int gig 1/24',
            'description MGMT',
            'switchport mode access',
            'switchport access vlan 5',

            'int 10gig 1/1',
            'switchport trunk allowed vlan 5,212,207,201,205,202',

            'do copy run start',
            ]
        return cmds


class ESNH_BAS_BLG1B_L7_01(ReactorlessCommando):
    def to_adtran(self, dev, commands=None, extra=None):
        cmds = [
            'enable',
            'conf t',
            'int gig 1/1',
            'description LIFTS',
            'switchport mode access',
            'switchport access vlan 211',
            'int gig 1/2',
            'description ACCESSCTRL',
            'switchport mode access',
            'switchport access vlan 203',
            'int gig 1/3',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/4-5',
            'switchport mode access',
            'switchport access vlan 213',
            'int gig 1/6-7',
            'switchport mode access',
            'switchport access vlan 205',
            'int gig 1/8',
            'switchport mode access',
            'switchport access vlan 216',
            'int gig 1/9-13',
            'switchport mode access',
            'switchport access vlan 201',
            'int gig 1/14',
            'switchport mode access',
            'switchport access vlan 207',
            'int gig 1/15-22',
            'switchport mode access',
            'switchport access vlan 202',
            'int gig 1/23-24',
            'switchport mode access',
            'switchport access vlan 5',

            'int 10gig 1/1',
            'switchport trunk allowed vlan add 211,203,213,205,216,207,202',
            'do copy run start',
        ]
        return cmds


class ESNH_BAS_MCR_B1_01(ReactorlessCommando):
        def to_adtran(self, dev, commands=None, extra=None):
            cmds = [
                'enable',
                'conf t',
                'int gig 1/1',
                'description LIGHTING',
                'switchport mode access',
                'switchport access vlan 211',
                'int gig 1/2',
                'description ACCESSCTRL',
                'switchport mode access',
                'switchport access vlan 203',
                'int gig 1/3-4',
                'description PPLCOUNT',
                'switchport mode access',
                'switchport access vlan 217',
                'int gig 1/5-7',
                'description BMS',
                'switchport mode access',
                'switchport access vlan 205',
                'int gig 1/8-13',
                'description DIGSIGNAGE',
                'switchport mode access',
                'switchport access vlan 215',
                'int gig 1/14',
                'description CARPARK',
                'switchport mode access',
                'switchport access vlan 209',
                'int gig 1/15-16',
                'description CCTV',
                'switchport mode access',
                'switchport access vlan 201',
                'int gig 1/17',
                'description BBWIFI',
                'switchport mode trunk',
                'switchport trunk allowed vlan 5,2222,2223',
                'switchport trunk native vlan 5',
                'int gig 1/18',
                'description AUDIOSPKR',
                'switchport mode access',
                'switchport access vlan 216',
                'int gig 1/19-20',
                'description AIRCOND',
                'switchport mode access',
                'switchport access vlan 208',
                'int gig 1/24',
                'switchport mode access',
                'switchport access vlan 5',

                'int 10gig 1/1',
                'switchport trunk allowed vlan add 208,216,2222,2223,201,209,215,205,217,211,203',
                'do copy run start',
            ]

            return cmds


class ESNH_SWT_01(ReactorlessCommando):
        def to_juniper(self, dev, commands=None, extra=None):
            cmds = [
                'configure',
                'set vlans v201 description CCTV vlan-id 201',
                'set vlans v202 description INTRCM vlan-id 202',
                'set vlans v203 description ACCSCTR vlan-id 203',
                'set vlans v204 description EVCHARG vlan-id 204',
                'set vlans v205 description BMS vlan-id 205',
                'set vlans v206 description OIP vlan-id 206',
                'set vlans v207 description HYDRLCS vlan-id 207',
                'set vlans v208 description AIRCON vlan-id 208',
                'set vlans v209 description CARPARK vlan-id 209',
                'set vlans v210 description VOIP vlan-id 210',
                'set vlans v211 description LIFTS vlan-id 211',
                'set vlans v212 description WASTE vlan-id 212',
                'set vlans v213 description SOLAR vlan-id 213 ',
                'set vlans v214 description LITING vlan-id 214',
                'set vlans v215 description DIGSNG vlan-id 215',
                'set vlans v216 description AUDIOSPKR vlan-id 216',
                'set vlans v217 description PPLCTNG vlan-id 217',
                'set vlans v218 description IRRIGATION vlan-id 218',
                'set vlans v219 description NOTICEBRD vlan-id 219',
                'set vlans v220 description CMO vlan-id 220',
                'set vlans v2222 description BBWIFI vlan-id 2222',
                'set vlans v2223 description PUBWIFI vlan-id 2223',

                'set interfaces ge-0/0/1 unit 0 family ethernet-switching interface-mode access vlan members v201',
                'set interfaces ge-0/0/2 unit 0 family ethernet-switching interface-mode access vlan members v201',
                'set interfaces ge-0/0/3 unit 0 family ethernet-switching interface-mode access vlan members v201',
                'set interfaces ge-0/0/4 unit 0 family ethernet-switching interface-mode access vlan members v201',
                'set interfaces ge-0/0/5 unit 0 family ethernet-switching interface-mode access vlan members v202',
                'set interfaces ge-0/0/6 unit 0 family ethernet-switching interface-mode access vlan members v203',
                'set interfaces ge-0/0/7 unit 0 family ethernet-switching interface-mode access vlan members v206',
                'set interfaces ge-0/0/8 unit 0 family ethernet-switching interface-mode access vlan members v207',
                'set interfaces ge-0/0/9 unit 0 family ethernet-switching interface-mode access vlan members v208',
                'set interfaces ge-0/0/10 unit 0 family ethernet-switching interface-mode access vlan members v209',
                'set interfaces ge-0/0/11 unit 0 family ethernet-switching interface-mode access vlan members v219',
                'set interfaces ge-0/0/12 unit 0 family ethernet-switching interface-mode access vlan members v219',
                'set interfaces ge-0/0/13 unit 0 family ethernet-switching interface-mode access vlan members v216',
                'set interfaces ge-0/0/14 unit 0 family ethernet-switching interface-mode access vlan members v216',
                'set interfaces ge-0/0/15 unit 0 family ethernet-switching interface-mode access vlan members v2222',
                'set interfaces ge-0/0/16 unit 0 family ethernet-switching interface-mode access vlan members v204',
                'set interfaces ge-0/0/17 unit 0 family ethernet-switching interface-mode access vlan members v204',

                'set interfaces xe-0/2/0 unit 0 family ethernet-switching vlan members [v201 v202 v203 v204 v205 v206 207 v208 v209 v210 v211 v212 v213 v214 v215 v216 v217 v219 v220 v2222 v2223]',
                'commit confirmed',
            ]

            return cmds


class ESNH_SWT_02(ReactorlessCommando):
        def to_juniper(self, dev, commands=None, extra=None):
            cmds = [
                'configure',
                'set vlans v201 description CCTV vlan-id 201',
                'set vlans v202 description INTRCM vlan-id 202',
                'set vlans v203 description ACCSCTR vlan-id 203',
                'set vlans v204 description EVCHARG vlan-id 204',
                'set vlans v205 description BMS vlan-id 205',
                'set vlans v206 description OIP vlan-id 206',
                'set vlans v207 description HYDRLCS vlan-id 207',
                'set vlans v208 description AIRCON vlan-id 208',
                'set vlans v209 description CARPARK vlan-id 209',
                'set vlans v210 description VOIP vlan-id 210',
                'set vlans v211 description LIFTS vlan-id 211',
                'set vlans v212 description WASTE vlan-id 212',
                'set vlans v213 description SOLAR vlan-id 213 ',
                'set vlans v214 description LITING vlan-id 214',
                'set vlans v215 description DIGSNG vlan-id 215',
                'set vlans v216 description AUDIOSPKR vlan-id 216',
                'set vlans v217 description PPLCTNG vlan-id 217',
                'set vlans v218 description IRRIGATION vlan-id 218',
                'set vlans v219 description NOTICEBRD vlan-id 219',
                'set vlans v220 description CMO vlan-id 220',
                'set vlans v2222 description BBWIFI vlan-id 2222',
                'set vlans v2223 description PUBWIFI vlan-id 2223',

                'set interfaces ge-0/0/1 unit 0 family ethernet-switching interface-mode access vlan members v201',
                'set interfaces ge-0/0/2 unit 0 family ethernet-switching interface-mode access vlan members v201',
                'set interfaces ge-0/0/3 unit 0 family ethernet-switching interface-mode access vlan members v201',
                'set interfaces ge-0/0/4 unit 0 family ethernet-switching interface-mode access vlan members v219',
                'set interfaces ge-0/0/5 unit 0 family ethernet-switching interface-mode access vlan members v205',
                'set interfaces ge-0/0/6 unit 0 family ethernet-switching interface-mode access vlan members v216',
                'set interfaces ge-0/0/7 unit 0 family ethernet-switching interface-mode access vlan members v206',
                'set interfaces ge-0/0/8 unit 0 family ethernet-switching interface-mode access vlan members v207',
                'set interfaces ge-0/0/9 unit 0 family ethernet-switching interface-mode access vlan members v208',
                'set interfaces ge-0/0/10 unit 0 family ethernet-switching interface-mode access vlan members v2223',
                'set interfaces ge-0/0/11 unit 0 family ethernet-switching interface-mode access vlan members v204',

                'set interfaces xe-0/2/0 unit 0 family ethernet-switching vlan members [v201 v202 v203 v204 v205 v206 207 v208 v209 v210 v211 v212 v213 v214 v215 v216 v217 v219 v220 v2222 v2223]',
                'commit confirmed',
            ]

            return cmds
