from el_ph_generator import *
from el_ph_genFunctions import *

def connected_check_ph(inp,n):                           # varifies if a diagram is conn or disconn

    for i in inp:                                        # removal of those containing 1',1'
        if i==['11', '11'] or i==['1p', '1p']:           # or 1,1 (efficient)
            return False  
    
    direct_on_line=[]                                    # finds all on_line varibles
    for k in var_list_ph(n):                             # saves to said array, if all on line
        epsilon=reachzero_ph(k,inp)                      # diagram MUST be connected
        if epsilon[0] is True:
            for l in epsilon[1]:
                for g in l:
                    if g not in direct_on_line:
                        direct_on_line.append(g)
                        if len(direct_on_line)==len(inp):
                            return True
    
    final_big_array=[]
    for q in var_list_ph(n):                                # for each variable in var_list
        eta=bigloopcheck_ph(q,inp)                          # we look to see if contains a bigloop
        if eta[0] is True:                                  # and saves if true
            big_array=[]
            for j in eta[1]:
                for h in j:
                    if h not in big_array:
                        big_array.append(h)
            final_big_array.append(big_array)
    remm=[]

    for w in final_big_array:                           # if bigloop is true it finds if any
        for y in w:                                     # part is connected to the main line in
            if y in direct_on_line:                     # any way, if so the whole bigloop is added
                if w not in remm:                       # to the direct line
                    remm.append(w)
                for t in w:
                    if t not in direct_on_line:
                        direct_on_line.append(t)
            z=counterpart_ph(y,genall2_ph(n))
            if z!='11':
                if z!='1p':
                    if z in direct_on_line:
                        if w not in remm:
                            remm.append(w)
                        for t in w:
                           if t not in direct_on_line:
                              direct_on_line.append(t)
    
    for i in remm:
        if i in final_big_array:
            final_big_array.remove(i)
    if final_big_array!=[]:                            # this is done again but in a while loop
        counter=5                                      # so all bigloops are checked before false
        while counter!=0:                              # is returned
            counter-=1
            for p in final_big_array:
                for f in p:
                    eta=counterpart_ph(f,genall2_ph(n))
                    if eta in direct_on_line:
                        if f not in direct_on_line:
                            direct_on_line.append(f)
                            if f in p:
                                p.remove(f)
    if len(direct_on_line)==len(inp):              
        return True
    for i in var_list_ph(n):                              # we then look for smallloops and see what
        mu=smallloopcheck_ph(i,inp)                       # they are connected to. They must connect
        if mu[0] is True:                                 # in some way or else it HAS to be disconected
            var=mu[1][0][0]
            zeta=counterpart_ph(var,genall2_ph(n))
            if zeta in direct_on_line:
                if var not in direct_on_line:
                    direct_on_line.append(var)
    if len(direct_on_line)==len(inp):
        return True                
    return False