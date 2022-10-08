from el_ph_topological_inequiv import *

def main():
    n=3
    num_string=[]
    for i in genall2(n):
        for j in i:                                              
            num_string.append(j)
    connected=[]
    for i in all_diagrams(n):
        result=connected_check(i,n)
        if result==True:
            connected.append(i)
    print(len(connected))
    for i in connected: 
        for j in all_swapps(n): 
            translated=reparam(j,i,num_string)
            if translated in connected:
                connected.remove(translated)
    print(len(connected))

if __name__ == "__main__":
    main()