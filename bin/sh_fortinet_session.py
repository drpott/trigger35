#!/usr/bin/env python

"""
commando_reactorless.py - Running multiple Commando's in the same script
"""
import sys
sys.path.append(r'/home/dan/python35/trigger35')

from trigger.cmds import ReactorlessCommando
from trigger.tacacsrc import get_device_password
from trigger.netdevices import NetDevices
from twisted.internet import reactor, defer
from twisted.python import log


# Uncomment me for verbose logging.
# import sys
# log.startLogging(sys.stdout, setStdout=False)

def stop_reactor(result):
    if reactor.running:
        log.msg('STOPPING REACTOR!')
        reactor.stop()
    return result

class showSessionList(ReactorlessCommando):
    """Execute 'show clock' on a list of Cisco devices."""
    commands = [b'get system session list']
    vendor = ['fortinet']


if __name__ == '__main__':
    # Replace these with real device IPs/hostnames in your network
    devices = ['fortinet']

    # nd = NetDevices()
    # dev = nd.find('svp00c')
    # async = dev.execute(['show clock'])
    # async.addCallback(print_me)
    
    c1 = showSessionList(devices, creds=get_device_password('fortinet'), )

    instances = [c1]

    # Once every task has returned a result, stop the reactor
    deferreds = []
    for i in instances:
        deferreds.append(i.run())

    d = defer.DeferredList(deferreds)

    d.addBoth(stop_reactor)
    reactor.run()

    for c_id, c_info in c1.results.items():
        for key in c_info:
            print("command: {}\n {}".format(key.decode('utf-8'), c_info[key].decode('utf-8')))

#    print(c1.parsed_results)
