#!/usr/bin/python3
import os
from collections import defaultdict


class PossibleEquivalence:
    def __init__(self):
        self.dirname = os.path.dirname(__file__)
        # self.ec_result = self.path + "/ec_result.txt"
        self.ec_result_missing = os.path.join(self.dirname, "/ec_result_missing.txt")
        self.ec_result_normal = os.path.join(self.dirname, "/ec_result_normal.txt")
        self.poss_result = os.path.join(self.dirname,"/poss_result.txt")

    def convert_value_to_set(self, value):
        list_ret = value.split(",")
        list_ret = set(int(i) for i in list_ret)
        #list_ret = set(value.split(","))
        return list_ret

    def dict_of_missing(self):
        try:
            dict_ret = {}
            f_file = open(self.ec_result_missing, "r")
            l_line = f_file.readline().strip()
            while l_line != "":
                k_key, v_value = l_line.split("\t")
                dict_ret[k_key]=self.convert_value_to_set(v_value)
                l_line = f_file.readline().strip()

            return dict_ret
        except Exception as e:
            print(e)

    def powerset_of_missing(self,items):
        N = len(items)
        for i in range(2 ** N):
            ret = set()
            for j in range(N):
                if (i >> j) % 2 == 1:
                    ret.add(items[j])
            yield ret

    def poss(self):
        try:
            dict_of_missing = self.dict_of_missing()
            f_write = open(self.poss_result, "w+")

            f_normal = open(self.ec_result_normal, "r")
            f_normal_line = f_normal.readline().strip()
            while f_normal_line != "":
                key, value = f_normal_line.split("\t")
                # Search key in dict_of_missing. Return its value as a set. Otherwise, set a empty set
                str_value = ""
                if key in dict_of_missing.keys():
                    v_missing = dict_of_missing[key]
                    str_value = str_value + str(v_missing).replace("{","").replace("}","").strip()+"|"
                else:
                    v_missing = set()
                for v in value.split("|"):
                    v_set = self.convert_value_to_set(v)
                    v_set=v_set.union(v_missing)
                    str_value = str_value + str(v_set).replace("{","").replace("}","").strip() + "|"
                # remove the last | and write to file
                f_write.write("{key}\t{value}\n".format(key=key, value=str_value[:-1]))

                f_normal_line=f_normal.readline().strip()
            f_write.close()
        except Exception as e:
            print(e)

a = PossibleEquivalence()
for i in a.powerset_of_missing([1,3,5]):
    print(i)
