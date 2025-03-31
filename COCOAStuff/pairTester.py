#!/usr/bin/env python

import numpy as np
import h5py
import uproot

uprootFile = uproot.open("test.root")
tree =  uprootFile[uprootFile.keys()[0]]
branches = tree.arrays()
uprootFile.close()


cell_ilay = np.array(branches["cell_ilay"][0])
cell_ieta = np.array(branches["cell_ieta"][0])
cell_iphi = np.array(branches["cell_iphi"][0])

pairFile = h5py.File("pairData.hdf5", "r")
cellPairs = np.array(pairFile.get("pairData")[:])
pairFile.close()

for pair in cellPairs:
    cell1 = int(pair[0])
    cell2 = int(pair[1])

    ilay1 = cell_ilay[cell1]
    ilay2 = cell_ilay[cell2]
    lay_diff = abs(ilay1-ilay2)

    ieta1 = cell_ieta[cell1]
    ieta2 = cell_ieta[cell2]
    eta_diff = abs(ieta1-ieta2)

    iphi1 = cell_iphi[cell1]
    iphi2 = cell_iphi[cell2]
    phi_diff = abs(iphi1-iphi2)

    if lay_diff > 1 or eta_diff > 2 or phi_diff > 2:
        print("Pairs are not working correctly: Lay_diff: " +str(lay_diff)+" eta_diff: "+str(eta_diff)+" phi_diff: "+str(phi_diff))

print("Test is finished")

