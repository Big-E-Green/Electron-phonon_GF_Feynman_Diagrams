from math import dist
from pyparsing import line
from topologicalInequiv import *
from copy import deepcopy
from generator import *

def counterpart(n,inters):
    for i in inters:
        if i[0]==n:
            return i[1]
        if i[1]==n:
            return i[0]

def rev_slice(mylist):
    a = mylist[::-1]
    return a

def bubble(ARR):
    arr=deepcopy(ARR)
    cool=[]
    c=0
    for i in arr:
        c=c+1
        ii=rev_slice(i)
        if ii in arr:
            if i not in cool:
                if i[1]!=i[0]:
                    cool.append(i)
            if ii not in cool:
                if i[1]!=i[0]:
                    cool.append(ii)
        if c==len(ARR):
            if cool==[]:
                return False, cool
            if cool!=[]:
                return True, cool

def on_line(inp,arr):
    ret_arr=[]
    tmp=[]
    c=0
    while len(arr)>0:
        c=c+1
        for i in arr:
            if i[0]==inp:
                tmp=i[1]
                ret_arr.append(i)
                if i[1]=='11' or i[1]=='1p':
                    return True, ret_arr
            if i[0]==tmp:
                tmp=i[1]
                ret_arr.append(i)
                if i[1]=='11' or i[1]=='1p':
                    ret_arr.remove(i)
                    return True, ret_arr
        if c>3:
            return False, ret_arr

def var_to_var(inp,arr):
    ret_arr=[]
    tmp=[]
    c=0
    ARR=deepcopy(arr)
    while len(ARR)>0:
        c=c+1
        for i in ARR:
            if i[0]==inp:
                tmp=i[1]
                ret_arr.append(i)
                ARR.remove(i)
                if i[1]==inp:
                    ret_arr.append(i)
                    return True, ret_arr
            if i[0]==tmp:
                tmp=i[1]
                ret_arr.append(i)
                ARR.remove(i)
                if i[1]==inp:
                    ret_arr.remove(i)
                    ret_arr.append(i)
                    return True, ret_arr
        if c>3:
            return False, ret_arr

def loops_path(init,arr):
    i1=init
    i2=rev_slice(init)
    sav_arr=[]
    c=0
    tmp=[]
    safe_check=0
    while len(i1)>0:
        c=c+1
        for i in arr:
            a=i1[0]
            b=i1[1]
            if i[0]==a:
                tmp=i[1]
                sav_arr.append(i)
                if i[0]==i[1]:
                    return False, sav_arr
                if i[1]=='11' or i[1]=='1p':
                    c=3
            if tmp==b:
                return False, sav_arr
            if tmp==a:
                return False, sav_arr
            if i[0]==tmp:
                tmp=i[1]
                sav_arr.append(i)
                if i[1]==b:
                    return True, sav_arr
                if i[1]=='11' or i[1]=='1p':
                    c=3
        if c==3:
            safe_check=safe_check+1
            i1=i2
            sav_arr=[]
            tmp=[]
            if safe_check==2:
                return False, sav_arr, 'odd out'
n=3
digs=distinctDiagrams(n,True)
all_vars=['11', '1p']
hartree=genny(n)
hartree.remove('11')
hartree.remove('1p')
Hartree=[]
for i in hartree:
    tmp=[]
    tmp.append(i)
    tmp.append(i)
    Hartree.append(tmp)
fock=genall2(n)
fock.remove(['11', '1p'])
Fock=[]
for i in fock:
    Fock.append(i)
    Fock.append(rev_slice(i))
bolo=genall2(n)
bolo.remove(['11', '1p'])
inters=genall2(n)

for i in digs:
    truei=deepcopy(i)
    tmparr=[]
    for k in bolo:
        zultan=loops_path(k,i)
        tmparr.append(zultan[1])
    tmp2arr=[]
    tmp3arr=[]
    for q in tmparr:
        if len(q)==1:
            tmp3arr.append(q)
        if len(q)>1:
            tmp2arr.append(q)
    one=[]
    for o in tmp2arr:
        for hp in o:
            for d in hp:
                one.append(d)
    tmp_var_hartree=[]
    for k in Hartree:
        if k in i:
            count=counterpart(k[0],inters)
            line_check=on_line(count,i)
            if line_check[0]==True:
                if one==[]:  
                    i.remove(k)
                    tmp_var_hartree.append(count)
                if one!=[]:
                    if count not in one:
                        i.remove(k)
                        tmp_var_hartree.append(count)
    tmp_var_fock=[]
    for o in Fock:
        if o in i:
            line_check=on_line(o[0],i)
            if line_check[0]==True:
                if one==[]:
                    i.remove(o)
                    tmp_var_fock.append(o)
                if one!=[]:
                    if o[1] not in one or o[0] not in one:
                        i.remove(o)
                        tmp_var_fock.append(o)
    for j in tmp_var_hartree:
        a=[]
        b=[]
        tmp_add=[]
        tmp2=[]
        for l in i:
            if j==l[0]:
                a=l[1] 
                tmp2.append(l)
            if j==l[1]:
                b=l[0]
                tmp2.append(l)
            if a!=[] and b!=[]:
                tmp=[]
                tmp.append(b)
                tmp.append(a)
                tmp_add.append(tmp)
                for p in tmp2:
                    i.remove(p) 
        for h in tmp_add: 
            i.append(h)
    for f in tmp_var_fock:
        A=[]
        B=[]
        fin_tmp=[]
        tmp22=[]
        for z in i:
            if f[0]==z[1]:
                A=z[0]
                tmp22.append(z)
            if f[1]==z[0]:
                B=z[1]
                tmp22.append(z)
            if A!=[] and B!=[]:
                tmp=[]
                tmp.append(A)
                tmp.append(B)
                fin_tmp.append(tmp)
                for q in tmp22:
                    i.remove(q)
        for a in fin_tmp:
            i.append(a)
    tmp_var_bubble=[]
    float_var=[]
    revvo=[]
    ggg=bubble(i)
    if ggg[0]==True:
        jj=ggg[1]
        for k in jj:
            if '11' in k or '1p' in k:
                i.remove(k)
                for l in k:
                    if l!='11' and l!='1p':
                        if l not in float_var:
                            float_var.append(l)
                            if len(float_var)==2:
                                for s in float_var:
                                    cc=counterpart(s,inters)
                                    revvo.append(cc)
            else:
                counter1=counterpart(k[0],inters)
                counter2=counterpart(k[1],inters)
                c1=on_line(counter1,i)
                c2=on_line(counter2,i)
                if c1[0] == True and c2[0] == True:
                    if k in i:
                        i.remove(k)
                        for e in k:
                            cc=counterpart(e,inters)
                            if cc not in tmp_var_bubble:
                                tmp_var_bubble.append(cc)
    if len(revvo)==2:
        float_var2=rev_slice(revvo)
        if revvo in i and float_var2 in i:
            i.remove(revvo)
            i.remove(float_var2)
    for j in tmp_var_bubble:
        a=[]
        b=[]
        tmp_add=[]
        tmp2=[]
        for l in i:
            if j==l[0]:
                a=l[1] 
                tmp2.append(l)
            if j==l[1]:
                b=l[0]
                tmp2.append(l)
            if a!=[] and b!=[]:
                tmp=[]
                tmp.append(b)
                tmp.append(a)
                tmp_add.append(tmp)
                for p in tmp2:
                    i.remove(p) 
        for h in tmp_add: 
            i.append(h)
    on_site=[]
    for k in all_vars:
        zultann=var_to_var(k,truei)
        if zultann[0]==True:
            if len(zultann[1])==4:
                tmp=[]
                for d in zultann[1]:
                    for k in d:
                        if k not in tmp:
                            tmp.append(k)
                iinii=deepcopy(inters)
                for u in iinii:
                    c=0
                    for q in tmp:
                        if q in u:
                            c=c+1
                            if c==2:
                                on_site.append(zultann)
    on_site_two=deepcopy(on_site)       
    for f in on_site:
        c=False
        c1=False
        for l in f[1]:
            if '11' in l:
                c=True
            if '1p' in l:
                c1=True
        if c == True and c1 == True:
            on_site_two.remove(f)
    for e in on_site_two:
        rr=e[1]
        for ww in rr:
            if ww in i:
                i.remove(ww)
                                
digg=[]
inter=genny(n)
for i in digs:
    if i not in digg:
        digg.append(i)
diags=[]
for i in digg:
    tmp=[]
    while len(i)>0:
        for k in inter:
            for l in i:
                if l[0]==k:
                    tmp.append(l)
                    i.remove(l)
                    if len(i)==0:
                        diags.append(tmp)
Digg=[]
for i in diags:
    if i not in Digg:
        Digg.append(i)
        
#for i in Digg:
#    print(i)
#print(len(Digg))