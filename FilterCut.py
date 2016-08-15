import h5py
import numpy as np
import matplotlib.pyplot as plt

#sets parameters for the code
snap='snapshot_103'
#z=0.5
filt='WFC3-F105W'
cut1=10**10.5
cut2=50
figlabel='Comp'
restwave=730 #730 or 460
restcolor='red' #red or blue
parameter1='Mstar_Msun'
label='Mass'
parameter2='SFR_Msunperyr'

#file
catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

#reads in all elongation values for given filter and snapshot
elongation_0=catalog['nonparmorphs'][snap][filt]['CAMERA0']['ELONG']
elongation_1=catalog['nonparmorphs'][snap][filt]['CAMERA1']['ELONG']
elongation_2=catalog['nonparmorphs'][snap][filt]['CAMERA2']['ELONG']
elongation_3=catalog['nonparmorphs'][snap][filt]['CAMERA3']['ELONG']

#reads in variable for given snapshot
variable1=catalog['nonparmorphs'][snap][parameter1].value

#reads in variable for given snapshot
variable2=catalog['nonparmorphs'][snap][parameter2].value

#sets variable cut
elongation1=[] #data that passes the cut gets added- INVERSES of elongation
for i in range(len(variable1)):
	if cut1<variable1[i] and cut2<variable2[i]:
		elongation1.append(1/elongation_0.value[i])
		elongation1.append(1/elongation_1.value[i])
		elongation1.append(1/elongation_2.value[i])
		elongation1.append(1/elongation_3.value[i])

#elongation2=[] #data that passes the cut gets added- INVERSES of elongation
#for i in range(len(variable)):
#        if cut2<variable[i]:
#                elongation2.append(1/elongation_0.value[i])
#                elongation2.append(1/elongation_1.value[i])
#                elongation2.append(1/elongation_2.value[i])
#                elongation2.append(1/elongation_3.value[i])

#gets rid of NaNs
elong1=[]
for i in range(len(elongation1)):
	if np.isnan(elongation1[i])==False:
		elong1.append(elongation1[i])

#elong2=[]
#for i in range(len(elongation2)):
#        if np.isnan(elongation2[i])==False:
#                elong2.append(elongation2[i])

#median
med1=np.median(elong1)
#print(med1)
#med2=np.median(elong2)

#bootstrap method of finding the error of the median
medians1=[]
for i in range(1000):
        sample=np.random.choice(elong1, 1000)
        medians1.append(np.median(sample))
print(np.std(medians1))

#medians2=[]
#for i in range(1000):
#        sample=np.random.choice(elong2, 1000)
#        medians2.append(np.median(sample))
#print(np.std(medians2))

#plotting 
#plt.hist(elong1, 50, (0,1), alpha=.5, normed=True,color='b',label='{:.2e}<Mass<{:.2e}'.format(cut1,cut2))#label='Median={}, {}>{}'.format(med,label,cut))
#plt.hist(elong2, 50, (0,1), alpha=.5, normed=True, color='r',label='Mass>{:.2e}'.format(cut2))
#plt.xlabel('1/elongation')
#plt.title('z={} Rest Wavelength={}nm ({})'.format(z,restwave,filt))
#plt.legend(loc=2)
#plt.savefig('/Users/aquirk/Desktop/{}_{}_{}_{}.png'.format(parameter,figlabel,restcolor,z))
