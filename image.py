import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from pylab import *
from matplotlib.colors import LogNorm

#this script plots the images created by the GALFIT program

#loads halo IDS
shID=np.loadtxt('/Users/aquirk/Desktop/galfit/subpopulation/subpopulation.txt', usecols=(0,), unpack=True)

#below is a loop to create a converted image for all halos in the subpopulation
for i in range(len(shID)):
	#loads in file (image created by GALFIT)
	hdu_list=fits.open('/Users/aquirk/Desktop/galfit/subpopulation/red/galfit_{0:g}.fits'.format(shID[i]))

	#layers of GALFIT image block (original image, model, and residual)
	original=hdu_list[1].data
	model=hdu_list[2].data
	residual=hdu_list[3].data

	#first layer- original
	ax1=plt.subplot(131)
	plt.imshow(original, vmin=(10**-2), vmax=(10**4), norm=LogNorm())
	ax1.set_title('Original')

	#second layer-model 
	ax2=plt.subplot(132)
	plt.imshow(model, vmin=(10**-2), vmax=(10**4), norm=LogNorm())
	ax2.set_title('GALFIT Model')

	#third layer: orginal-model
	ax3=plt.subplot(133)
	plt.imshow(residual, vmin=(10**-2), vmax=(10**4), norm=LogNorm())
	ax3.set_title('Residual')

	#removes tick marks
	ax1.set_xticks([]) 
	ax1.set_yticks([])
	ax2.set_xticks([]) 
	ax2.set_yticks([])
	ax3.set_xticks([]) 
	ax3.set_yticks([])

	fig = gcf()
	fig.suptitle('Subhalo {0:g} z=1 NC-F277W CAM0 SB25'.format(shID[i]), fontsize=14, y=0.75)
	#plt.subplots_adjust(wspace=0, hspace=0) #removes space between plots
	plt.colorbar()
	plt.savefig('/Users/aquirk/Desktop/galfit/subpopulation/red/newestcomp_image/{0:g}.png'.format(shID[i]), bbox_inches='tight')
	plt.close()
