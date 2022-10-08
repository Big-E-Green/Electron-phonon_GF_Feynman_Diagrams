from el_ph_disconnected import *
import itertools

def all_swapps(inp_n):
    all_trans=[]

    kk_indiv=[]
    for i in pair_gen(inp_n):              # gens individual k-->k' transforms
        kk_indiv.append(i)   
    kk_multi=[]                     
    n_var=inp_n-1                   
    while n_var!=0:
        permute=list(itertools.combinations(kk_indiv,n_var))
        kk_multi.append(permute)
        n_var-=1
    for i in kk_multi:
        all_trans.extend(i)               # gens all k-->k' transf permutations

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
                pair_swaps_indiv.append(i)     # gens individual swap pairs
    pair_multi=[]                     
    n_var=inp_n-1                     
    while n_var!=0:
        permute=list(itertools.combinations(pair_swaps_indiv,n_var))
        for i in permute:
            pperm=[]
            for j in i:
                for k in j:
                    pperm.append(k)
            pair_multi.append(pperm)
        n_var-=1
    all_trans.extend(pair_multi)     # gens all swap pair permutations

    kk_intpair_combs=[]
    for i in kk_multi:
        for j in i:
            for o in pair_multi:
                tmp=[]
                tmp.extend(j)
                tmp.extend(o)
                kk_intpair_combs.append(tmp)
    for i in kk_intpair_combs:
       all_trans.append(i)         # gens all permutations of k-->k' and swap pairs
    return all_trans