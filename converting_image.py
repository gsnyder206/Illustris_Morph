from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

#this reads in an origial fits image and saves it as another fits file with the correct units for GALFIT. it also addes exposure time to the new file's header

#loads sub halo IDs
shID=np.loadtxt('/Users/aquirk/Desktop/galfit/subpopulation/subpopulation.txt', usecols=(0,), unpack=True)

#below is a loop to create a converted image for all halos in the subpopulation
for i in range(len(shID)):
	hdulist=fits.open('/Users/aquirk/Desktop/galfit/subpopulation/red/original_images/{0:g}.fits'.format(shID[i])) #the 0:g truncates the .0 at the end of the ID

	#below will convert ADU to counts and will create the exposure time
	image=hdulist[0].data #image units
	skysig=hdulist[0].header['SKYSIG'] #image units
	photfnu=hdulist[0].header['PHOTFNU'] #image units
	pix_as=hdulist[0].header['PIXSCALE'] #arc seconds
	skysig_Jy= (((skysig)*((pix_as)**2))/(10**6))
	skysig_cts= ((skysig_Jy)/(photfnu))
	exptime_sec =((skysig_cts)**(-2))
	image_cts= ((image*(pix_as**2))/(photfnu*(10**6)))
	image_count= ((image_cts)*(exptime_sec)) #GALFIT ideal unit- counts

	#creating new fits file with ADU unit counts
	hdu=fits.PrimaryHDU(image_count)
	hdulist=fits.HDUList([hdu])
	#adds exposure time to header- note that this new file loses most of the original file's header-- this seems fine for GALFIT
	hdulist[0].header['EXPTIME']=(exptime_sec)

	#saves new file
	hdulist.writeto('/Users/aquirk/Desktop/galfit/subpopulation/red/converted_{0:g}.fits'.format(shID[i]))
