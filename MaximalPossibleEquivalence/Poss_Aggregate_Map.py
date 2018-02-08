#!/usr/bin/python3
import os
import sys

def convert_value_to_frozenset(value):
    list_ret = value.split(",")
    list_ret = frozenset(int(i) for i in list_ret)
    return list_ret

# path=os.path.join(os.path.dirname(__file__),"poss_result_attributes.txt")
# f_file=open(path, "r")
# lines=f_file.readlines()
for line in sys.stdin:
    try:
        # set_ret = set()
        key, values = line.split("\t")
        #Convert value into a set of sets
        # for v in values.split("|"):
        #     set_ret.add(convert_value_to_frozenset(v))
        #
        print('{k}\t{v}\n'.format(k=key,v=values))
        # line = f_file.readline()
    except Exception as e:
        print(e)
        pass