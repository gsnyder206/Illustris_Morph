import numpy as np
import h5py

#this scripts lists all of a parameter value for the subpopulation given a filter, snap, and camera

shID=np.loadtxt('/Users/aquirk/Desktop/galfit/subpopulation/subpopulation.txt', usecols=(0,), unpack=True)

camera='CAMERA0'
snapshot='snapshot_085'
filt='NC-F277W'

catalog=catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

haloID=catalog['nonparmorphs'][snapshot]['SubfindID'].value
elongation=catalog['nonparmorphs'][snapshot][filt][camera]['ELONG'].value

for i in range(len(shID)):
	print(1/elongation[np.where(haloID==shID[i])])
