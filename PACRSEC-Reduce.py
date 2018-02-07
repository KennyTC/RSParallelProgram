#!/usr/bin/python3

def compare2keys(key1,key2):
    #print("key1={k1},key2={k2}".format(k1=key1,k2=key2))
    if key1==None:
        return False
    i=0
    ret=True
    while (i< len(key2)):
        if (key1[i]!=key2[i]):
            ret=False
            #print("ret:{0}".format(ret))
            return ret
        i=i+1
    #print("ret:{0}".format(ret))
    return ret

import sys
c_key, c_value = None, ""
for line in sys.stdin:
    line = line.strip()

    try:
        key, value = line.split("\t")
        # print("key={k}, value={v}".format(k=key,v=value))
        # for the first row
        # if c_key==key:
        if compare2keys(c_key,key):
            c_value = c_value+","+ value
        else:
            if c_key:  # c_key is not None then print. If None, i.e., the first row, we skip it
                print('{k}\t{v}'.format(k=c_key, v=c_value))
            c_key = key
            #print("after c_key={0}, key={1}".format(c_key, key))
            c_value = value
    except:
        pass

if c_key==key:
    print('{k}\t{v}'.format(k=c_key, v=c_value))