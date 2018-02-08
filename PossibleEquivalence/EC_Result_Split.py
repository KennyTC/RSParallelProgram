#!/usr/bin/python3
import os


def ec_result_split():
    dirname = os.path.dirname(__file__)
    ec_result = os.path.join(dirname, "ec_result.txt")
    ec_result_missing = os.path.join(dirname, "ec_result_missing.txt")
    ec_result_normal = os.path.join(dirname, "ec_result_normal.txt")

    f = open(ec_result, "r")
    f_missing = open(ec_result_missing, "w+")
    f_normal = open(ec_result_normal, "w+")

    l_line = f.readline().strip()
    while l_line != "":
        key, value = l_line.split("\t")
        key_1, key_2 = key.split(",")
        current_key = key_1
        str_missing, str_normal = "", ""
        while current_key == key_1:
            if "*" in key_2:
                str_missing = str_missing + value + ","
            else:
                str_normal = str_normal + value + "|"
            l_line = f.readline().strip()
            if l_line == "":
                break
            key, value = l_line.split("\t")
            key_1, key_2 = key.split(",")
        f_missing.write("{key}\t{value}\n".format(key=current_key, value=str_missing[:-1]))
        f_normal.write("{key}\t{value}\n".format(key=current_key, value=str_normal[:-1]))
    f_missing.close()
    f_normal.close()


ec_result_split()
