#!/usr/bin/python3

import sys
import os


def convert_value_to_set(values):
    set_ret = set()
    for v in values.split("|"):
        f_set = frozenset(v.split(","))
        set_ret.add(f_set)
    return set_ret


# path=os.path.join(os.path.dirname(__file__),"poss_aggregate_result.txt")
# f_file=open(path,"w+")
# f_file=open("poss_aggregate_result.txt","w+")
set_ret = set()
c_key = ""
for line in sys.stdin:
    try:
        line = line.strip()
        key, values = line.split("\t",1)
        # Convert values to set
        c_ret = convert_value_to_set(values)
        print("c_ret {0}".format(c_ret))
        if c_key == "":
            c_key = key
            set_ret = c_ret
        else:
            set_ret = set_ret.intersection(c_ret)
    except Exception as e:
        #print("%s",e)
        pass

if set_ret != set():
    # f_file.write('{k}\t{v}\n'.format(k=c_key, v=c_value))
    print('{k}\t{v}\n'.format(k=c_key, v=set_ret))
else:
    # f_file.write("No exists")
    print("No exists")
# f_file.close()
