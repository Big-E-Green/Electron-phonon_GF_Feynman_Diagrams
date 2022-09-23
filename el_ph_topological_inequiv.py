from re import L
from el_ph_disconnected import *
from el_ph_generator import *
import itertools

def pair_gen(n):
    One=[]
    c=2
    while n>=c:
        g=str(c)+str(c)
        One.append(str(g))
        f=str(c)+'p'
        One.append(str(f))
        c+=1
    chunked=[]
    for x in range(0, len(One), 2):
        chunked.append(One[x:x+2])
    return chunked

def all_swapps(inp_n):
    all_trans=[]

    kk_indiv=[]
    for i in pair_gen(inp_n):       
        kk_indiv.append(i)           # all individual k-k' tansforms
    kk_multi=[]                     
    n_var=inp_n-1                   
    while n_var!=0:
        permute=list(itertools.combinations(kk_indiv,n_var))
        kk_multi.append(permute)
        n_var-=1
    all_trans.append(kk_multi)                  # all kk' vars
    
    perm=list(itertools.combinations(var_list_noone(inp_n),2))
    for i in list(kk_indiv):
        a=i[0]
        b=i[1]
        c=(a,b)
        if c in perm:
            perm.remove(c)
    perm2=list(itertools.combinations(perm,2))
    pair_swaps_indiv=[]
    for i in perm2:
        counter1=counterpart(i[0][0],pair_gen(inp_n))
        counter2=counterpart(i[0][1],pair_gen(inp_n))
        if i[1][0]==counter1:
            if i[1][1]==counter2:
                pair_swaps_indiv.append(i)            # all individual pairswaps
    pair_multi=[]                     
    n_var=inp_n-1                     
    while n_var!=0:
        permute=list(itertools.combinations(pair_swaps_indiv,n_var))
        pair_multi.append(permute)
        n_var-=1
    all_trans.append(pair_multi)                    # all pairswap vars

    kk_intpair_comb=[]                              # finds all kk' + pairswaps
    for i in kk_multi:
        kk_intpair_size=[]
        for j in i:
            for k in pair_multi:
                for l in k:
                    tmp=[]
                    tmp.append(j)
                    tmp.append(l)
                    kk_intpair_size.append(tmp)
        kk_intpair_comb.append(kk_intpair_size)
    all_trans.append(kk_intpair_comb)
    return all_trans
