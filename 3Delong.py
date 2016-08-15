import astropy
import astropy.cosmology
import h5py
import numpy as np
import matplotlib.pyplot as plt

#sets parameters
snap='snapshot_103'
filt='WFC3-F105W'
redshift=0.5
cut=3
label='SMiA' #RP or SMiA
restcolor='red'
restwave=730 #460 or 730

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

#reads in all elongation data
elongation0=catalog['nonparmorphs'][snap][filt]['CAMERA0']['ELONG'].value
elongation1=catalog['nonparmorphs'][snap][filt]['CAMERA1']['ELONG'].value
elongation2=catalog['nonparmorphs'][snap][filt]['CAMERA2']['ELONG'].value
elongation3=catalog['nonparmorphs'][snap][filt]['CAMERA3']['ELONG'].value

#mass data
Mass=catalog['nonparmorphs'][snap]['Mstar_Msun']

#Creates an array for radius size in arcsec and one for INVERSES of elongation and gets rid of NaNs
#view angle 0
radius_arcsec0=[]
elong0=[]
mass0=[]
for i in range(len(RP0)):
        if np.isnan(RP0[i])==False and np.isnan(Mass[i])==False and np.isnan(elongation0[i])==False:
                radius_arcsec0.append(RP0[i]*PIX0[i])
                elong0.append(1/elongation0[i])
		mass0.append(Mass[i])

#view angle 1
radius_arcsec1=[]
elong1=[]
mass1=[]
for i in range(len(RP1)):
        if np.isnan(RP1[i])==False and np.isnan(Mass[i])==False and np.isnan(elongation1[i])==False:
                radius_arcsec1.append(RP1[i]*PIX1[i])
                elong1.append(1/elongation1[i])
		mass1.append(Mass[i])

#view angle 2
radius_arcsec2=[]
elong2=[]
mass2=[]
for i in range(len(RP2)):
        if np.isnan(RP2[i])==False and np.isnan(Mass[i])==False and np.isnan(elongation2[i])==False:
                radius_arcsec2.append(RP2[i]*PIX2[i])
                elong2.append(1/elongation2[i])
		mass2.append(Mass[i])

#view angle 3
radius_arcsec3=[]
elong3=[]
mass3=[]
for i in range(len(RP3)):
        if np.isnan(RP3[i])==False and np.isnan(Mass[i])==False and np.isnan(elongation3[i])==False:
                radius_arcsec3.append(RP3[i]*PIX3[i])
                elong3.append(1/elongation3[i])
		mass3.append(Mass[i])

#adds together all view angles
radius_arcsec=radius_arcsec0+radius_arcsec1+radius_arcsec2+radius_arcsec3
elongation=elong0+elong1+elong2+elong3
mass=mass0+mass1+mass2+mass3

#print(len(elongation), len(radius_arcsec), len(mass))

#converting from arcsec to kpc
semi_major_axis=[]
for i in range(len(radius_arcsec)):
        semi_major_axis.append(radius_arcsec[i]/scale.value)

#calculating the semi-minor axis
#note that elongation is the inverse, so to find the minor axis, you multiply (reverse of what seems logical)
semi_minor_axis=[]
for i in range(len(semi_major_axis)):
        semi_minor_axis.append(semi_major_axis[i]*elongation[i])

#loading in PSF- same value at all angles given a redshift and a filter
PSF_arcsec=catalog['nonparmorphs'][snap][filt]['CAMERA0']['APPROXPSF_ARCSEC'].value
PSF=PSF_arcsec[0]/scale.value

plt.scatter(mass, semi_major_axis, c=elongation)
plt.colorbar()
plt.show()
