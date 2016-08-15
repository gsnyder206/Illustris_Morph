import numpy as np
import h5py
import matplotlib.pyplot as plt

#this program RANDOMLY selects subhalos from a given redshift and filter and camera 0 to create a subpopulation to compare axis ratios to GALFIT

#file
catalog=catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

#loads in parameters
haloID=catalog['nonparmorphs']['snapshot_085']['SubfindID'].value
mass=catalog['nonparmorphs']['snapshot_085']['Mstar_Msun'].value
PSF=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['APPROXPSF_ARCSEC'].value #pixels
Pix_as=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['PIX_ARCSEC'].value #arcsecs/pixel
elongation=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['ELONG'].value
RP=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['RP'].value #pixels

subhalos=np.random.choice(haloID, 99, replace=False)
#print((subhalos))

indices=[]
for i in range(len(subhalos)):
	n=np.where(haloID==subhalos[i])
	indices.append(n)
#print(indices)
