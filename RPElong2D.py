import astropy
import astropy.cosmology
import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

#sets parameters
snap='snapshot_085'
filt='NC-F115W'
redshift=1
#CHANGE PLOTTING COMMAND FOR Y
ylabel='Semi-Minor Axis' #Petrosian Radius or Semi-Minor Axis
savelabel='SmA' #RP or SMA
restcolor='blue'
restwave=460 #460 or 730

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

#Creates an array for radius size in arcsec and one for INVERSES of elongation and gets rid of NaNs
#view angle 0
radius_arcsec0=[]
elong0=[]
for i in range(len(RP0)):
        if np.isnan(RP0[i])==False and np.isnan(elongation0[i])==False:
                radius_arcsec0.append(RP0[i]*PIX0[i])
		elong0.append(1/elongation0[i])

#view angle 1
radius_arcsec1=[]
elong1=[]
for i in range(len(RP1)):
        if np.isnan(RP1[i])==False and np.isnan(elongation1[i])==False:
                radius_arcsec1.append(RP1[i]*PIX1[i])
                elong1.append(1/elongation1[i])

#view angle 2
radius_arcsec2=[]
elong2=[]
for i in range(len(RP2)):
        if np.isnan(RP2[i])==False and np.isnan(elongation2[i])==False:
                radius_arcsec2.append(RP2[i]*PIX2[i])
                elong2.append(1/elongation2[i])

#view angle 3
radius_arcsec3=[]
elong3=[]
for i in range(len(RP3)):
        if np.isnan(RP3[i])==False and np.isnan(elongation3[i])==False:
                radius_arcsec3.append(RP3[i]*PIX3[i])
                elong3.append(1/elongation3[i])

#adds together all view angles
radius_arcsec=radius_arcsec0+radius_arcsec1+radius_arcsec2+radius_arcsec3
elongation=elong0+elong1+elong2+elong3

#converting from arcsec to kpc
semi_major_axis=[]
for i in range(len(radius_arcsec)):
        semi_major_axis.append(radius_arcsec[i]/scale.value)

#testing lengths and points
#print(len(elongation0), len(elongation1), len(elongation2), len(elongation3))
#print(len(RP0), len(RP1), len(RP2), len(RP3))
#print(len(elong0), len(elong1), len(elong2), len(elong3))
#print(len(radius_arcsec0), len(radius_arcsec1), len(radius_arcsec2), len(radius_arcsec3))
#print(len(radius_arcsec))
#print(len(elongation))
#print(len(semi_major_axis))
#print(elong1[0], radius_arcsec1[0])
#print(elongation[len(elong0)], radius_arcsec[len(radius_arcsec0)])

#calculating the semi-minor axis
#note that elongation is the inverse, so to find the minor axis, you multiply (reverse of what seems logical)
semi_minor_axis=[]
for i in range(len(semi_major_axis)):
	semi_minor_axis.append(semi_major_axis[i]*elongation[i])

#print(semi_major_axis[0],elongation[0],semi_minor_axis[0])

#plotting 2D histogram
plt.hist2d(elongation, semi_minor_axis, bins=50, norm=LogNorm())
plt.xlabel('1/Elongation')
plt.ylabel('{} kpc'.format(ylabel))
plt.yscale('log')
plt.title('Rest Wavelength={}nm  z={}  {}'.format(restwave,redshift, filt))
plt.colorbar()
#plt.show()
plt.savefig('/Users/aquirk/Desktop/{}Elong_{}{}_{}.png'.format(savelabel,filt,redshift, restcolor))
