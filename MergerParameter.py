import h5py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

#sets parameters for the code
snap='snapshot_068'
restfilt='NC-F115W' #rest frame lambda that all z's share- red or blue
parameter1='ASYM'
parameter2='GINI'

#data files
morph_catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")
merg_catalog=h5py.File('/astro/snyder_lab2/Illustris/MorphologyAnalysis/imagedata_mergerinfo.hdf5')

#reads in all parameter data for a given z and filter
variable1_0=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA0'][parameter1].value
variable1_1=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA1'][parameter1].value
variable1_2=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA2'][parameter1].value
variable1_3=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA3'][parameter1].value

variable2_0=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA0'][parameter2].value
variable2_1=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA1'][parameter2].value
variable2_2=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA2'][parameter2].value
variable2_3=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA3'][parameter2].value

#reads in mass, SFR, PSF, and pixels to as, data
mass=morph_catalog['nonparmorphs'][snap]['Mstar_Msun'].value
PSF=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA0']['APPROXPSF_ARCSEC'].value
SFR=morph_catalog['nonparmorphs'][snap]['SFR_Msunperyr'].value
PIX_AS=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA0']['PIX_ARCSEC'].value

#reads in merger info for a given z
NM=merg_catalog['mergerinfo'][snap]['latest_NumMajorMergersLastGyr'].value

#reads in RP and magnitude data
mag_0=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA0']['MAG'].value
mag_1=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA1']['MAG'].value
mag_2=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA2']['MAG'].value
mag_3=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA3']['MAG'].value
RP_0=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA0']['RP'].value
RP_1=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA1']['RP'].value
RP_2=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA2']['RP'].value
RP_3=morph_catalog['nonparmorphs'][snap][restfilt]['CAMERA3']['RP'].value

#below gets rid of Nan values 
#does this individually for each camera view angle
#view angle 0
NumMergers_0=[] #this will have the total number of mergers- minor and major since time specified above
V1_0=[]
V2_0=[]
M_0=[]
SFR_0=[]
MAG_0=[]
R_0=[]
for i in range(len(variable1_0)):
        if np.isnan(RP_0[i])==False and np.isnan(mag_0[i])==False and np.isnan(SFR[i])==False and np.isnan(mass[i])==False and np.isnan(variable1_0[i])==False and np.isnan(variable2_0[i])==False and np.isnan(NM[i])==False:
                NumMergers_0.append(NM[i])
		V1_0.append(variable1_0[i])
		V2_0.append(variable2_0[i])
		M_0.append(mass[i])
		SFR_0.append(SFR[i])
		MAG_0.append(mag_0[i])
		R_0.append(RP_0[i])
#view angle 1
NumMergers_1=[] #this will have the total number of mergers- minor and major since time specified above
V1_1=[]
V2_1=[]
M_1=[]
SFR_1=[]
MAG_1=[]
R_1=[]
for i in range(len(variable1_0)):
        if np.isnan(RP_1[i])==False and np.isnan(mag_1[i])==False and np.isnan(SFR[i])==False and np.isnan(mass[i])==False and np.isnan(variable1_1[i])==False and np.isnan(variable2_1[i])==False and np.isnan(NM[i])==False:
                NumMergers_1.append(NM[i])
                V1_1.append(variable1_1[i])
                V2_1.append(variable2_1[i])
		M_1.append(mass[i])
                SFR_1.append(SFR[i])
                MAG_1.append(mag_0[i])
                R_1.append(RP_0[i])
#view angle 2
NumMergers_2=[] #this will have the total number of mergers- minor and major since time specified above
V1_2=[]
V2_2=[]
M_2=[]
SFR_2=[]
MAG_2=[]
R_2=[]
for i in range(len(variable1_0)):
        if np.isnan(RP_2[i])==False and np.isnan(mag_2[i])==False and np.isnan(SFR[i])==False and np.isnan(mass[i])==False and np.isnan(variable1_2[i])==False and np.isnan(variable2_2[i])==False and np.isnan(NM[i])==False:
                NumMergers_2.append(NM[i])
                V1_2.append(variable1_2[i])
                V2_2.append(variable2_2[i])
		M_2.append(mass[i])
                SFR_2.append(SFR[i])
                MAG_2.append(mag_0[i])
                R_2.append(RP_0[i])
#view angle 0
NumMergers_3=[] #this will have the total number of mergers- minor and major since time specified above
V1_3=[]
V2_3=[]
M_3=[]
SFR_3=[]
MAG_3=[]
R_3=[]
for i in range(len(variable1_0)):
        if np.isnan(RP_3[i])==False and np.isnan(mag_3[i])==False and np.isnan(SFR[i])==False and np.isnan(mass[i])==False and np.isnan(variable1_3[i])==False and np.isnan(variable2_3[i])==False and np.isnan(NM[i])==False:
                NumMergers_3.append(NM[i])
                V1_3.append(variable1_3[i])
                V2_3.append(variable2_3[i])
		M_3.append(mass[i])        
                SFR_3.append(SFR[i])
                MAG_3.append(mag_0[i])
                R_3.append(RP_0[i])

#adds all of the data from the camera angles together
NumMergers=NumMergers_0+NumMergers_1+NumMergers_2+NumMergers_3
V1=V1_0+V1_1+V1_2+V1_3
V2=V2_0+V2_1+V2_2+V2_3
M=M_0+M_1+M_2+M_3
Mag=MAG_0+MAG_1+MAG_2+MAG_3
S=SFR_0+SFR_1+SFR_2+SFR_3
R=R_0+R_1+R_2+R_3

#print(len(NumMergers), len(V1), len(V2), len(M), len(Mag), len(S), len(R))

#mass cut
NumMergers_cut=[]
V1_cut=[]
V2_cut=[]
for i in range(len(M)):
	if (10**10.5)<M[i] and (3*PSF[0])<(R[i]*PIX_AS[0]) and 5<S[i] and 23>Mag[i]:
		NumMergers_cut.append(NumMergers[i])
		V1_cut.append(V1[i])
		V2_cut.append(V2[i])
#print(len(NumMergers_cut), len(V1_cut), len(V2_cut))

#creating an array that is V2xV1 and where each entry is the mean or median of the number of mergers in that V1 and V2 range
#these will need to be customized to range of the specific variables
rows=np.linspace(0.35,0.75,25) #V2, keep proportional, n*original number of intervals+1
columns=np.linspace(0,1,16) #V1, keep proportional, n*original number of intervals+1
data=np.zeros(shape=(len(rows)-1,len(columns)-1)) #creates array to be filled with data
rowdiff=rows[1]-rows[0]
columndiff=columns[1]-columns[0]

#fills the empty array with the mean of the number of medians placed into each fake cell of the array
for i in range(len(rows)-1):
        for j in range(len(columns)-1):
                cell=[]
		number=[]
                for k in range(len(V1_cut)):
                        if rows[i]<=V2_cut[k] and (rows[i]+rowdiff)>V2_cut[k] and columns[j]<=V1_cut[k] and (columns[j]+columndiff)>V1_cut[k]:
                                number.append(NumMergers_cut[k])
				if NumMergers_cut[k]!=0:
					cell.append(NumMergers_cut[k])
                        if len(number)==0:
				data[i,j]=0
			if len(number)!=0:
				data[i,j]=(float(len(cell))/len(number))

#THIS ASSUMES ZERO IS IN THE TOP LEFT CORNER if you want it in the bottom left corner, invert the y axis

#gets rid of nan values and replaces them with zeros
grid=np.nan_to_num(data)

#plotting
#plt.hist2d(V1_cut,V2_cut, bins=30, norm=LogNorm())
plt.imshow(grid, interpolation='nearest', aspect='auto')
plt.xlabel('Asymmetry')
#plt.xlim((0,1))
#plt.gca().invert_xaxis() #only for 3D M20
plt.ylabel('Gini Coefficient')
#plt.ylim((0.35,0.75)) #limits based on Lotz 04 
plt.gca().invert_yaxis() #only for M20 or only not for M20 if 3D
plt.title('z=2 WFC3-F160W')
plt.colorbar()
#plt.show()
plt.savefig('/Users/aquirk/Desktop/3Dasym_gini_multicut_115.png')
