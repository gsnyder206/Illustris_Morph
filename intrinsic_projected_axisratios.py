import numpy as np
import matplotlib.pyplot as plt

#creates random numbers 0-1 but not 0
values1=np.random.random_sample((35000))
values2=np.random.random_sample((35000))
values3=np.random.random_sample((35000))

#makes sure there are no zero values
A=[]
B=[]
C=[]
for i in range(len(values1)):
	if values1[i]!=0 and values2[i]!=0 and values3[i]!=0:
		A.append(values1[i])
		B.append(values2[i])
		C.append(values3[i])		

#creates and array so that a[i]>=b[i]>=c[i]
a=[]
b=[]
c=[]
for i in range(len(A)):
	if A[i]>=B[i] and A[i]>=C[i]:
		a.append(A[i])
		if B[i]>=C[i]:
			b.append(B[i])
			c.append(C[i])
		if C[i]>=B[i]:
			b.append(C[i])
			c.append(B[i])
	if B[i]>=A[i] and B[i]>=C[i]:
		a.append(B[i])
		if A[i]>=C[i]:
			b.append(A[i])
			c.append(C[i])
		if C[i]>=A[i]:
			b.append(C[i])
			c.append(A[i])
	if C[i]>=B[i] and C[i]>=A[i]:
		a.append(C[i])
		if B[i]>=A[i]:
			b.append(B[i])
			c.append(A[i])
		if A[i]>=B[i]:
			b.append(A[i])
			c.append(B[i])


#elongated, disk, and spheroid lists-adds 1/e to each shape type based on their characteristics for the intrinsic shape ratios
#(e,d,s)_(a,b,c) adds the individual axes lengths to later be used for projected shape ratios
elongated=[]
e_a=[]
e_b=[]
e_c=[]
disk=[]
d_a=[]
d_b=[]
d_c=[]
spheroid=[]
s_a=[]
s_b=[]
s_c=[]
for i in range(len(a)): #elongated
	if 0.05>(b[i]-c[i]) and 0.4>(b[i]/a[i]) and 0.4>(c[i]/a[i]):
		elongated.append((c[i]/b[i]))
		e_a.append(a[i])
		e_b.append(b[i])
		e_c.append(c[i])
for i in range(len(a)): #disk
	if 0.25>(a[i]-b[i]) and 0.4<(b[i]/a[i]) and 0.4>(c[i]/a[i]):
		disk.append((c[i]/b[i]))
		d_a.append(a[i])
                d_b.append(b[i])
                d_c.append(c[i])
for i in range(len(a)): #spheroid
	if 0.25>(a[i]-b[i]) and 0.25>(b[i]-c[i]) and 0.25>(a[i]-c[i]):
		spheroid.append((c[i]/b[i])) 
		s_a.append(a[i])
                s_b.append(b[i])
                s_c.append(c[i])
#testing
#print(len(spheroid))
#print(np.median(spheroid))
#print(len(e_a), len(e_b), len(e_c))

#projected distribution- for each shape, change a,b,c, and len for beta and gamma and change len for A_pr,B_pr, and C_pr
#creates the beta and gamma terms as desrcibed by Chang et al. 2013
beta=[]
gamma=[]
for i in  range(len(disk)):
	beta.append(d_b[i]/d_a[i])
	gamma.append(d_c[i]/d_a[i])

#creates the A, B, and C terms as describe by Chang et al. 2013
#greg says not to do it this way- fix it later
u=np.random.random_sample((20))
theta=[]
for i in range(len(u)):
        theta.append(np.arccos((2*u[i])-1)) 
phi=[]
v=np.random.random_sample((20))
for i in range(len(v)):
        phi.append(2*np.pi*v[i]) 

A_pr=[]
B_pr=[]
C_pr=[]
for i in range(len(disk)): #gamma and beta have same length
	for j in range(len(theta)):
		for k in range(len(phi)):
			costheta=np.cos(theta[j])
			cosphi=np.cos(phi[k])
			sintheta=np.sin(theta[j])
			sinphi=np.sin(phi[k])
			sin2phi=np.sin(2*phi[k])
			A_pr.append(((costheta**2)/(gamma[i]**2))*((sinphi**2)+((cosphi**2)/(beta[i]**2)))+((sintheta**2)/(beta[i]**2)))
			B_pr.append(costheta*sin2phi*(1-(1/(beta[i]**2)))*(1/(gamma[i]**2)))
			C_pr.append((((sinphi**2)/(beta[i]**2))+(cosphi**2))*(1/(gamma[i]**2)))


#creates list of inverse of elongations
q=[]
for i in range(len(A_pr)):
	Num=(A_pr[i]+C_pr[i]-np.sqrt(((A_pr[i]-C_pr[i])**2)+(B_pr[i])**2))
	Den=(A_pr[i]+C_pr[i]+np.sqrt(((A_pr[i]-C_pr[i])**2)+(B_pr[i])**2))
	Q=(Num/Den)
	if 0<Q:
		q.append(np.sqrt(Q))

print(np.median(q))
#print(np.mean(Denom))	

#median
med=np.median(q)
plt.hist(disk, 50, (0,1), color='r', alpha=0.5, normed=True, label='Intrinsic Distribution')
plt.hist(q, 50, (0,1), color='b', alpha=0.5, normed=True, label='Project Distribution')
plt.title('Axis Ratio for a Spheroid Population')
plt.xlabel('1/e')
plt.legend(loc=2)
#plt.show()
plt.savefig('/Users/aquirk/Desktop/axisratio_disk.pdf')
