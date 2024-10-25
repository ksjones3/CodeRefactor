Multi-Class Classifiation Model File Order:
  
  1. pairingDatapointsForGNN.ipynb - This file uses the content of the GeneralFunctions.ipynb file to prepare and process the data from a ROOT file, which contains
information regarding 100 events. The data are converted into numpy arrays and the dimensions are checked to ensure the structure makes sense. Labels are created for
neighbors and all the information is saved as an hdf5 file. Labels for the neighbors include
      0 - Lone Lone neighbor pairs (neither cell belongs to a cluster)
      1 - True True neighbor pairs (both cells are within the same cluster)
      2 - Cluster Lone neighbor pairs (first cell is within a cluster while the second is not)
      3 - Lone Cluster neighbor pairs (first cell is not within a cluster while the second is)
      4 - Cluster Cluster neighbor pairs (each cell belongs to a different cluster)
     
  2. multiClassDataPrep.ipynb - This file creates the training and testing data to be used in the model. All data is stored in hdf5 files. The training data includes
all possible neighbors, while the testing data only concerns itself with the minimum amounts of each neighbor relation over the 100 events.
  
  3. multiCalloInAction.ipynb - The multi-class classification model is created here. Every 100 epochs of the run are saved alongside respective metrics such as the
labels, scores, and losses. This allows for one to continue where they left off if the kernel is interrupted. The model allows one to choose the number of layers that
the data will pass through the forward function.

  4. multiROCCurves.ipynb - Here the ROC curves are plotted using the one-vs-rest method. The AUC score as a function of epoch is also plotted.
