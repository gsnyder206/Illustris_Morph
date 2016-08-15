import matplotlib.pyplot as plt
import numpy as np
import h5py
from matplotlib.colors import LogNorm
import matplotlib.ticker as ticker

#this script plots the subpopulations of illstris to compare measurements by photutils to those made by galfit
#MUST CUSTOMIZE FOR VARIABLE AND REST WAVELENGTH

shIDr, nr, gqr, pqr=np.loadtxt('/Users/aquirk/Desktop/galfit/subpopulation/red/subpopulation_red.txt', usecols=(0,1,2,3,), unpack=True)
shIDb, nb,  gqb, pqb=np.loadtxt('/Users/aquirk/Desktop/galfit/subpopulation/blue/subpopulation_blue.txt', usecols=(0,1,2,3,), unpack=True)

#histograms
medp=np.median(pqr)
medg=np.median(gqr)
#plt.hist(pqr, 10, color='b', alpha=0.5, normed=True, label='photutils Med={}'.format(medp))
#plt.hist(gqr, 10, color='r', alpha=0.3, normed=True, label='galfit Med={}'.format(medg))
#plt.xlabel('1/e')
#plt.title('Projected Axis Ratio for Illustris Subpopulation (NC-F277W)')
#plt.legend(loc=2)

#scatter plots
x_r=np.linspace(1,len(shIDr),len(shIDr))

#plt.scatter(x_r, pqr, color='b', label='photutils')
#plt.scatter(x_r, gqr, color='r', label='galfit')
#plt.xlim(0,100)
#plt.xlabel('Galaxy ID in Subpopulation (not the same as shID)')
#plt.ylabel('1/e')
#plt.title('Comparison of Individual Measurements (NC-F277W)')
#plt.legend()

#plt.show()
#plt.savefig('/Users/aquirk/Desktop/q_comp_red.png')

#sets conditions for h5py data
camera='CAMERA0'
snapshot='snapshot_085'
filt='WFC3-F105W' #red 277 blue 105

subhaloID=np.loadtxt('/Users/aquirk/Desktop/galfit/subpopulation/subpopulation.txt', unpack=True)

#loads image file and data for a given camera, snapshot, and filter
catalog=catalog= h5py.File("/astro/snyder_lab2/Illustris/MorphologyAnalysis/nonparmorphs_SB25_12filters_morestats.hdf5")
haloID=catalog['nonparmorphs'][snapshot]['SubfindID'].value
HLR=catalog['nonparmorphs'][snapshot][filt][camera]['RHALF'].value #pixels
concentration=catalog['nonparmorphs'][snapshot][filt][camera]['CC'].value
RP=catalog['nonparmorphs'][snapshot][filt][camera]['RP'].value
mass=catalog['nonparmorphs'][snapshot]['Mstar_Msun'].value
M20=catalog['nonparmorphs'][snapshot][filt][camera]['M20'].value
G=catalog['nonparmorphs'][snapshot][filt][camera]['GINI'].value

half_light_radius=[]
petrosian_radius=[]
masses=[]
m_20=[]
gini=[]
for i in range(len(subhaloID)):
	n=np.where(haloID==subhaloID[i])	
	half_light_radius.append(HLR[n])
	petrosian_radius.append(RP[n])
	masses.append(mass[n])
	m_20.append(M20[n])
	gini.append(G[n])

F=[]
for i in range(len(subhaloID)):
	if gini[i]>=((0.14*m_20[i])+0.778):
		F.append(abs((-0.693*m_20[i])+(4.95*gini[i])-3.85))
        if gini[i]<((0.14*m_20[i])+0.778):
                F.append(-abs((-0.693*m_20[i])+(4.95*gini[i])-3.85))
fractionalq=[]
for i in range(len(subhaloID)):
	fractionalq.append((pqb[i]-gqb[i])/(gqb[i]))

#plotting
#plt.hist2d(fractionalq, m_20, bins=50, norm=LogNorm())
#plt.scatter(gqb, F, color='r', label='galfit')
#plt.scatter(pqb, F, color='b', label='photutils')
plt.hist(gqr, bins=30, color='r', alpha=0.5)
plt.hist(pqr, bins=30, color='b', alpha=0.5)
plt.title('Illustris Subpopulation z=1 (WFC3-F105W)')
plt.xlabel('1/elongation')
plt.ylabel('N') 
#plt.colorbar()
#plt.show()
plt.savefig('/Users/aquirk/Desktop/comp_q_red.ps')
