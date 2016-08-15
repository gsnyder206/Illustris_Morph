import astropy
import astropy.cosmology
import h5py
import numpy as np
import matplotlib.pyplot as plt

#sets parameters
snap='snapshot_085'
filt='WFC3-F105W'
redshift=1
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

#calculating the semi-minor axis
#note that elongation is the inverse, so to find the minor axis, you multiply (reverse of what seems logical)
semi_minor_axis=[]
for i in range(len(semi_major_axis)):
        semi_minor_axis.append(semi_major_axis[i]*elongation[i])

#loading in PSF- same value at all angles given a redshift and a filter
PSF_arcsec=catalog['nonparmorphs'][snap][filt]['CAMERA0']['APPROXPSF_ARCSEC'].value
PSF=PSF_arcsec[0]/scale.value

#print(len(elongation), len(semi_major_axis), len(semi_minor_axis))

#creating the radius limit
#change to RP or SmA
elongation_cut=[]
for i in range(len(elongation)):
	if (cut*PSF)<semi_minor_axis[i]:
		elongation_cut.append(elongation[i])

#median
med=np.median(elongation_cut)
#print(med)

#print(len(elongation))
#print(len(elongation_cut))

#randomly samples 1,000 values in finalE 1,000 times and computers std of the medians of each new sample- this is the error of the median for the full sample
medians=[]
for i in range(1000):
        sample=np.random.choice(elongation_cut, 1000)
        medians.append(np.median(sample))
print(np.std(medians))

#plotting
#plt.hist(elongation,50,(0,1), normed=True,alpha=.5, label='No Cut')
#plt.hist(elongation_cut,50, (0,1), normed=True, alpha=.5, color='r', label='{}<{}*PSF, PSF={}, med={}'.format(label,cut, PSF,med))
#plt.title('R Wavelength={}nm  z={}  {}'.format(restwave,redshift, filt)) 
#plt.xlabel('1/Elongation')
#plt.legend(loc=2)
#plt.show()
#plt.savefig('/Users/aquirk/Desktop/L.{}_{}_{}{}.png'.format(label,cut,redshift,restcolor))
