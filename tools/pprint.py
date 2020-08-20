#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pprint_result: just print results from commando

"""

def printResults(cmd):
    for c_id, c_info in cmd.results.items():
        for key in c_info:
            print("DEV: {}   CMD: {}\n{}".format(c_id,
                                                 key,
                                                 c_info[key].decode('utf-8')))
    
