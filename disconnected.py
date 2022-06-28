from generator import *
from functions import *
import timeit
from copy import deepcopy

def connectedDiagrams(n):
    s=timeit.default_timer()
    gun2=all_diags(n)
    cheeko=genall(n)
    ARRAY=gun2.copy()
    connected=[]
    for z in ARRAY:
        zulu=deepcopy(z)
        ZERO_CHECK=deepcopy(z)
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
                    kk2=tmpp(z)
                    kk=kk2[0]
                    for zz in kk2[1]:
                        if zz in ZERO_CHECK:
                            ZERO_CHECK.remove(zz)
                    cc=0
                    while ZERO_CHECK!=[]:
                        cc=cc+1
                        if cc==10:
                            ZERO_CHECK=[]
                        for i in kk:
                            jj=counterpart(i,cheeko)
                            slc=smallloopcheck(jj,zulu)
                            if slc[0]==True:
                                kk.remove(i)
                                for h in slc[1]:
                                    ZERO_CHECK.remove(h)
                                    if ZERO_CHECK==[]:
                                        connected.append(zulu)
                            blc=bigloopcheck(jj,z)
                            if blc[0]==True:
                                for t in blc[1]:
                                    if t in ZERO_CHECK:
                                        ZERO_CHECK.remove(t)
                                        if ZERO_CHECK==[]:
                                            connected.append(zulu)
                                if ZERO_CHECK!=[]:
                                    dd=checker(jj,blc[1])
                                    for q in dd:
                                        if q=='1p':
                                            dd.remove(q)
                                        if q=='11':
                                            dd.remove(q)
                                    for q in dd:
                                        if dd!=[]:
                                            JJ=counterpart(q,cheeko)
                                            sl=smallloopcheck(JJ,zulu)
                                            bl=bigloopcheck(JJ,zulu)
                                            if sl[0]==True:
                                                dd.remove(q)
                                                for pp in sl[1]:
                                                    if pp in ZERO_CHECK:
                                                        ZERO_CHECK.remove(pp)
                                                        if ZERO_CHECK==[]:
                                                            connected.append(zulu)
                                            if bl[0]==True:
                                                for tt in bl[1]:
                                                    if tt in ZERO_CHECK:
                                                        ZERO_CHECK.remove(tt)
                                                        if ZERO_CHECK==[]:
                                                            connected.append(zulu)                                                  
    st=timeit.default_timer()
    print('Time Disconected:',st-s)           
    return connected

print(len(connectedDiagrams(3)))