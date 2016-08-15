import numpy as np
import h5py
import matplotlib.pyplot as plt

#this program retrieves parameters for indivdual Illustris subhalos (to then feed to GALFIT)
#it also creates arrays of parameters for the subpopulation

catalog=catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

haloID=catalog['nonparmorphs']['snapshot_085']['SubfindID'].value
#note this mag does not correspond to the zero point magnitude
mag=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['MAG'].value #magnitude
HLR=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['RHALF'].value #pixels
angle=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['ORIENT'].value #radians?
elongation=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['ELONG'].value
concentration=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['CC'].value
PSF=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['APPROXPSF_ARCSEC'].value #pixels
Pix_as=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['PIX_ARCSEC'].value #arcsecs/pixel
mass=catalog['nonparmorphs']['snapshot_085']['Mstar_Msun'].value
RP=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['RP'].value #pixels

#halo ID does not match the index so belong gets index of chosen subhalo
i=np.where(haloID==33375)
#print(i)
print(Pix_as[i])

#for the selected subpopulation
ind, ID, q_p=np.loadtxt('/Users/aquirk/Desktop/galfit/subpopulation/subpopulation.txt', unpack=True)
sub_IDs=[]
sub_q=[]
sub_mass=[]
sub_RP=[]
for i in range(len(ind)):
	sub_IDs.append(haloID[ind[i]])
	sub_q.append(1/elongation[ind[i]])
	sub_mass.append(mass[ind[i]])
	sub_RP.append(RP[ind[i]])

#median
med=np.median(q_p)

#plotting
plt.hist(q_p, 30, normed=True, label='Median={}'.format(med))
plt.xlabel('q')
plt.title('Axis Ratio for Illustris Subpopulation (from PhoUtils)')
plt.legend()
plt.savefig('/Users/aquirk/Desktop/sub_q_p.png')
