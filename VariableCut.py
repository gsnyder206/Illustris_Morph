import h5py
import numpy as np
import matplotlib.pyplot as plt

#sets parameters for the code
snap='snapshot_103'
z=0.5
filt='WFC3-F105W'
cut=30
restwave=730 #730 or 460
restcolor='red' #red or blue
parameter='SNPIX'
label='Sount to Noise Ratio'

#file
catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

#reads in all elongation values for given filter and snapshot
elongation0=catalog['nonparmorphs'][snap][filt]['CAMERA0']['ELONG'].value
elongation1=catalog['nonparmorphs'][snap][filt]['CAMERA1']['ELONG'].value
elongation2=catalog['nonparmorphs'][snap][filt]['CAMERA2']['ELONG'].value
elongation3=catalog['nonparmorphs'][snap][filt]['CAMERA3']['ELONG'].value

#reads in all variable values for given filter and snapshot
variable0=catalog['nonparmorphs'][snap][filt]['CAMERA0'][parameter].value
variable1=catalog['nonparmorphs'][snap][filt]['CAMERA1'][parameter].value
variable2=catalog['nonparmorphs'][snap][filt]['CAMERA2'][parameter].value
variable3=catalog['nonparmorphs'][snap][filt]['CAMERA3'][parameter].value

#sets variable cut
#adds the inverse of elongation into array
elongation=[]
#view angle 0
for i in range(len(variable0)):
	if cut<variable0[i]:
		elongation.append(1/elongation0[i])
#view angle 1
for i in range(len(variable1)):
        if cut<variable1[i]:
                elongation.append(1/elongation1[i])
#view angle 2
for i in range(len(variable2)):
        if cut<variable2[i]:
                elongation.append(1/elongation2[i])
#view angle 3
for i in range(len(variable3)):
        if cut<variable3[i]:
                elongation.append(1/elongation3[i])

#print(len(elongation0), len(elongation1), len(elongation2), len(elongation3), len(elongation))

#gets rid of NaNs
finalE=[]
for i in range(len(elongation)):
	if np.isnan(elongation[i])==False:
		finalE.append(elongation[i])

#median of distribution
med=np.nanmedian(finalE)
print(med)

#plotting
plt.hist(finalE,100,(0,1), label='Median={}, {}>{}'.format(med,label,cut))
plt.xlabel('1/elongation')
plt.title('z={} Rest Wavelength={}nm ({})'.format(z,restwave,filt))
plt.legend(loc=2)
plt.savefig('/Users/aquirk/Desktop/{}_{}_{}_{}.png'.format(parameter,cut,restcolor,z))
