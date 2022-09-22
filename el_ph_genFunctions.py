def genall2(n):
    One=[]
    c=0
    while n>=c:
        g=str(c)+str(c)
        One.append(str(g))
        f=str(c)+'p'
        One.append(str(f))
        c+=1
    One.remove('0p')
    One.remove('00')
    chunkii=[]
    for x in range(0, len(One), 2):
        chunkii.append(One[x:x+2])
    return chunkii

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

def var_list_noone(n):                        # var_list creates list of varibles 
    vars=[]                             # i.e. 1,1',2,2',3,3',...,n,n'
    c=2
    while n>=c:
        g=str(c)+str(c)
        vars.append(str(g))
        f=str(c)+'p'
        vars.append(str(f))
        c+=1
    return vars
