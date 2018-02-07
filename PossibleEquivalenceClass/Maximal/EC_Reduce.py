#!/usr/bin/python3

import sys
c_key, c_value = "", ""
f_file=open("ec_result.txt","w+")
for line in sys.stdin:
    line = line.strip()
    try:
        key, value = line.split("\t")
        if c_key==key:
            c_value = c_value+","+ value
        else:
            if c_key:  # c_key is not None then print. If None, i.e., the first row, we skip it
                #print('{k}\t{v}'.format(k=c_key, v=c_value))
                f_file.write('{k}\t{v}\n'.format(k=c_key, v=c_value))
            c_key = key
            c_value = value
    except:
        pass

if c_key==key:
    f_file.write('{k}\t{v}\n'.format(k=c_key, v=c_value))
    #print('{k}\t{v}'.format(k=c_key, v=c_value))
f_file.close()