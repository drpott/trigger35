#!/usr/bin/env python

import csv
import json


def convertCSVToJson():
    csvfile = open('mac_pk_onts1.csv', 'r')
    jsonfile = open('devs.json', 'w')
    
    fieldnames = ("nodeName", "adminStatus", "manufacturer", "make", "model",
                  "deviceType", "operationStatus", "authMethod", "loginPW", "enablePW", "site", "serialNumber", "OLTInterface", "ipAddr")

    reader = csv.DictReader(csvfile, fieldnames)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

if __name__ ==  "__main__":
    convertCSVToJson()
