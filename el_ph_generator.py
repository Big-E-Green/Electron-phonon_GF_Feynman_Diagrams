from itertools import permutations
import timeit

def var_list(n):                        # var_list creates list of varibles 
    vars=[]                             # i.e. 1,1',2,2',3,3',...,n,n'
    c=1
    while n>=c:
        g=str(c)+str(c)
        f=str(c)+'p'
        vars.extend([str(g),str(f)])
        c+=1
    return vars

def all_diagrams(n):                    # Finds all permutations of var_list
    s=timeit.default_timer()            # then pairs them with the unaltered var_list
    perm=permutations(var_list(n))      # yielding all possible diagrams
    perm=list(perm)
    final=[]
    for i in perm:
        c=-1
        tmp=[]
        for k in var_list(n):
            c+=1
            tmp.append([k,i[c]])
        final.append(tmp)
    st=timeit.default_timer()
    print('Time Generator:',st-s)
    return final