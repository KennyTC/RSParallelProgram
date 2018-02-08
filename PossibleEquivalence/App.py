#!/usr/bin/python3
import os
from functools import reduce
from collections import defaultdict


# from Poss import PossibleEquivalence


class Approximation():
    def __init__(self):
        self.dirname = os.path.dirname(__file__)
        self.poss_aggregate = os.path.join(self.dirname, "poss_aggregate.txt")
        self.app_aggregate = os.path.join(self.dirname, "app_aggregate.txt")

    def convert_value_to_set(self, value):
        list_ret = value.split(",")
        list_ret = set(int(i) for i in list_ret)
        # list_ret = set(value.split(","))
        return list_ret

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

            list_lower_app, list_upper_app = [], []
            aggregated_lower_app, aggregated_upper_app = set(), set()

            poss_d = self.convert_possible_decision_list()
            f_poss = open(self.poss_aggregate, "r")
            l_line = f_poss.readline().strip()

            """ Approximations and Aggregated
            """
            while l_line != "":
                key, value = l_line.split("\t")
                for v in value.split("|"):
                    v_set = self.convert_value_to_set(v)
                    if bool(v_set) == True:
                        for d_set in poss_d:
                            if v_set.issubset(d_set):
                                list_lower_app.append(v_set)
                                list_upper_app.append(v_set)
                                aggregated_lower_app.update(v_set)
                                aggregated_upper_app.update(v_set)
                            elif v_set.intersection(d_set):
                                list_upper_app.append(v_set)
                                aggregated_upper_app.update(v_set)
                l_line=f_poss.readline().strip()
            f_poss.close()

            f_app_file = open(self.poss_aggregate, "w+")
            f_app_file.write("lower:\t{0}\n".format(list_lower_app))
            f_app_file.write("upper:\t{0}\n".format(list_upper_app))
            f_app_file.write("lower aggregated:\t{0}\n".format(aggregated_lower_app))
            f_app_file.write("upper aggragated:\t{0}\n".format(aggregated_upper_app))
            f_app_file.close()

        except Exception as e:
            print(e)


a = Approximation()
a.approximation()
