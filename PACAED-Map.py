#!/usr/bin/python3
import sys

for line in sys.stdin:
    try:
        line = line.strip()
        attributes = line.split(",")
        key=attributes[1:]
        value=0
        print('{k}/t{v}'.format(k=key,v=value))
    except:
        pass