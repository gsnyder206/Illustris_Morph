import matplotlib.pyplot as plt
import numpy as np

parameter='RP'

fig = plt.figure()
ax = plt.subplot(111)

#data
xr, yr, errr=np.loadtxt('/Users/aquirk/Desktop/Medians/Medianred.txt', unpack=True)
xb, yb, errb=np.loadtxt('/Users/aquirk/Desktop/Medians/Medianblue.txt', unpack=True)
xSr50, ySr50=np.loadtxt('/Users/aquirk/Desktop/Medians/SFR_50_red.txt', unpack=True)
xSr100, ySr100=np.loadtxt('/Users/aquirk/Desktop/Medians/SFR_100_red.txt', unpack=True)
xSb50, ySb50=np.loadtxt('/Users/aquirk/Desktop/Medians/SFR_50_blue.txt', unpack=True)
xSb100, ySb100=np.loadtxt('/Users/aquirk/Desktop/Medians/SFR_100_blue.txt', unpack=True)
xSr1, ySr1=np.loadtxt('/Users/aquirk/Desktop/Medians/SFR_1_red.txt', unpack=True)
xSb1, ySb1=np.loadtxt('/Users/aquirk/Desktop/Medians/SFR_1_blue.txt', unpack=True)
xSr10, ySr10=np.loadtxt('/Users/aquirk/Desktop/Medians/SFR_10_red.txt', unpack=True)
xSb10, ySb10=np.loadtxt('/Users/aquirk/Desktop/Medians/SFR_10_blue.txt', unpack=True)
xMassb10, yMassb10, M10errb=np.loadtxt('/Users/aquirk/Desktop/Medians/Mass_10.5_blue.txt',unpack=True)
xMassr10, yMassr10, M10errr=np.loadtxt('/Users/aquirk/Desktop/Medians/Mass_10.5_red.txt',unpack=True)
xMassb11, yMassb11, M11errb=np.loadtxt('/Users/aquirk/Desktop/Medians/Mass_11_blue.txt',unpack=True)
xMassr11, yMassr11, M11errr=np.loadtxt('/Users/aquirk/Desktop/Medians/Mass_11_red.txt',unpack=True)
xMagr24, yMagr24=np.loadtxt('/Users/aquirk/Desktop/Medians/Mag_24.5_red.txt', unpack=True)
xMagb24, yMagb24=np.loadtxt('/Users/aquirk/Desktop/Medians/Mag_24.5_blue.txt', unpack=True)
xSNb3, ySNb3=np.loadtxt('/Users/aquirk/Desktop/Medians/SN_3_blue.txt',unpack=True)
xSNr3, ySNr3=np.loadtxt('/Users/aquirk/Desktop/Medians/SN_3_red.txt',unpack=True)
xSNb10, ySNb10=np.loadtxt('/Users/aquirk/Desktop/Medians/SN_10_blue.txt',unpack=True)
xSNr10, ySNr10=np.loadtxt('/Users/aquirk/Desktop/Medians/SN_10_red.txt',unpack=True)
xSNb30, ySNb30=np.loadtxt('/Users/aquirk/Desktop/Medians/SN_30_blue.txt',unpack=True)
xSNr30, ySNr30=np.loadtxt('/Users/aquirk/Desktop/Medians/SN_30_red.txt',unpack=True)
xM105SFR10b, yM105SFR10b, MSFR10errb=np.loadtxt('/Users/aquirk/Desktop/Medians/Mass10.5_SFR10_blue.txt',unpack=True)
xM105SFR10r, yM105SFR10r, MSFR10errr=np.loadtxt('/Users/aquirk/Desktop/Medians/Mass10.5_SFR10_red.txt',unpack=True)
xM105SFR50b, yM105SFR50b, MSFR50errb=np.loadtxt('/Users/aquirk/Desktop/Medians/Mass10.5_SFR50_blue.txt',unpack=True)
xM105SFR50r, yM105SFR50r, MSFR50errr=np.loadtxt('/Users/aquirk/Desktop/Medians/Mass10.5_SFR50_red.txt',unpack=True)
xRP5r,yRP5r=np.loadtxt('/Users/aquirk/Desktop/Medians/RP_5_red.txt',unpack=True)
xRP5b,yRP5b=np.loadtxt('/Users/aquirk/Desktop/Medians/RP_5_blue.txt',unpack=True)
xRP7r,yRP7r=np.loadtxt('/Users/aquirk/Desktop/Medians/RP_7_red.txt',unpack=True)
xRP7b,yRP7b=np.loadtxt('/Users/aquirk/Desktop/Medians/RP_7_blue.txt',unpack=True)
xRP3r,yRP3r=np.loadtxt('/Users/aquirk/Desktop/Medians/RP_3_red.txt',unpack=True)
xRP3b,yRP3b=np.loadtxt('/Users/aquirk/Desktop/Medians/RP_3_blue.txt',unpack=True)
xSMA3b, ySMA3b, SMA3errb=np.loadtxt('/Users/aquirk/Desktop/Medians/SmA_3_blue.txt',unpack=True)
xSMA3r, ySMA3r, SMA3errr=np.loadtxt('/Users/aquirk/Desktop/Medians/SmA_3_red.txt',unpack=True)
xSMA5b, ySMA5b, SMA5errb=np.loadtxt('/Users/aquirk/Desktop/Medians/SmA_5_blue.txt',unpack=True)
xSMA5r, ySMA5r, SMA5errr=np.loadtxt('/Users/aquirk/Desktop/Medians/SmA_5_red.txt',unpack=True)
xSMA5M11r, ySM5M11r, SMA5M11errr=np.loadtxt('/Users/aquirk/Desktop/Medians/SMA5_Mass11_red.txt',unpack=True)
xSMA5M11b, ySM5M11b, SMA5M11errb=np.loadtxt('/Users/aquirk/Desktop/Medians/SMA5_Mass11_blue.txt',unpack=True)
xLSMA3b, yLSMA3b=np.loadtxt('/Users/aquirk/Desktop/Medians/L.SMA_3_blue.txt',unpack=True)
xLSMA3r, yLSMA3r=np.loadtxt('/Users/aquirk/Desktop/Medians/L.SMA_3_red.txt',unpack=True)

#no cuts
plt.errorbar(xb,yb,errb, label='460nm')
plt.errorbar(xr,yr,errr, color='r', label='730nm')

#SMiA and Mass cuts
#plt.errorbar(xSMA5M11r, ySM5M11r,SMA5M11errr, color='r',linestyle='--',label='SmA>5*PSF and Mass>10^11')
#plt.errorbar(xSMA5M11b, ySM5M11b, SMA5M11errb, color='b',linestyle='--',label='SmA>5*PSF and Mass>10^11')

#SMiA cuts
#plt.errorbar(xSMA3b, ySMA3b, SMA3errb, color='b',linestyle='--',label='SmA>3PSF')
#plt.errorbar(xSMA3r, ySMA3r, SMA3errr, color='r',linestyle='--',label='SmA>3PSF')
#plt.errorbar(xSMA5b, ySMA5b, SMA5errb, color='b',linestyle=':',label='SmA>5PSF')
#plt.errorbar(xSMA5r, ySMA5r, SMA5errr, color='r',linestyle=':',label='SmA>5PSF')
#plt.plot(xLSMA3b, yLSMA3b,color='b',linestyle='--',label='SmA<3PSF')
#plt.plot(xLSMA3r, yLSMA3r,color='r',linestyle='--',label='SmA<3PSF')

#RP cuts
#plt.plot(xRP3b,yRP3b, color='b',linestyle='--',label='RP<3PSF')
#plt.plot(xRP3r,yRP3r, color='r',linestyle='--',label='RP<3PSF')
#plt.plot(xRP5b,yRP5b, color='b',linestyle='-.',label='RP>5PSF')
#plt.plot(xRP5r,yRP5r, color='r',linestyle='-.',label='RP>5PSF')
#plt.plot(xRP7b,yRP7b, color='b',linestyle=':',label='RP>7PSF')
#plt.plot(xRP7r,yRP7r, color='r',linestyle=':',label='RP>7PSF')

#SFR AND Mass cuts
plt.errorbar(xM105SFR10b, yM105SFR10b, MSFR10errb, color='b',linestyle='--',label='SFR>10, Mass>10E10.5')
plt.errorbar(xM105SFR10r, yM105SFR10r, MSFR10errr, color='r',linestyle='--',label='SFR>10, Mass>10E10.5')
plt.errorbar(xM105SFR50b, yM105SFR50b, MSFR50errb, color='b',linestyle=':',label='SFR>50, Mass>10E10.5')
plt.errorbar(xM105SFR50r, yM105SFR50r, MSFR50errr, color='r',linestyle=':',label='SFR>50, Mass>10E10.5')

#S/N cuts
#plt.plot(xSNb3, ySNb3, color='b', linestyle='--', label='S/N>3')
#plt.plot(xSNr3, ySNr3, color='r', linestyle='--', label='S/N>3')
#plt.plot(xSNb10, ySNb10, color='b', linestyle=':', label='S/N>10')
#plt.plot(xSNr10, ySNr10, color='r', linestyle=':', label='S/N>10')
#plt.plot(xSNb30, ySNb30, color='b', linestyle='-.', label='S/N>30')
#plt.plot(xSNr30, ySNr30, color='r', linestyle='-.', label='S/N>30')

#Mag cuts
#plt.plot(xMagr24,yMagr24, color='r', linestyle='--', label='Mag<24.5')
#plt.plot(xMagb24,yMagb24, color='b', linestyle='--', label='Mag<24.5')

#Mass cuts
#plt.errorbar(xMassb10, yMassb10, M10errb, color='b', linestyle='--', label='Mass>10^10.5')
#plt.errorbar(xMassr10, yMassr10, M10errr, color='r', linestyle='--', label='Mass>10^10.5')
#plt.errorbar(xMassb11, yMassb11, M11errb, color='b', linestyle=':', label='Mass>10^11')
#plt.errorbar(xMassr11, yMassr11, M11errr, color='r', linestyle=':', label='Mass>10^11')

#SFR cuts
#plt.plot(xSb10, ySb10, color='k', linestyle='--', label='blue SFR<10')
#plt.plot(xSr10, ySr10, color='k', linestyle=':', label='red SFR<10')
#plt.plot(xSb1, ySb1, color='b', linestyle='-.', label='SFR<1')
#plt.plot(xSr1, ySr1, color='r', linestyle='-.', label='SFR<1')
#plt.plot(xSr50,ySr50, color='r', linestyle='--', label='SFR>50')
#plt.plot(xSr100,ySr100, color='r', linestyle=':', label='SFR>100')
#plt.plot(xSb50,ySb50, color='b', linestyle='--', label='SFR>50')
#plt.plot(xSb100,ySb100, color='b',linestyle=':', label='SFR>100')

#plotting
plt.gca().invert_xaxis()
plt.xlabel('Redshift')
plt.ylabel('1/elong')
plt.title('Change in Axis Ratio')
plt.legend(loc=3)
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
#ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#plt.savefig('/Users/aquirk/Desktop/{}deltaaxisratio.png'.format(parameter))
plt.show()
