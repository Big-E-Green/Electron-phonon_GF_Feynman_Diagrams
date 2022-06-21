from cgitb import small
from numpy import zeros
from generator import *
from copy import deepcopy
import timeit
from functions import *

def reachzero(start,array):
    c=0
    hold=[]
    RAY=array.copy()
    while len(RAY)!=0:         
        c=c+1
        for k in RAY:
            if k[0]==start:
                start=k[1]
                hold.append(k)
                RAY.remove(k)
                if k[1]=='1p':
                    return True, hold
            if c>10:
                return False, hold

def loopcheck(var,i):
    c=0
    hold=[]
    tmp=var
    print(tmp)
    while len(i)!=0:
        c=c+1      
        for k in i:
            if k[0]==tmp:
                if k[1]!='1p':
                    tmp=k[1]
                    hold.append(k)
                    if k[0]==k[1]:
                        return True, hold
                    if k[1]==var:
                        return True, hold
            if c>10:
                i=[]
                return False, hold

def contains_critial_loop(arr):
    c=0
    for k in arr:
        c=c+1
        if k[0]=='1p':
            z1=smallloopcheck(k[0],arr)
            if z1[0]==True:
                return True
        if k[0]=='11':
            z2=smallloopcheck(k[0],arr)
            if z2[0]==True:
                return True      
        if c==len(arr):
            return False

def counterpart(n,inters):
    for i in inters:
        if i[0]==n:
            return i[1]
        if i[1]==n:
            return i[0]

def tmpp(arr):
    sav_arr=[]
    while len(arr)>0:
        for i in arr:
            if i[0]=='11':
                tmp=i[1]
                sav_arr.append(i[1])
                arr.remove(i)
            if i[0]==tmp:
                tmp=i[1]
                if tmp!='11':
                    sav_arr.append(i[1])
                    arr.remove(i)
                if tmp=='11':
                    if '1p' in sav_arr:
                        sav_arr.remove('1p')
                    return(sav_arr)

def checker(inn,loop):
    savv=[]
    while len(loop)>0:
        for i in loop:
            if i[0]==inn:
                tmp=i[1]
                loop.remove(i)
                savv.append(i[1])
            if i[0]==tmp:
                tmp=i[1]
                if tmp!=inn:
                    loop.remove(i)
                    savv.append(i[1])
                if tmp==inn:
                    return savv

def connectedDiagrams(n):
    s=timeit.default_timer()
    gun2=all_diags(n)
    cheeko=genall(n)
    ARRAY=gun2.copy()
    connected=[]
    for z in ARRAY:
        zulu=deepcopy(z)
        true_check=[]
        for k in z:
            for p in k:
                zero=reachzero(p,z)
                true_check.append(zero[0])
        if False not in true_check:
            connected.append(zulu)
        if False in true_check:
            if True in true_check:
                ss=contains_critial_loop(z)
                if ss==False: 
                    kk=tmpp(z)
                    while len(kk)!=0:
                        for i in kk:
                            jj=counterpart(i,cheeko)
                            slc=smallloopcheck(jj,z)
                            if slc[0]==True:
                                kk.remove(i)
                                if len(kk)==0:
                                    connected.append(zulu)
                            blc=bigloopcheck(jj,z)
                            if blc[0]==True:
                                dd=checker(jj,blc[1])
                                for q in dd:
                                    if q == '11':
                                        dd.remove(q)
                                    if q == '1p':
                                        dd.remove(q)
                                    if q in kk:
                                        dd.remove(q)
                                    if len(dd)==0:
                                        kk.remove(i)    
                        if len(kk)==0:
                            if zulu not in connected:
                                connected.append(zulu)

    st=timeit.default_timer()
    print('Time Disconected:',st-s)           
    return connected
#print(connectedDiagrams(2))