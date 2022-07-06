# Electron-phonon Greens function Feynman diagrams

Simmilar to the case of an electron-electron interaction, the electron-phonon interaction once applied to the case of one-particle greens function in the interaction picture produces an expression containing: interactions, verteses and g-naught functions. The combination of these enables the production of Feynamn diagrams.

This code aims to process all possible diagrams for m order interactions, removing all disconnected diagrams, and removing all topologically inequivalent diagrams. The remaining diagrams can then be reduced further through reduction of on-bubble Hartree and Fock terms, enabling a clear veiw of all self-energy insertions. A further reduction can then be made into full greens functions, leaving only fundamental diagrams with all possible insertions.
