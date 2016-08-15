import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

#sets parameters for the code
snap='snapshot_103'
z=0.5
restfilt='WFC3-F105W' #rest frame lambda that all z's share- red or blue
F='F105W'
restwave='730' #460 or 730
restcolor='red' #blue or red
parameter='SNPIX' #any paramter from the list CHECK SCALES AND LIMITS BELOW 
ylabel='Sound to Noise Ratio'

#data file
catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

#reads in all elongation data for a given z and filter
elongation=catalog['nonparmorphs'][snap][restfilt]['CAMERA0']['ELONG'].value
elongation1=catalog['nonparmorphs'][snap][restfilt]['CAMERA1']['ELONG'].value
elongation2=catalog['nonparmorphs'][snap][restfilt]['CAMERA2']['ELONG'].value
elongation3=catalog['nonparmorphs'][snap][restfilt]['CAMERA3']['ELONG'].value

#reads in all parameter data for a given z and filter
variable=catalog['nonparmorphs'][snap][restfilt]['CAMERA0'][parameter].value
variable1=catalog['nonparmorphs'][snap][restfilt]['CAMERA1'][parameter].value
variable2=catalog['nonparmorphs'][snap][restfilt]['CAMERA2'][parameter].value
variable3=catalog['nonparmorphs'][snap][restfilt]['CAMERA3'][parameter].value

#below gets rid of Nan values (if the elongation OR the radius is Nan, the whole data point gets eliminated) 
#does this individually for each camera view angle
#view angle 0
E=[]
V=[]
for i in range(len(elongation)):
	if np.isnan(elongation[i])==False and np.isnan(variable[i])==False:
		E.append(1/elongation[i])
		V.append(variable[i])
#view angle 1
E1=[]
V1=[]
for i in range(len(elongation1)):
        if np.isnan(elongation1[i])==False and np.isnan(variable1[i])==False:
                E1.append(1/elongation1[i])
                V1.append(variable1[i])

#view angle 2
E2=[]
V2=[]
for i in range(len(elongation2)):
        if np.isnan(elongation2[i])==False and np.isnan(variable2[i])==False:
                E2.append(1/elongation2[i])
                V2.append(variable2[i])

#view angle 3
E3=[]
V3=[]
for i in range(len(elongation3)):
        if np.isnan(elongation3[i])==False and np.isnan(variable3[i])==False:
                E3.append(1/elongation3[i])
                V3.append(variable3[i])

#adding the data together
X=E+E1+E2+E3
Y=V+V1+V2+V3

#testing points and lengths
print(len(E), len(E1), len(E2), len(E3))
#print(len(V), len(V1), len(V2), len(V3))
#print(len(X), len(Y))
print(E1[0], V1[0])
print(X[len(E)], Y[len(V)])

#plotting
plt.hist2d(X,Y, bins=50, norm=LogNorm())
plt.xlabel('1/Elongation')
#plt.xscale('log')
plt.ylabel('{}'.format(ylabel))
#plt.gca().invert_yaxis()
plt.yscale('log')
plt.ylim(.1,100)
plt.title('Rest Wavelengh={}nm  z={}  ({})'.format(restwave,z,F))
plt.colorbar()
#plt.show()
plt.savefig('/Users/aquirk/Desktop/2DElong{}_{}_{}.png'.format(parameter,restcolor,z))
