#!/usr/bin/python3

import sys
c_key = None
for line in sys.stdin:
    line = line.strip()
    try:
        key, value = line.split("/t")
        if c_key==key:
            continue
        else:
            if c_key:  # c_key is not None then print. If None, i.e., the first row, we skip it
                print('{k}/t{v}'.format(k=c_key, v=value))
            c_key = key
    except:
        pass

if c_key==key:
    print('{k}/t{v}'.format(k=c_key, v=value))
