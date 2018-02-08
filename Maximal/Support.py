class Support:
    def split_ec_result(self):
        f=open("ec_result.txt","r")
        l_line=f.readline().strip()

        f_missing = open("ec_result_missing.txt","w+")
        f_normal = open("ec_result_normal.txt", "w+")

        while l_line!="":
            key,value=l_line.split("\t")
            key_1,key_2=key.split(",")
            current_key = key_1
            str_missing,str_normal="",""
            while current_key==key_1:
                if "*" in key_2:
                    str_missing = str_missing +  value + ","
                else:
                    str_normal = str_normal + value + "|"
                l_line = f.readline().strip()
                if l_line=="":
                    break
                key, value = l_line.split("\t")
                key_1, key_2 = key.split(",")
            f_missing.write("{key}\t{value}\n".format(key=current_key,value=str_missing[:-1]))
            f_normal.write("{key}\t{value}\n".format(key=current_key, value=str_normal[:-1]))
        f_missing.close()
        f_normal.close()

    def split_poss_result(self,index):
        f = open("poss_result.txt", "r")
        l_line = f.readline().strip()

        f_attributes = open("poss_result_attributes.txt", "w+")
        f_decision = open("poss_result_decision.txt", "w+")

        while l_line != "":
            key, value = l_line.split("\t")
            if int(key)==int(index):
                f_decision.write("{line}\n".format(line=l_line))
            else:
                f_attributes.write("{line}\n".format(line=l_line))
            l_line = f.readline().strip()
        f_attributes.close()
        f_decision.close()



a=Support()
# a.split_ec_result()
a.split_poss_result(3)