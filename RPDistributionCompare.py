import astropy
import astropy.cosmology
import h5py
import numpy as np
import matplotlib.pyplot as plt

#sets parameters
snap='snapshot_103'
filt1='WFC3-F160W'
filt2='NC-F150W'
redshift=0.5
#CHANGE HISTOGRAM PLOTTING COMMAND
xlabel='Semi-Minor Axis' #Semi-Minor Axis or Petrosian Radius
savelabel='Minor' #Minor or Major

# set cosmological model, use Illustris values
ilh = 0.704
illcos = astropy.cosmology.FlatLambdaCDM(H0=70.4,Om0=0.2726,Ob0=0.0456)

# return scale in arcsec/kpc
scale = illcos.arcsec_per_kpc_proper(redshift)

#file
catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

#DATA FOR FIRST FILTER
#RP data from all views for given snapshot and filter
RPW0=catalog['nonparmorphs'][snap][filt1]['CAMERA0']['RP'].value
RPW1=catalog['nonparmorphs'][snap][filt1]['CAMERA1']['RP'].value
RPW2=catalog['nonparmorphs'][snap][filt1]['CAMERA2']['RP'].value
RPW3=catalog['nonparmorphs'][snap][filt1]['CAMERA3']['RP'].value

#Pixel size data from all views for a given snapshot and filter- doesn't change with camera or index, so adding in all three is redundant 
PIXW0=catalog['nonparmorphs'][snap][filt1]['CAMERA0']['PIX_ARCSEC'].value
PIXW1=catalog['nonparmorphs'][snap][filt1]['CAMERA1']['PIX_ARCSEC'].value
PIXW2=catalog['nonparmorphs'][snap][filt1]['CAMERA2']['PIX_ARCSEC'].value
PIXW3=catalog['nonparmorphs'][snap][filt1]['CAMERA3']['PIX_ARCSEC'].value

#reads in all elongation data
elongationW0=catalog['nonparmorphs'][snap][filt1]['CAMERA0']['ELONG'].value
elongationW1=catalog['nonparmorphs'][snap][filt1]['CAMERA1']['ELONG'].value
elongationW2=catalog['nonparmorphs'][snap][filt1]['CAMERA2']['ELONG'].value
elongationW3=catalog['nonparmorphs'][snap][filt1]['CAMERA3']['ELONG'].value

#Creates an array for radius size in arcsec and one for INVERSES of elongation and gets rid of NaNs
#view angle 0
radius_arcsecW0=[]
elongW0=[]
for i in range(len(RPW0)):
        if np.isnan(RPW0[i])==False and np.isnan(elongationW0[i])==False:
                radius_arcsecW0.append(RPW0[i]*PIXW0[i])
                elongW0.append(1/elongationW0[i])

#view angle 1
radius_arcsecW1=[]
elongW1=[]
for i in range(len(RPW1)):
        if np.isnan(RPW1[i])==False and np.isnan(elongationW1[i])==False:
                radius_arcsecW1.append(RPW1[i]*PIXW1[i])
                elongW1.append(1/elongationW1[i])

#view angle 2
radius_arcsecW2=[]
elongW2=[]
for i in range(len(RPW2)):
        if np.isnan(RPW2[i])==False and np.isnan(elongationW2[i])==False:
                radius_arcsecW2.append(RPW2[i]*PIXW2[i])
                elongW2.append(1/elongationW2[i])

#view angle 3
radius_arcsecW3=[]
elongW3=[]
for i in range(len(RPW3)):
        if np.isnan(RPW3[i])==False and np.isnan(elongationW3[i])==False:
                radius_arcsecW3.append(RPW3[i]*PIXW3[i])
                elongW3.append(1/elongationW3[i])

#adds together all view angles
radius_arcsecW=radius_arcsecW0+radius_arcsecW1+radius_arcsecW2+radius_arcsecW3
elongationW=elongW0+elongW1+elongW2+elongW3

#converting from arcsec to kpc
semi_major_axisW=[]
for i in range(len(radius_arcsecW)):
        semi_major_axisW.append(radius_arcsecW[i]/scale.value)

#calculating the semi-minor axis
#note that elongation is the inverse, so to find the minor axis, you multiply (reverse of what seems logical)
semi_minor_axisW=[]
for i in range(len(semi_major_axisW)):
        semi_minor_axisW.append(semi_major_axisW[i]*elongationW[i])

#DATA FOR SECOND FILTER
#RP data from all views for given snapshot and filter
RPN0=catalog['nonparmorphs'][snap][filt2]['CAMERA0']['RP'].value
RPN1=catalog['nonparmorphs'][snap][filt2]['CAMERA1']['RP'].value
RPN2=catalog['nonparmorphs'][snap][filt2]['CAMERA2']['RP'].value
RPN3=catalog['nonparmorphs'][snap][filt2]['CAMERA3']['RP'].value

#Pixel size data from all views for a given snapshot and filter- doesn't change with camera or index, so adding in all three is redundant 
PIXN0=catalog['nonparmorphs'][snap][filt2]['CAMERA0']['PIX_ARCSEC'].value
PIXN1=catalog['nonparmorphs'][snap][filt2]['CAMERA1']['PIX_ARCSEC'].value
PIXN2=catalog['nonparmorphs'][snap][filt2]['CAMERA2']['PIX_ARCSEC'].value
PIXN3=catalog['nonparmorphs'][snap][filt2]['CAMERA3']['PIX_ARCSEC'].value

#reads in all elongation data
elongationN0=catalog['nonparmorphs'][snap][filt2]['CAMERA0']['ELONG'].value
elongationN1=catalog['nonparmorphs'][snap][filt2]['CAMERA1']['ELONG'].value
elongationN2=catalog['nonparmorphs'][snap][filt2]['CAMERA2']['ELONG'].value
elongationN3=catalog['nonparmorphs'][snap][filt2]['CAMERA3']['ELONG'].value

#Creates an array for radius size in arcsec and one for INVERSES of elongation and gets rid of NaNs
#view angle 0
radius_arcsecN0=[]
elongN0=[]
for i in range(len(RPN0)):
        if np.isnan(RPN0[i])==False and np.isnan(elongationN0[i])==False:
                radius_arcsecN0.append(RPN0[i]*PIXN0[i])
                elongN0.append(1/elongationN0[i])

#view angle 1
radius_arcsecN1=[]
elongN1=[]
for i in range(len(RPN1)):
        if np.isnan(RPN1[i])==False and np.isnan(elongationN1[i])==False:
                radius_arcsecN1.append(RPN1[i]*PIXN1[i])
                elongN1.append(1/elongationN1[i])

#view angle 2
radius_arcsecN2=[]
elongN2=[]
for i in range(len(RPN2)):
        if np.isnan(RPN2[i])==False and np.isnan(elongationN2[i])==False:
                radius_arcsecN2.append(RPN2[i]*PIXN2[i])
                elongN2.append(1/elongationN2[i])

#view angle 3
radius_arcsecN3=[]
elongN3=[]
for i in range(len(RPN3)):
        if np.isnan(RPN3[i])==False and np.isnan(elongationN3[i])==False:
                radius_arcsecN3.append(RPN3[i]*PIXN3[i])
                elongN3.append(1/elongationN3[i])

#adds together all view angles
radius_arcsecN=radius_arcsecN0+radius_arcsecN1+radius_arcsecN2+radius_arcsecN3
elongationN=elongN0+elongN1+elongN2+elongN3

#converting from arcsec to kpc
semi_major_axisN=[]
for i in range(len(radius_arcsecN)):
        semi_major_axisN.append(radius_arcsecN[i]/scale.value)

#calculating the semi-minor axis
#note that elongation is the inverse, so to find the minor axis, you multiply (reverse of what seems logical)
semi_minor_axisN=[]
for i in range(len(semi_major_axisN)):
        semi_minor_axisN.append(semi_major_axisN[i]*elongationN[i])

#loading in PSF- same value at all angles given a redshift and a filter
PSF_arcsecW=catalog['nonparmorphs'][snap][filt1]['CAMERA0']['APPROXPSF_ARCSEC'].value
PSFW=PSF_arcsecW[0]/scale.value

PSF_arcsecN=catalog['nonparmorphs'][snap][filt2]['CAMERA0']['APPROXPSF_ARCSEC'].value
PSFN=PSF_arcsecN[0]/scale.value

#plotting
(W, bins, patches)=plt.hist(semi_minor_axisW, 100, alpha=.5, color='b', label='{}'.format(filt1))
(N, bins, patches)=plt.hist(semi_minor_axisN,100, alpha=.4, color='r', label='{}'.format(filt2))
plt.plot((PSFW,PSFW),(0,W.max()), color='k', linestyle='-', linewidth=2,label='WFC3 PSF={}kpc'.format(PSFW))
plt.plot((5*PSFW,5*PSFW),(0,W.max()), color='k', linestyle='--', linewidth=2,label='5PSF'.format(PSFW))
plt.plot((PSFN,PSFN),(0,N.max()), color='g', linestyle='-', linewidth=2,label='NC PSF={}kpc'.format(PSFN))
plt.plot((5*PSFN,5*PSFN),(0,N.max()), color='g', linestyle='--', linewidth=2,label='5PSF'.format(PSFN))
plt.title('z={}'.format(redshift))
plt.xlabel('{} kpc'.format(xlabel))
plt.legend()
#plt.show()
plt.savefig('/Users/aquirk/Desktop/RPCompare{}{}.png'.format(savelabel,redshift))
