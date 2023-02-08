# Electron-phonon Greens function Feynman diagrams

Upon implementation of the electron-phonon interaction to the standard Green's function of a point particle, we are able to produce a finite amount of Feynman diagrams representing all possible interactions and their variations for some system of 'm' particles. The relationship between the total number of diagrams and particle number 'm' is then (2m)!, where 'm' has to be some integer.

This code aims to generate possible diagrams for the given 'm' and distil them down into their most fundamental forms. This is done through the distinction of connected and disconnected diagram topologies, and then via topological equivalence of like diagrams. This will then result in a few fundamental distinct diagrams which remain. 

NOTE: As a 2m! relationship exists, for increasing values of m the computation time increases factorially (It gets slow at m=5 onwards). 

For more details on the rules of topological inequivalence and self-energy insertions papers can be readily found. 
