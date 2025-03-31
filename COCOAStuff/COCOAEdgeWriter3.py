#!/usr/bin/env python

import numpy as np
import h5py
import uproot

inputFile = uproot.open("test.root")
tree = inputFile[inputFile.keys()[0]]
branches = tree.arrays()
inputFile.close()

cell_ids = np.array(branches["cell_id"][0])
cell_ilay = np.array(branches["cell_ilay"][0])
cell_ieta = np.array(branches["cell_ieta"][0])
cell_iphi = np.array(branches["cell_iphi"][0])

maxiLayer = int(max(cell_ilay))+3
maxiEta = int(max(cell_ieta))+3
maxiPhi = int(max(cell_iphi))+3

cellGrid = np.zeros((maxiLayer, maxiEta, maxiPhi))
cellGrid[:][:][:] = -1

cellIdLength = len(cell_ids)

for i in range(0, cellIdLength):
    cell_id = cell_ids[i]
    cell_layer_index = int(cell_ilay[i])
    cell_eta_index = int(cell_ieta[i])
    cell_phi_index = int(cell_iphi[i])

    cellGrid[cell_layer_index][cell_eta_index][cell_phi_index] = cell_id

neighbors = []


for i in range(0, cellIdLength):
    cell_id = cell_ids[i]
    cell_layer_index = int(cell_ilay[i])
    cell_eta_index = int(cell_ieta[i])
    cell_phi_index = int(cell_iphi[i])

    cell_neighbors = []

    for j in range(-1, 2):
        for k in range(-2, 3):
            for n in range(-2, 3):
                neighbor_layer_index = cell_layer_index+j
                neighbor_eta_index = cell_eta_index+k
                neighbor_phi_index = cell_phi_index+n
                if neighbor_layer_index >= 0 and neighbor_eta_index >= 0 and neighbor_phi_index >= 0:
                    if j != 0 or k != 0 or n != 0:
                        cell_neighbor = cellGrid[neighbor_layer_index][neighbor_eta_index][neighbor_phi_index]
                        if cell_neighbor >= 0:
                            cell_neighbors.append(cell_neighbor)
    neighbors.append(cell_neighbors)
    print("Found neighbors for cell "+str(cell_id))

outputFile = h5py.File("neighborData.h5py", "w")
for i in range(0, len(neighbors)):
    outputFile.create_dataset("neighborData"+str(i), data=neighbors[i])
outputFile.close()
print("Wrote out to file neighborData.hdf5")
