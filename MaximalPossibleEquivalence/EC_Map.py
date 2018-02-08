#!/usr/bin/python3
import sys
index=1
for line in sys.stdin:
    try:
        line = line.strip()
        attributes = line.split(",")
        # print(attributes)
        for i,attribute in enumerate(attributes):
            key=str(i+1)+","+attribute
            value=index
            print('{k}\t{v}'.format(k=key,v=value))
        index=index+1
    except:
        pass