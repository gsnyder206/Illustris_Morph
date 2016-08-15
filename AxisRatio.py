import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
from pylab import *

#sets parameters for the code
snap='snapshot_075'
filt='NC-F115W'
z=1.5
F='F115W'
restcolor='blue'

#file
catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

#elongation data from all views for given snapshot and filter
elongation0=catalog['nonparmorphs'][snap][filt]['CAMERA0']['ELONG'].value
elongation1=catalog['nonparmorphs'][snap][filt]['CAMERA1']['ELONG'].value
elongation2=catalog['nonparmorphs'][snap][filt]['CAMERA2']['ELONG'].value
elongation3=catalog['nonparmorphs'][snap][filt]['CAMERA3']['ELONG'].value

elong0=[]
for i in range(len(elongation0)):
	elong0.append(1/elongation0[i])
elong1=[]
for i in range(len(elongation1)):
	elong1.append(1/elongation1[i])
elong2=[]
for i in range(len(elongation2)):
	elong2.append(1/elongation2[i])
elong3=[]
for i in range(len(elongation3)):
	elong3.append(1/elongation3[i])

elongation=elong0+elong1+elong2+elong3
print(len(elongation0), len(elongation1), len(elongation2), len(elongation3))
print(len(elongation))

finalE=[]
for i in range(len(elongation)):
	if np.isnan(elongation[i])==False:
		finalE.append(elongation[i])

#median of inverse of elongation
m=np.nanmedian(finalE) 
print(m)

#plotting
#rc('axes', linewidth=2)
#rcParams['xtick.major.size']=8
#rcParams['xtick.major.width']=2
#rcParams['xtick.minor.size']=4
#rcParams['xtick.minor.width']=2
#rcParams['ytick.major.size']=8
#rcParams['ytick.major.width']=2
#rcParams['ytick.minor.size']=4
#rcParams['ytick.minor.width']=2
plt.hist(finalE, 50, (0,1), color='g', alpha=.5, normed=True,label='median={}'.format(m))
plt.xlabel('1/e', fontsize=15)
plt.title('Projected Axis Ratio z={} ({})'.format(z,filt))
plt.legend(loc=2)
#plt.show()
plt.savefig('/Users/aquirk/Desktop/axisratio{}z{}.png'.format(restcolor,z))
