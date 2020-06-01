# A linear congruential generator

import numpy as np
from scipy.stats import uniform
import time
import matplotlib.pyplot as plt

t0 = time.time()						#starting time
a = 7689								#choice of parameters
c = 9135
m =  10001								#range of random number from 0 to 10000
x1 = 1

n = 10000  								#reqd range
rand = []								#array to store random number

for i in range (n):
	x1 = (a*x1 + c)%m						#generating random number
	rand.append(x1*0.0001)				#range in 0 to 1 by multiplying by 1/10000

t1 = time.time()-t0
print("Time taken by linear congruential generator", t1)	#printing reqd time 	


plt.hist(rand, bins = 10, density=True)				#plotting histogram of random numbers generated
plt.plot(rand, uniform.pdf(rand), label="uniform pdf")
plt.xlabel("x")
plt.ylabel("PDF")
plt.title("Density histogram (Linear congruential generator)")
plt.legend()
plt.savefig("q1.png")

# Random number generator from NumPy

t2 = time.time()						#starting time
x2 = np.random.rand(10000)				#generating random numbers using NumPy

t3 = time.time()-t2

print("Time taken by Numpy random number generator", t3)	#printing time taken
print("Time difference between two methods", t1-t3)

fig1 = plt.figure()
plt.hist(x1, bins = 10, density=True)									#plotting histogram	
plt.plot(x1, uniform.pdf(x1), label="uniform pdf")						#plotting true distribution
plt.xlabel("x")

fig2 = plt.figure()
plt.hist(x2, bins = 10, density=True)									#plotting histogram	
plt.plot(x2, uniform.pdf(x2), label="uniform pdf")						#plotting true distribution
plt.xlabel("x")
plt.ylabel("PDF")
plt.title("Density histogram (NumPy generator)")
plt.legend()
plt.show()
