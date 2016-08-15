import numpy as np
import matplotlib.pyplot as plt

#example data
V1=[.1,.7,.65,.2,.9]
V2=[-3,-2.1,-2.3,-.7,-1.9]
NumMergers=[1,2,6,4,3]

#creates the dimensions and intervals of array
#creates array to be filled with data
rows=np.linspace(-3,0,7)
columns=np.linspace(0,1,6)
data=np.zeros(shape=(len(rows)-1,len(columns)-1))

#used for placing data points in an interval
rowdiff=rows[1]-rows[0]
columndiff=columns[1]-columns[0]

#goes through the grid cell by cell and places all of the Z that belongs in the cell (based on the X and Y value)
for i in range(len(rows)-1):
	for j in range(len(columns)-1):
		cell=[]
		for k in range(len(V1)):
			if rows[i]<=V2[k] and (rows[i]+rowdiff)>V2[k] and columns[j]<=V1[k] and (columns[j]+columndiff)>V1[k]:
				cell.append(NumMergers[k])
			data[i,j]=np.mean(cell) #once all of the data that belongs in the cell is placed in it, the average of the Zs in the cells is taken and added to the corresponding entree in the array
#THIS ASSUMES ZERO IS IN THE TOP LEFT CORNER if you want it in the bottom left corner do:
#plt.gca().invert_yaxis()

#converts all nan entrees to 0s
grid=np.nan_to_num(data)
print(grid)

#displays the data
#plt.imshow(grid)
#plt.colorbar()
#plt.show()			
