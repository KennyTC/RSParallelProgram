#!/usr/bin/python3
import os
from functools import reduce
from collections import defaultdict


class MaximalEquivalence:
    def __init__(self):
        self.path = os.getcwd()
        self.ec_result_missing = self.path + "/ec_result_missing.txt"
        self.ec_result_normal = self.path + "/ec_result_normal.txt"
        self.poss_result = self.path + "/poss_result.txt"
        self.poss_result_attributes = self.path + "/poss_result_attributes.txt"
        self.poss_result_decision = self.path + "/poss_result_decision.txt"
        self.app_result = self.path + "/app_result.txt"
        self.id_to_ignore_in_ec_result_normal = 3
        self.id_to_aggregate = 2  # We will aggregate attributes from 1 to this number

    def convert_value_to_set(self, value):
        list_ret = value.split(",")
        list_ret = set(int(i) for i in list_ret)
        # list_ret = set(value.split(","))
        return list_ret

    def dict_of_missing(self):
        try:
            dict_ret = {}

            f_file = open(self.ec_result_missing, "r")
            l_line = f_file.readline().strip()
            while l_line != "":
                k_key, v_value = l_line.split("\t")
                dict_ret[k_key] = self.convert_value_to_set(v_value)
                l_line = f_file.readline().strip()

            return dict_ret
        except Exception as e:
            print(e)

    # Convert possible decision into lists
    def convert_possible_decision_list(self):
        try:
            list_ret = []
            f_file = open(self.poss_result_decision, "r")
            l_line = f_file.readline().strip()
            while l_line != "":
                key, value = l_line.split("\t")
                for v in value.split("|"):
                    list_ret.append(self.convert_value_to_set(v))
                l_line = f_file.readline().strip()
        except Exception as e:
            print(e)
        return list_ret

    def approximation(self):
        try:
            dict_lower_app, dict_upper_app = defaultdict(list), defaultdict(list)
            dict_of_missing = self.dict_of_missing()
            poss_d = self.convert_possible_decision_list()

            f_ec_result = open(self.ec_result_normal, "r")
            l_line = f_ec_result.readline().strip()

            """ lower approximations
            """
            while l_line != "":
                key, value = l_line.split("\t")
                if int(key) == self.id_to_ignore_in_ec_result_normal:
                    l_line = f_ec_result.readline().strip()
                    continue
                for v in value.split("|"):
                    v_set = self.convert_value_to_set(v)
                    for d_set in poss_d:
                        if v_set.issubset(d_set):
                            lower_set = v_set.union(dict_of_missing[key].intersection(d_set))
                            if bool(lower_set) == True:
                                if lower_set not in dict_lower_app[key]:
                                    dict_lower_app[key].append(lower_set)
                # When v_set is an empty set
                for d_set in poss_d:
                    lower_set = dict_of_missing[key].intersection(d_set)
                    if bool(lower_set) == True:
                        if lower_set not in dict_lower_app[key]:
                            dict_lower_app[key].append(lower_set)
                l_line = f_ec_result.readline().strip()

            """upper approximation
            """
            f_poss_attr = open(self.poss_result_attributes, "r")
            f_poss_line = f_poss_attr.readline().strip()
            while f_poss_line != "":
                key, value = f_poss_line.split("\t")
                for v in value.split("|"):
                    v_set = self.convert_value_to_set(v)
                    for d_set in poss_d:
                        upper_set = v_set.intersection(d_set)
                        if bool(upper_set):
                            if v_set not in dict_upper_app[key]:
                                dict_upper_app[key].append(v_set)
                f_poss_line = f_poss_attr.readline().strip()

            """ Aggregate
            """
            f_file = open(self.app_result, "w+")
            for key, value in dict_lower_app.items():
                f_file.write("{0}\t{1}\t{2}\n".format(key, value, dict_upper_app[key]))
            f_file.write("Aggregate \n")
            agg_lower = reduce(lambda x, y: set(x).intersection(set(y)), dict_lower_app.values())
            agg_upper = reduce(lambda x, y: set(x).intersection(set(y)), dict_upper_app.values())
            f_file.write("{0}\n{1}\n".format(agg_lower, agg_upper))
            f_file.close()

        except Exception as e:
            print(e)

    # def aggregate(self, dict):
#

a = MaximalEquivalence()
a.approximation()
