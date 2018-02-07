#!/usr/bin/python3
import sys
index=0
for line in sys.stdin:
    try:
        line = line.strip()
        attributes = line.split(",")
        key=attributes[1:-1]
        value=index
        print('{k}\t{v}'.format(k=key,v=value))
        index=index+1
    except:
        pass