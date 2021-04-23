#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python


def printResults(cmd):
    """
    printResult: just print results from commando

    """
    
    print("\n\n[++] RESULTS:")
    for c_id, c_info in cmd.results.items():
        for key in c_info:
            print("[+] DEV: {}   CMD: {}\n{}".format(c_id,
                                                     key,
                                                     c_info[key].decode('utf-8')))

    if len(cmd.errors) != 0:
        print("[++] ERRORS:")
        #print(cmd.errors.items())
        for c_id, c_info in cmd.errors.items():
            print("[+]" + c_id, c_info)
    else:
        print("[++] No errors")
