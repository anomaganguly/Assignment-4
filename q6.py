#Rejection method

import numpy as np
import matplotlib.pyplot as plt

def g(z):
	return 1/(z**2+1)						#enveloping function

def f(z):
	return np.sqrt(2/np.pi)*np.exp(-z**2/2)	#required PDF for random numbers
	
x = np.random.rand(1000)*np.pi/2			#random numbers between 0 to pi/2
x = np.tan(x)								#cdf of enveloping function
y = np.random.rand(1000)*g(x)				#y points having range of enveloping fn

y_good = y[y < f(x)]						#y points lying inside the required pdf
x_good = x[y < f(x)]						#x points lying inside the required pdf

xpts = np.linspace(0, 8, 100)				


plt.hist(x_good, density=True)				#density pdf of selected x points
plt.plot(xpts, f(xpts), 'r', label="Required PDF")	#plotting the reqd pdf
plt.title("Density histogram of random numbers")
plt.legend()
plt.show()