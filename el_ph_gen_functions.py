from copy import deepcopy

def genall2(n):
    One=[]
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

def counterpart(n,inters):
    for i in inters:
        if i[0]==n:
            return i[1]
        if i[1]==n:
            return i[0]

def smallloopcheck(var,i):
    c=0
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

def reachzero(start,array):
    c=0
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
                if k[1]=='11':
                    return True, hold
            if c>10:
                return False, hold

def bigloopcheck(var,i):
    c=0
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

def var_list_noone(n):
    vars=[]
    c=2
    while n>=c:
        g=str(c)+str(c)
        f=str(c)+'p'
        vars.extend([str(g),str(f)])
        c+=1
    return vars

def pair_gen(n):
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

def swap(translation,numm):
    cc=[]
    for i in translation: 
        c=-1
        for j in numm:
            c+=1
            if j==i:
                cc.append(c)
                if len(cc)==2:
                    return cc
                    
def reparam(trans,inp,numm):   
    ii=deepcopy(inp)
    for i in trans:
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
        sw=swap(i,numm)
        ii[sw[0]],ii[sw[1]]=ii[sw[1]],ii[sw[0]]
    return ii
