import h5py
import numpy as np
import matplotlib.pyplot as plt

#sets parameters for the code
snap='snapshot_085'
filt='WFC3-F105W'
#z=1.5
#F='F356W'
#restcolor='red'

#file
catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

#elongation data from all views for given snapshot and filter
elongation0=catalog['nonparmorphs'][snap][filt]['CAMERA0']['ELONG'].value
elongation1=catalog['nonparmorphs'][snap][filt]['CAMERA1']['ELONG'].value
elongation2=catalog['nonparmorphs'][snap][filt]['CAMERA2']['ELONG'].value
elongation3=catalog['nonparmorphs'][snap][filt]['CAMERA3']['ELONG'].value

#finds inverses of elongation
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

#adds all the data together
elongation=elong0+elong1+elong2+elong3

finalE=[]
for i in range(len(elongation)):
        if np.isnan(elongation[i])==False:
                finalE.append(elongation[i])

#print(np.median(finalE))

#randomly samples 1,000 values in finalE 1,000 times and computers std of the medians of each new sample- this is the error of the median for the full sample
medians=[]
for i in range(1000):
	sample=np.random.choice(finalE, 1000)
	#print(np.median(sample))
	medians.append(np.median(sample))
#print(len(medians))
print(np.std(medians))

