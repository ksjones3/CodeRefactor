#!/usr/bin/env python

import numpy as np
import h5py
import uproot

def canonical_form(t):
    """Return a canonical representation of a tuple."""
    return tuple(sorted(t))

def remove_permutation_variants(tuple_list):
    """Remove permutation variants from a list of tuples."""
    unique_tuples = set(canonical_form(t) for t in tuple_list)
    return [tuple(sorted(t)) for t in unique_tuples]

uprootFile = uproot.open("test.root")
tree =  uprootFile[uprootFile.keys()[0]]
branches = tree.arrays()
uprootFile.close()

cell_id = branches["cell_id"][0]
id_length = len(cell_id)

pairs = []
neighborFile = h5py.File("neighborData.hdf5", "r")
for i in range(0, id_length):
    cellNeighbors = np.array(neighborFile.get("neighborData"+str(i))[:])
    for cellNeighbor in cellNeighbors:
        pairs.append((cell_id[i], cellNeighbor))
    print("Wrote pairs for cell: "+str(i))

neighborFile.close()

pairs = remove_permutation_variants(pairs)

pairFile = h5py.File("pairData.hdf5", "w")
pairFile.create_dataset("pairData", data = pairs)
pairFile.close()
