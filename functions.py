from copy import deepcopy

def smallloopcheck(var,i):
    c=0
    hold=[]
    tmp=var
    while len(i)!=0:
        c=c+1      
        for k in i:
            if k[0]==tmp:
                if k[1]!='00':
                    tmp=k[1]
                    hold.append(k)
                    if k[0]==k[1]:
                        return True, hold
                    if k[1]==var:
                        return False, hold
def bigloopcheck(var,i):
    c=0
    hold=[]
    tmp=var
    while len(i)!=0:
        c=c+1      
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
def genloopcheck(var,i):
    c=0
    hold=[]
    tmp=var
    while len(i)!=0:
        c=c+1      
        for k in i:
            if k[0]==tmp:
                if k[1]!='00':
                    tmp=k[1]
                    hold.append(k)
                    if k[0]==k[1]:
                        return True, hold
                    if k[1]==var:
                        return True, hold
            if c>10:
                i=[]
                return False, hold

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
                if k[1]=='00':
                    return True, hold
            if c>10:
                return False, hold

def loopcheck(var,i):
    c=0
    hold=[]
    tmp=var
    while len(i)!=0:
        c=c+1      
        for k in i:
            if k[0]==tmp:
                if k[1]!='00':
                    tmp=k[1]
                    hold.append(k)
                    if k[0]==k[1]:
                        return True, hold
                    if k[1]==var:
                        return True, hold
            if c>10:
                i=[]
                return False, hold

def closes(gamma,i,sig):
    rho=gamma[1]
    for j in rho:
        for k in j:
            c=0
            while c<10:
                c=c+1
                for a in sig:
                    if k in a:
                        c=11
                    if c==9:
                        return True
