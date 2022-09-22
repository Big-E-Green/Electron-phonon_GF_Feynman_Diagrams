# Electron-phonon Greens function Feynman diagrams

Upon implementation of the electron-phonon interaction to the standard Green's function for a point particle, we are able to produce a finite amount of Feynman diagrams representing all possible interactions and variations of said interactions depending on some limit 'm'. The relationship between the total number of diagrams and 'm' is then (2m)! where 'm' has to be some integer.

This code aims to generate possible diagrams for the given 'm' and find the most fundamental self-energy insertions. This is done first through the generation of all diagrams, then the reduction to connected only diagrams. We then reduce further to those which are topologically inequivalent, finally analysing those insertions in the topologically inequivalent diagrams which cannot be further reduced given the implementation of a full electronic and phononic Green's function representation.
