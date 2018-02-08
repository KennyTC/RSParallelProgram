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
result_set = set()
c_key = ""
for line in sys.stdin:
    try:
        line = line.strip()
        key, values = line.split("\t",1)
        # Convert values to set
        c_ret = convert_value_to_set(values)
        if c_key == "":
            c_key = key
            result_set = c_ret
        else:
            result_set = result_set.intersection(c_ret)
    except Exception as e:
        #print("%s",e)
        pass

if result_set != set():
    # f_file.write('{k}\t{v}\n'.format(k=c_key, v=c_value))
    print('{k}\t{v}\n'.format(k=c_key, v=result_set))
else:
    # f_file.write("No exists")
    print("No exists")
# f_file.close()
