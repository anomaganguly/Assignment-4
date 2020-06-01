#Area using Monte Carlo method

import numpy as np
		
def f(z):							#function returns 1 only if x<=1 otherwise 0
	if (z <= 1):
		return 1
	else:
		return 0
		
a = -1								#range of unit circle
b = 1

npts = 600000						#number of random nos

dim = 2								#circle 2d
nrand = np.zeros((npts, dim))	
fd = 0

for i in range (0, dim):
	nrand[:,i] = (np.random.rand(npts)-0.5)*(b-a)	#ith column has set of npts random numbers
													#generating random nos. in range -1 to +1
	
for i in range (0, npts):
	fsum = 0
	for j in range (0, dim):
		fsum +=  nrand[i][j]**2						
	fd += f(fsum)
	
i = ((b-a)**dim)*fd/(npts)			#finding the area				

print("Area of circle is:", i)

dim = 10							#in 10-d
nrand = np.zeros((npts, dim))
fd = 0

for i in range (0, dim):
	nrand[:,i] = (np.random.rand(npts)-0.5)*(b-a)#generating random nos. in range -1 to +1

for i in range (0, npts):
	fsum = 0
	for j in range (0, dim):
		fsum +=  nrand[i][j]**2		#finding volume
	fd += f(fsum)
		
idim = ((b-a)**dim)*fd/npts

print("Volume of 10-d sphere", idim)