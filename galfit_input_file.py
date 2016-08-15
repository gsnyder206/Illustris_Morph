import numpy as np
import h5py 
from astropy.io import fits

#get to run this in a loop once it works for one galaxy-- change saving name and location

#sets conditions for the loop-- this makes it completely customizeable
#HAVE TO CHANGE PSF IMAGE BY HAND IN D
camera='CAMERA0'
snapshot='snapshot_085'
filt='NC-F277W'

#loads image file and data for a given camera, snapshot, and filter
catalog=catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")
haloID=catalog['nonparmorphs'][snapshot]['SubfindID'].value
HLR=catalog['nonparmorphs'][snapshot][filt][camera]['RHALF'].value #pixels
angle=catalog['nonparmorphs'][snapshot][filt][camera]['ORIENT'].value #radians?
elongation=catalog['nonparmorphs'][snapshot][filt][camera]['ELONG'].value
concentration=catalog['nonparmorphs'][snapshot][filt][camera]['CC'].value
Pix_as=catalog['nonparmorphs'][snapshot][filt][camera]['PIX_ARCSEC'].value #arcsecs/pixel
mag=catalog['nonparmorphs'][snapshot][filt][camera]['MAG'].value #magnitude

#these are parameters needed for GALFIT and will be filled into the input file below
#loads halo IDS
shID=np.loadtxt('/Users/aquirk/Desktop/galfit/subpopulation/subpopulation.txt', usecols=(0,), unpack=True)

#creates a loop to create an input file per sub halo
for i in range(len(shID)):
	n=np.where(haloID==shID[i])
	K=Pix_as[n] 
	three=mag[n]
	four=HLR[n]
	five=concentration[n]
	nine=(1/elongation[n])
	ten=angle[n] #maybe convert this to radians 

	hdulist=fits.open('/Users/aquirk/Desktop/galfit/subpopulation/red/converted_{0:g}.fits'.format(shID[i]))
	xsize=hdulist[0].header['NAXIS1']
	ysize=hdulist[0].header['NAXIS2']
	xcenter=xsize/2 #i'm not sure this is the best way to do the center
	ycenter=ysize/2

	hdulist=fits.open('/Users/aquirk/Desktop/galfit/subpopulation/red/original_images/{0:g}.fits'.format(shID[i]))
	zero_point=hdulist[0].header['ABZP']

	#creates an input file for galfit to run-- creates a customized one per galaxy
	file=open('/Users/aquirk/Desktop/galfit/subpopulation/red/{0:g}_input.txt'.format(shID[i]), 'w')
	file.write('A) converted_{0:g}.fits #input file \n'.format(shID[i]))
	file.write('B) galfit_{0:g}.fits #output file \n'.format(shID[i]))
	file.write('C) none #sigma image name \n') 
	file.write('D) F105W_rebin.fits #input PSF image \n') #this will need to be changed if the snap and filter change
	file.write('E) 1 #PSF fine sampling factor relative to data \n')
	file.write('F) none #bad pixel mask \n')
	file.write('G) none #file with parameter constraints \n')
	file.write('H) 1 {} 1 {} #image region to fit\n'.format(xsize, ysize)) 
	file.write('I) {} {} #size of the convolution box (x,y) \n'.format(xsize, ysize)) 
	file.write('J) {} #magnitude photometric zeropoint \n'.format(zero_point)) 
	file.write('K) {} {} #plate scale (dx dy) [arcsec per pixel] \n'.format(K[0], K[0]))
	file.write('O) regular #display type \n')
	file.write('P) 0 #normal run \n')
	file.write('0) sersic #object type \n')
	file.write('1) {} {} 1 1 #position x y [pixel] \n'.format(xcenter,ycenter))  
	file.write('3) {} 1 #integrated magnitude \n'.format(three[0]))
	file.write('4) {} 1 #half light radius [pixel] \n'.format(four[0]))
	file.write('5) {} 1 #concentration \n'.format(five[0]))
	file.write('6) 0.0000 0 \n')
	file.write('7) 0.0000 0 \n')
	file.write('8) 0.0000 0 \n')
	file.write('9) {} 1 #axis ratio \n'.format(nine[0]))
	file.write('10) {} 1 #position angle \n'.format(ten[0]))
	file.write('Z) 0 #dont skip this model \n')
	file.write('0) sky #object type \n')
	file.write('1) 0 0 #sky background at center of fitting region [ADUs] \n')
	file.write('2) 0.0000 0 #dsky/dx \n')
	file.write('3) 0.0000 0 #dsky/dy \n')
	file.write('Z) 0 #dont skip this model \n')
	file.close()
