import numpy as np
import h5py
import matplotlib.pyplot as plt

#this program selects subhalos from a given redshift and filter and camera 0 to create a subpopulation to compare axis ratios to GALFIT

#file
catalog=catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")

#loads in parameters
haloID=catalog['nonparmorphs']['snapshot_085']['SubfindID'].value
mass=catalog['nonparmorphs']['snapshot_085']['Mstar_Msun'].value 
PSF=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['APPROXPSF_ARCSEC'].value #pixels
Pix_as=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['PIX_ARCSEC'].value #arcsecs/pixel
elongation=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['ELONG'].value
RP=catalog['nonparmorphs']['snapshot_085']['NC-F277W']['CAMERA0']['RP'].value #pixels


#adds the index of qualifying subhalos
#aim to get a broad range of mass, size, and 1/e
#does not add NaNs
sub_mass1=[]
sub_mass2=[]
sub_mass3=[]
sub_mass4=[]
for i in range(len(mass)):
	if np.isnan(mass[i])==False and np.isnan(RP[i])==False and np.isnan(elongation[i])==False:
		if (10**10)<mass[i]<(10**10.5):
			sub_mass1.append(np.where(mass==mass[i])[0])
		if (10**10.5)<mass[i]<(10**11):
			sub_mass2.append(np.where(mass==mass[i])[0])
		if (10**11)<mass[i]<(10**11.5):
			sub_mass3.append(np.where(mass==mass[i])[0])
		if (10**11.5)<mass[i]:
			sub_mass4.append(np.where(mass==mass[i])[0])
sub_RP1=[]
sub_RP2=[]
sub_RP3=[]
sub_RP4=[]
for i in range(len(RP)):
        if np.isnan(mass[i])==False and np.isnan(RP[i])==False and np.isnan(elongation[i])==False:
		if 0<RP[i]<20:
			sub_RP1.append(np.where(RP==RP[i])[0])
		if 20<RP[i]<40:
			sub_RP2.append(np.where(RP==RP[i])[0])			
		if 40<RP[i]<60:
			sub_RP3.append(np.where(RP==RP[i])[0])
		if 60<RP[i]:	
			sub_RP4.append(np.where(RP==RP[i])[0])

sub_elong1=[]
sub_elong2=[]
sub_elong3=[]
sub_elong4=[]
sub_elong5=[]
for i in range(len(elongation)):
	if np.isnan(mass[i])==False and np.isnan(RP[i])==False and np.isnan(elongation[i])==False:
		if 1<elongation[i]<1.5:
			sub_elong1.append(np.where(elongation==elongation[i])[0])
		if 1.5<elongation[i]<2:
			sub_elong2.append(np.where(elongation==elongation[i])[0])
		if 2<elongation[i]<2.5:
			sub_elong3.append(np.where(elongation==elongation[i])[0])
		if 2.5<elongation[i]<4:
			sub_elong4.append(np.where(elongation==elongation[i])[0])
		if 4<elongation[i]:
			sub_elong5.append(np.where(elongation==elongation[i])[0])
#np.random.choice was being difficult so I am picking by hand
shIDs=[]
for i in range(len(sub_mass3)):
	shIDs.append(haloID[sub_mass3[i]])
#print(shIDs)

