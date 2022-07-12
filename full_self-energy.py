from self_energy import *

Final=[]
for i in Digg:
    fl=0
    c=0
    for t in Fock:
        if t not in i:
            c=c+1
            if c==len(Fock):
                fl=fl+1
    c=0
    for s in Hartree:
        if s not in i:
            c=c+1
            if c==len(Hartree):
                fl=fl+1
    if fl==2:
        Final.append(i)
    def HT(inp_arr):
        c=0
        colo=[]
        while len(inp_arr)>0:
            c=c+1
            for j in Hartree:
                if j in inp_arr:
                    cc=counterpart(j[0],fock)
                    inp_arr.remove(j)
                    new=[]
                    a=[]
                    b=[]
                    tmp=[]
                    for k in inp_arr:
                        if cc==k[0]:
                            a=k[1]
                            tmp.append(k)
                        if cc==k[1]:
                            b=k[0]
                            tmp.append(k)
                        if a!=[] and b!=[]:
                            c=[]
                            c.append(b)
                            c.append(a)
                            new.append(c)
                    colo=inp_arr.copy()
                    for q in new:
                        colo.append(q)
                    for h in tmp:
                        if h in colo:
                            colo.remove(h)
                    return True, colo
            if c>10:
                return False, colo
    kk=True
    c=-1
    zz=[]
    while kk is True:
        for l in Hartree:
            if l in i:
                kk=True        
                zz=HT(i)
                i=zz[1]
            if l not in i:
                c=c+1
                jj=len(Hartree)
                if c>=jj:
                    kk=False
    def FK(inpu_var):
        c=0
        colo2=[]
        while len(inpu_var)>0:
            c=c+1
            for j in Fock:
                if j in inpu_var:
                    one=j[0]
                    two=j[1]
                    tmp=[]
                    new=[]
                    a=[]
                    b=[]
                    for q in inpu_var:
                        if two==q[0]:
                            a=q[1]
                            tmp.append(q)
                        if one==q[1]:
                            b=q[0]
                            tmp.append(q)
                        if a!=[] and b!=[]:
                            c=[]
                            c.append(b)
                            c.append(a)
                            if c not in new:
                                new.append(c)
                    colo2=inpu_var.copy()
                    colo2.remove(j)
                    for q in new:
                        colo2.append(q)
                    for h in tmp:
                        if h in colo2:
                            colo2.remove(h)
                    return True, colo2
            if c>10:
                return False, colo2
    tt=True
    c=-1
    yy=[]
    while tt is True:
        for l in Fock:
            if l in i:
                tt=True        
                yy=FK(i)
                i=yy[1]
            if l not in i:
                c=c+1
                pp=len(Fock)
                if c>=pp:
                    tt=False 
    kk=True
    c=-1
    zz=[]
    while kk is True:
        for l in Hartree:
            if l in i:
                kk=True        
                zz=HT(i)
                i=zz[1]
            if l not in i:
                c=c+1
                jj=len(Hartree)
                if c>=jj:
                    kk=False
    if i not in Final:
        Final.append(i)
Dig_Fin=[]
for i in Final:
    if i not in Dig_Fin:
        Dig_Fin.append(i)
for i in Dig_Fin:
    print(i)
print(len(Dig_Fin))