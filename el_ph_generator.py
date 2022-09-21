from itertools import permutations
import timeit

def var_list(n):                        # var_list creates list of varibles 
    vars=[]                             # i.e. 1,1',2,2',3,3',...,n,n'
    c=1
    while n>=c:
        g=str(c)+str(c)
        vars.append(str(g))
        f=str(c)+'p'
        vars.append(str(f))
        c+=1
    return vars

def all_diagrams(n):                    # Finds all permutations of var_list
    s=timeit.default_timer()            # then pairs them with the unaltered var_list
    perm=permutations(var_list(n))      # yielding all possible diagrams
    all_permutations=list(perm)
    final=[]
    for i in all_permutations:
        c=-1
        tmp2=[]
        for k in var_list(n):
            c=c+1
            tmp=[]
            tmp.append(k)
            tmp.append(i[c])
            tmp2.append(tmp)
        final.append(tmp2)
    st=timeit.default_timer()
    print('Time Generator:',st-s)
    return final