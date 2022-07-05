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

digs=distinctDiagrams(3,False)
hartree=genny(3)
hartree.remove('11')
hartree.remove('1p')
Hartree=[]
for i in hartree:
    tmp=[]
    tmp.append(i)
    tmp.append(i)
    Hartree.append(tmp)
fock=genall2(3)
fock.remove(['11', '1p'])
Fock=[]
for i in fock:
    Fock.append(i)
    Fock.append(rev_slice(i))
bolo=genall2(3)
bolo.remove(['11', '1p'])
inters=genall2(3)

for i in digs:
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

digg=[]
inter=genny(3)
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