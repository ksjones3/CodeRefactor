import numpy as np
import uproot
import h5py

rootFile = uproot.open("test.root")
tree = rootFile[rootFile.keys()[0]]
branches = tree.arrays()
rootFile.close()

pairFile = h5py.File("pairData.hdf5", "r")
pairs = np.array(pairFile.get("pairData")[:])
pairFile.close()

eta = branches["cell_eta"][0]
phi = branches["cell_phi"][0]
ieta = branches["cell_ieta"][0]
iphi = branches["cell_iphi"][0]

deltaRs = []
deltaEtas = []
deltaPhis = []
counter = 0
for pair in pairs:
    cell1 = int(pair[0])
    cell2 = int(pair[1])

    eta1 = eta[cell1]
    eta2 = eta[cell2]

    ieta1 = ieta[cell1]
    ieta2 = iphi[cell2]

    phi1 = phi[cell1]
    phi2 = phi[cell2]

    iphi1 = iphi[cell1]
    iphi2 = iphi[cell2]

    deltaEta = abs(ieta1-ieta2)
    deltaPhi = abs(iphi1-iphi2)
    deltaR = np.sqrt((eta1-eta2)**2+(phi1-phi2)**2)
    
    deltaRs.append(deltaR)
    deltaEtas.append(deltaEta)
    deltaPhis.append(deltaPhi)
    print("Found DeltaR for pair "+str(counter))
    counter = counter+1

deltaRFile = h5py.File("deltaRData.hdf5", "w")
deltaRFile.create_dataset("deltaRData", data=deltaRs)
deltaRFile.create_dataset("deltaEtaData", data=deltaEtas)
deltaRFile.create_dataset("deltaPhiData", data=deltaPhis)
deltaRFile.close()
