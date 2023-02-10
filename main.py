from el_ph_topological_inequiv import *

def main():
    print('----------------------------------------------------------------')
    print('This code was created by Elliott Green with the help and supervision of Prof Lev Kantorovitch for a Physics Msc project at Kings College London - Project entitled \'Inelastic Tunnelling\'.')
    print('----------------------------------------------------------------')
    print('This code given an input of m, will return all possible diagrams, all connected diagrams then all topologically inequivalent diagrams for the given m.')
    print('NOTE 1: for m>4 it does work but takes a very long time to generate the topologically inequivalent terms.')
    print('NOTE 2: 00 on the left index refers to the start point \'b\' and 00 on the right refers to the end point \'a\'. In the case of the electron-phonon the endpoints are 11 and 1p as they are independently anchored to a and b respectively.')
    print('----------------------------------------------------------------')
    n=int(input('Which order of diagrams do you want? [any integer] '))
    print()
    total=input('Display every diagram from all diagrams? [y/n] ')
    print()
    total2=input('Display every diagram from connected diagrams? [y/n] ')
    print()
    total3=input('Display every diagram from topologically inequivalent diagrams? [y/n] ')
    print()
    num_string=[]
    for i in genall2_ph(n):         # gens all pairs
        for j in i:                                              
            num_string.append(j)
    connected=[]
    for i in all_diagrams_ph(n):      # gens all diagrams
        if total=='y':
            print(i)
        result=connected_check_ph(i,n)     # checks if connected
        if result==True:
            connected.append(i)
    print('Total number of diagrams:',len(all_diagrams_ph(n)))
    print()
    if total2=='y':
        for i in connected:
            print(i)
    print('Total number of connected diagrams:',len(connected))
    print()
    tmp=[]
    while len(connected)!=0:
        for i in connected: 
            tmp.append(i)                                   
            connected.remove(i)                             
            if total3=='y':
                print(i)
            for j in all_swapps_ph(n):                      #gens all transforms
                translated=reparam_ph(j,i,num_string)       #reparams the transfrom
                if translated in connected:                 # if in connected, removes
                    connected.remove(translated)
    print('Total number of topologically inequivalent diagrams:',len(tmp))
    print()

if __name__ == "__main__":
    main()