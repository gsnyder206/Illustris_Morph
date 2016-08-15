import astropy
import astropy.cosmology
import h5py
import numpy as np
import matplotlib.pyplot as plt

#sets parameters
snap='snapshot_103'
filt='WFC3-F160W'
redshift=0.5
xlabel='Semi-Minor Axis' #Semi-Minor Axis or Petrosian Riadius
savelabel='Minor' #Minor or Major
#restcolor='red'

# set cosmological model, use Illustris values
ilh = 0.704
illcos = astropy.cosmology.FlatLambdaCDM(H0=70.4,Om0=0.2726,Ob0=0.0456)

# return scale in arcsec/kpc
scale = illcos.arcsec_per_kpc_proper(redshift)

#file
catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

#RP data from all views for given snapshot and filter
RP0=catalog['nonparmorphs'][snap][filt]['CAMERA0']['RP'].value
RP1=catalog['nonparmorphs'][snap][filt]['CAMERA1']['RP'].value
RP2=catalog['nonparmorphs'][snap][filt]['CAMERA2']['RP'].value
RP3=catalog['nonparmorphs'][snap][filt]['CAMERA3']['RP'].value

#Pixel size data from all views for a given snapshot and filter- doesn't change with camera or index, so adding in all three is redundant 
PIX0=catalog['nonparmorphs'][snap][filt]['CAMERA0']['PIX_ARCSEC'].value
PIX1=catalog['nonparmorphs'][snap][filt]['CAMERA1']['PIX_ARCSEC'].value
PIX2=catalog['nonparmorphs'][snap][filt]['CAMERA2']['PIX_ARCSEC'].value
PIX3=catalog['nonparmorphs'][snap][filt]['CAMERA3']['PIX_ARCSEC'].value

#Creates an array for radius size in arcsec and gets rid of NaNs
#view angle 0
radius_arcsec0=[]
for i in range(len(RP0)):
	if np.isnan(RP0[i])==False:
		radius_arcsec0.append(RP0[i]*PIX0[i])

#view angle 1
radius_arcsec1=[]
for i in range(len(RP1)):
	if np.isnan(RP1[i])==False:
		radius_arcsec1.append(RP1[i]*PIX1[i])

#view angle 2
radius_arcsec2=[]
for i in range(len(RP2)):
	if np.isnan(RP2[i])==False:
        	radius_arcsec2.append(RP2[i]*PIX2[i])

#view angle 3
radius_arcsec3=[]
for i in range(len(RP3)):
	if np.isnan(RP3[i])==False:
        	radius_arcsec3.append(RP3[i]*PIX3[i])

#adds together all view angles
radius_arcsec=radius_arcsec0+radius_arcsec1+radius_arcsec2+radius_arcsec3

#converting from arcsec to kpc
semi_major_axis=[]
for i in range(len(radius_arcsec)):
	semi_major_axis.append(radius_arcsec[i]/scale.value)

#reads in all elongation data
elongation0=catalog['nonparmorphs'][snap][filt]['CAMERA0']['ELONG'].value
elongation1=catalog['nonparmorphs'][snap][filt]['CAMERA1']['ELONG'].value
elongation2=catalog['nonparmorphs'][snap][filt]['CAMERA2']['ELONG'].value
elongation3=catalog['nonparmorphs'][snap][filt]['CAMERA3']['ELONG'].value

#finds the inverse of elongation for all camera views
elong0=[]
R0=[]
for i in range(len(elongation0)):
	if np.isnan(elongation0[i])==False and np.isnan(RP0[i])==False:
        	elong0.append(1/elongation0[i])
		R0.append(RP0[i]*PIX0[0])
elong1=[]
R1=[]
for i in range(len(elongation1)):
        if np.isnan(elongation1[i])==False and np.isnan(RP1[i])==False:
                elong1.append(1/elongation1[i])
                R1.append(RP1[i]*PIX1[0])
elong2=[]
R2=[]
for i in range(len(elongation2)):
        if np.isnan(elongation2[i])==False and np.isnan(RP2[i])==False:
                elong2.append(1/elongation2[i])
                R2.append(RP2[i]*PIX2[0])
elong3=[]
R3=[]
for i in range(len(elongation3)):
        if np.isnan(elongation3[i])==False and np.isnan(RP3[i])==False:
                elong3.append(1/elongation3[i])
                R3.append(RP3[i]*PIX3[0])

#combines all camera views
elongation=elong0+elong1+elong2+elong3
R=R0+R1+R2+R3

#calculating the semi-minor axis
#note that elongation is the inverse, so to find the minor axis, you multiply (reverse of what seems logical)
semi_minor_axis=[]
for i in range(len(R)):
	semi_minor_axis.append(R[i]*elongation[i])

#loading in PSF- same value at all angles given a redshift and a filter
PSF_arcsec=catalog['nonparmorphs'][snap][filt]['CAMERA0']['APPROXPSF_ARCSEC'].value
PSF=PSF_arcsec[0]/scale.value

#plotting
(n, bins, patches)=plt.hist(semi_minor_axis,100)
plt.plot((PSF,PSF),(0,n.max()), color='r', linestyle='--', label='PSF={}kpc'.format(PSF))
plt.plot((5*PSF,5*PSF),(0,n.max()), color='m', linestyle='--', label='5PSF'.format(PSF))
plt.xlabel('{} (kpc)'.format(xlabel))
plt.title('z={}  {}'.format(redshift,filt))
plt.legend()
#plt.show()
plt.savefig('/Users/aquirk/Desktop/{}Distrib_{}{}.png'.format(savelabel,redshift, filt))
