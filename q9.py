#Metropolis algorithm

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def f(x):												#defining the uniform PDF
	if (3 < x < 7):
		return 0.25
	else:
		return 0

npts = 10000											#number of points
x = np.zeros(npts)						

for i in range (1, npts):
	xprime = x[i-1] + np.random.standard_normal()		#choosing x from normal distribution
	r = np.random.rand()								#random number between 0 and 1
	if (f(x[i-1])==0):									#Metropolis algorithm
		x[i] = xprime
	elif (f(xprime)/f(x[i-1]) > r):
		x[i] = xprime
	else:
		x[i] = x[i-1]
		
xplot = np.linspace(2, 8, num=100)
fxplot = np.zeros(100)
iplot = np.linspace(1, 5000, num=5000)

for i in range (0, 100):								#array to store the uniform pdf
	fxplot[i] = f(xplot[i])

fig1 = plt.figure()	
plt.title("Density histogram using Metropolis method")	
plt.hist(x, density=True, bins = 50, range = (2,8))
plt.ylabel("PDF")
plt.xlabel("x")
plt.plot(xplot, fxplot, '-r', label="uniform pdf")
plt.show()

fig2 = plt.figure()
plt.title("Markov chain")
plt.plot(iplot, x[0:5000], '-r', markersize = 0.25)
plt.xlabel("steps")
plt.show()