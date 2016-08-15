import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

#sets parameters for the code
snap='snapshot_103'
z=0.5
restfilt='WFC3-F105W' #rest frame lambda that all z's share- red or blue
F='F105W'
smallfilt='WFC3-F105W' #smaller wavelength filter for color
color1='F105W'
longfilt='WFC3-F160W' #larger wavelength filter for color
color2='F160W'
restwave='730' #460 or 730
restcolor='red' #blue or red

#data file
catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

#reads in all elongation data for a give z and filter
elongation=catalog['nonparmorphs'][snap][restfilt]['CAMERA0']['ELONG'].value
elongation1=catalog['nonparmorphs'][snap][restfilt]['CAMERA1']['ELONG'].value
elongation2=catalog['nonparmorphs'][snap][restfilt]['CAMERA2']['ELONG'].value
elongation3=catalog['nonparmorphs'][snap][restfilt]['CAMERA3']['ELONG'].value

#magnitudes of smaller wavelength filter
mags=catalog['nonparmorphs'][snap][smallfilt]['CAMERA0']['MAG'].value
mags1=catalog['nonparmorphs'][snap][smallfilt]['CAMERA1']['MAG'].value
mags2=catalog['nonparmorphs'][snap][smallfilt]['CAMERA2']['MAG'].value
mags3=catalog['nonparmorphs'][snap][smallfilt]['CAMERA3']['MAG'].value

#magnitude of longer wavelength filter
magl=catalog['nonparmorphs'][snap][longfilt]['CAMERA0']['MAG'].value
magl1=catalog['nonparmorphs'][snap][longfilt]['CAMERA1']['MAG'].value
magl2=catalog['nonparmorphs'][snap][longfilt]['CAMERA2']['MAG'].value
magl3=catalog['nonparmorphs'][snap][longfilt]['CAMERA3']['MAG'].value

#below gets rid of Nan values (if the elongation OR the radius is Nan, the whole data point gets eliminated) 
#does this individually for each camera view angle
#creates an array for the color mags-magl (smaller-longer filter)
#view angle 0
E=[]
C=[] #color
for i in range(len(elongation)):
	if np.isnan(elongation[i])==False and np.isnan(mags[i])==False and np.isnan(magl[i])==False:
		E.append(1/elongation[i])
		C.append(mags[i]-magl[i])

#view angle 1
E1=[]
C1=[] #color
for i in range(len(elongation1)):
        if np.isnan(elongation1[i])==False and np.isnan(mags1[i])==False and np.isnan(magl1[i])==False:
                E1.append(1/elongation1[i])
                C1.append(mags1[i]-magl1[i])

#view angle 2
E2=[]
C2=[] #color
for i in range(len(elongation2)):
        if np.isnan(elongation2[i])==False and np.isnan(mags2[i])==False and np.isnan(magl2[i])==False:
                E2.append(1/elongation2[i])
                C2.append(mags2[i]-magl2[i])

#view angle 3
E3=[]
C3=[] #color
for i in range(len(elongation3)):
        if np.isnan(elongation3[i])==False and np.isnan(mags3[i])==False and np.isnan(magl3[i])==False:
                E3.append(1/elongation3[i])
                C3.append(mags3[i]-magl3[i])

#adds data together
X=E+E1+E2+E3
Y=C+C1+C2+C3

#testing points and lengths
print(len(E), len(E1), len(E2), len(E3))
#print(len(C), len(C1), len(C2), len(C3))
#print(len(X),len(Y))
print(E1[0], C1[0])
print(X[len(E)],Y[len(C)])

#plotting
plt.hist2d(X,Y,bins=50, norm=LogNorm())
plt.xlabel('1/Elongation')
plt.ylabel('{}-{}'.format(color1, color2))
plt.title('Rest Wavelength={}nm  z={}  ({})'.format(restwave,z,F))
plt.colorbar()
#plt.show()
plt.savefig('/Users/aquirk/Desktop/2DElongColor_{}_{}.png'.format(restcolor,z))
