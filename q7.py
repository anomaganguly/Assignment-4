#Chi square test

import numpy as np
from scipy.stats import chi2

ntrials = 100000											#number of trials to get true probability																				
nc = 144													#number of times two dice were thrown			
s = np.random.randint(1, high=7, size=ntrials) + np.random.randint(1, high=7, size=ntrials)#sum of random numbers generated in two throws of dice

v, ns = np.unique(s, return_counts = True)					#returns the unique array with the number of times a particular element occurs in s			

nps = np.array(nc*ns/ntrials)

vxi = np.zeros(2)											#array to store values of v for two different simulations
x = np.zeros(2)

y1 = np.asarray([4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13])#random numbers generated in first trial
y2 = np.asarray([3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5])	#random numbers generated in second trial


for i in range (0, 11):
	vxi[0] = vxi[0] + np.square(y1[i] - nps[i])/nps[i]		#finding v for first trial
	vxi[1] = vxi[1] + np.square(y2[i] - nps[i])/nps[i]		#finding v for second trial
	
x = (1.0 - chi2.cdf(vxi, 10))*100

for i in range (0, 2):										#different cases of chi2 test result
	print("The value of V for", i+1, "trial is", x[i])
	if (x[i]<1 or x[i]>99):
		print("The counts of this trial are not sufficiently random")
	elif (1<x[i]<5 or 95<x[i]<99):
		print ("The counts of this trial are suspect")
	elif (5<x[i]<10 or 90<x[i]<95):
		print ("The counts of this trial are almost suspect")
	elif (10<x[i]<90):
		print ("The counts of this trial are sufficiently random")