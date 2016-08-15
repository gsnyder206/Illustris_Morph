import pandas as pd
import matplotlib.pyplot as plt

#reads in data for the result output of the random forest
result=pd.read_pickle('/Users/aquirk/Desktop/PyML_Illustris/result_cut_PC_0_0.5_105.pkl')

#reads probability data from random forest
probability=pd.read_pickle('/Users/aquirk/Desktop/PyML_Illustris/label_probability_cut_PC_0_0.5_105.pkl')

#probability is a matrix: Number of galaxies x number of iterations
#below averages the probability over all the iterations for each galaxy
P=probability.sum(axis=1)/1000

#plotting
plt.hist(P)
#plt.hist(result['PC3'])
plt.title('RF with Cuts and PCs z=0.5 (WFC3-F105W)')
plt.xlabel('Average Probability that Label Follows Random Forest')
plt.savefig('/Users/aquirk/Desktop/probability_cut_PC_0_0.5_105.png')
