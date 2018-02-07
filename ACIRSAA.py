def check(e,list_d,list_a):
    count=0
    for d in list_d:
        if e.append(d) in list_a:
           count=count+1
    return True if count > 2 else False


def ACIRSAA():
    list_d = [1, 2, 3, 4, 5, 6, 7]
    # load e
    f = open("eq.txt","a")
    list_e = f.read()
    f = open("association.txt","a")
    list_a = f.read()
    for d in list_d: # args =[D1,D2,..,Dn]
        upR=""
        for e in list_e:
            if (e.append(d) in list_a):
                upR=upR+e
    bool=[True*len(list_e)]
    for i,e in enumerate(list_e):
        if check(e,list_d,list_a):#if d1,d2 exists s.t. Ass(e,d1)=True, and Ass(e,d2)=True
            bool[i]=False
    for d in list_d:
        lowR=""
        for i,e in enumerate(list_e):
            if bool[i]==True and e+d in list_a:
                lowR=lowR+e
    return (lowR,upR)



