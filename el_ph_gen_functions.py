from copy import deepcopy

def genall2_ph(n):                      # generates all varibales and their prime
    One=[]                              # pairs together e.g [11,1p],[22,2p], etc
    c=0
    while n>=c:
        g=str(c)+str(c)
        f=str(c)+'p'
        One.extend([str(g),str(f)])
        c+=1
    One.remove('0p')
    One.remove('00')
    chunk=[]
    for x in range(0, len(One), 2):
        chunk.append(One[x:x+2])
    return chunk

def counterpart_ph(n,inters):           # finds the counterpart to a variable
    for i in inters:                    # e.g 11->1p or 1p->11 or 22->2p etc
        if i[0]==n:
            return i[1]
        if i[1]==n:
            return i[0]

def smallloopcheck_ph(var,i):              #checks for small loops
    c=0                                    # e.g. 11,11 or 1p,1p etc
    hold=[]
    tmp=var
    while len(i)!=0:
        c+=1      
        for k in i:
            if k[0]==tmp:
                hold.append(k)
                if k[0]==k[1]:
                    return True, hold
                if k[0]!=k[1]:
                    return False, hold

def reachzero_ph(start,array):              # will return true/false with its path
    c=0                                     # depending on if it reaches 1p or not
    hold=[]
    RAY=array.copy()
    while len(RAY)!=0:         
        c+=1
        for k in RAY:
            if k[0]==start:
                start=k[1]
                hold.append(k)
                RAY.remove(k)
                if k[1]=='1p':
                    return True, hold
            if c>10:
                return False, hold

def bigloopcheck_ph(var,i):               # checks if there are any big loops
    c=0                                   # if true, returns the loop          
    hold=[]
    tmp=var
    while len(i)!=0:
        c+=1      
        for k in i:
            if k[0]==tmp:
                if k[1]!='00':
                    tmp=k[1]
                    hold.append(k)
                    if k[0]==k[1]:
                        return False, hold
                    if k[1]==var:
                        return True, hold
            if c>10:
                i=[]
                return False, hold

def var_list_noone_ph(n):               # lists all variables in the given n
    vars=[]                             # e.g. 11,1p,22,2p,... (does not conatin 11 or 1p)
    c=2
    while n>=c:
        g=str(c)+str(c)
        f=str(c)+'p'
        vars.extend([str(g),str(f)])
        c+=1
    return vars

def pair_gen_ph(n):                     # generates pairs e.g. 11,1p for the given n
    One=[]
    c=2
    while n>=c:
        g=str(c)+str(c)
        f=str(c)+'p'
        One.extend([str(g),str(f)])
        c+=1
    chunked=[]
    for x in range(0, len(One), 2):
        chunked.append(One[x:x+2])
    return chunked

def swap_ph(translation,numm):      # swapps entries to their correct positions
    cc=[]                           # keeping the 11,1p,22,2p,... first entry format
    for i in translation: 
        c=-1
        for j in numm:
            c+=1
            if j==i:
                cc.append(c)
                if len(cc)==2:
                    return cc
                    
def reparam_ph(trans,inp,numm):   #this reparamiterises the diagram given
    ii=deepcopy(inp)              # a translation (trans) and a diagram inp
    for i in trans:               # num is an index of swapps e.g. 11->1p
        c=-1
        for k in ii:
            c+=1
            c2=-1
            for q in k:
                c2+=1
                if q==i[0]:
                    ii[c][c2]=i[1]      
                if q==i[1]:
                    ii[c][c2]=i[0]
        sw=swap_ph(i,numm)
        ii[sw[0]],ii[sw[1]]=ii[sw[1]],ii[sw[0]]
    return ii