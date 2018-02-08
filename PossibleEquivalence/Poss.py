#!/usr/bin/python3
import os
from collections import defaultdict


class PossibleEquivalence:
    def __init__(self):
        self.dirname = os.path.dirname(__file__)
        # self.ec_result = self.path + "/ec_result.txt"
        self.ec_result_missing = os.path.join(self.dirname, "ec_result_missing.txt")
        self.ec_result_normal = os.path.join(self.dirname, "ec_result_normal.txt")
        self.poss_result = os.path.join(self.dirname, "poss_result.txt")

    def convert_value_to_set(self, value):
        list_ret = value.split(",")
        list_ret = set(int(i) for i in list_ret)
        return list_ret

    """ 
    Return a dict whose values is [k], where k is power set
    """

    def dict_of_power_of_missing(self):
        try:
            dict_ret = {}
            f_file = open(self.ec_result_missing, "r")
            l_line = f_file.readline().strip()
            while l_line != "":
                k_key, v_value = l_line.split("\t")
                # v_value = list(map(lambda i:int(i),v_value.split(",")))
                v_value =[int(i) for i in v_value.split(",")]
                dict_ret[k_key] = list(self.powerset(v_value))
                l_line = f_file.readline().strip()
            return dict_ret
        except Exception as e:
            print(e)

    def powerset(self, list_of_value):
        N = len(list_of_value)
        for i in range(2 ** N):
            ret = set()
            for j in range(N):
                if (i >> j) % 2 == 1:
                    ret.add(list_of_value[j])
            yield ret

    def poss(self):
        try:
            dict_of_power_of_missing = self.dict_of_power_of_missing()
            f_write = open(self.poss_result, "w+")

            f_normal = open(self.ec_result_normal, "r")
            f_normal_line = f_normal.readline().strip()
            while f_normal_line != "":
                key, values = f_normal_line.split("\t")
                str_value = ""

                # Search key in dict_of_missing. Return its value as a set. Otherwise, set a empty set
                if key in dict_of_power_of_missing.keys():
                    powerset_of_missing = dict_of_power_of_missing[key]
                    powerset_of_missing = powerset_of_missing.remove(set())
                else:
                    powerset_of_missing = set()

                # If power_set_of_missing has no elements, just takes values
                if len(powerset_of_missing) == 0:
                    str_value = values
                else: # If not, we find union btw each element
                    # Add power_of_missing
                    for set_missing in powerset_of_missing:
                        str_value = str_value + str(set_missing).replace("{", "").replace("}", "").strip() + "|"
                    # Add union
                    for value in values.split("|"):
                        value_set = self.convert_value_to_set(value)
                        for set_missing in powerset_of_missing:
                            v_set = sorted(value_set.union(set_missing))
                            str_value = str_value + str(v_set).replace("{", "").replace("}", "").strip() + "|"
                        str_value = str_value[:-1]

                # Remove the last | and write to file
                f_write.write("{key}\t{value}\n".format(key=key, value=str_value))
                f_normal_line = f_normal.readline().strip()
            f_write.close()
        except Exception as e:
            print(e)


a = PossibleEquivalence()
a.poss()
