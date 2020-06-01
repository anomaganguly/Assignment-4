#Fitting a model using MCMC

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import emcee
import corner


def log_likelihood(theta, x, y, yerr):								#defining the negative of log of likelihood fn(Normal)
	a, b, c = theta
	model = a*x**2 + b*x + c
	sigma2 = yerr**2
	return 0.5*np.sum((y-model)**2/sigma2+np.log(2*np.pi*sigma2))

def log_prior(theta):												#defining log of prior
	a, b, c = theta
	if -500.0<a<500.0 and -500.0<b<500.0 and -600.0<c<700.0:	
		return 0
	return -np.inf
	
def log_probability(theta, x, y, yerr):								#log of reqd prob distribution
	lp = log_prior(theta)
	if not np.isfinite(lp):
		return -np.inf
	return lp - log_likelihood(theta, x, y, yerr)

with open('data.txt') as f:											#opening file to read data
	lines_after_5 = f.readlines()[5:]

x = []
y = []
sigmay = []	

for line in lines_after_5[0:]:										#reading the data and storing into arrays
	delimeter = "&"
	p = line.split(delimeter)
	x.append(float(p[1]))
	y.append(float(p[2]))
	sigmay.append(float(p[3]))

x = np.asarray(x)
y = np.asarray(y)
sigmay = np.asarray(sigmay)

guess = (1.0, 8.0, 10.0)											#guess on the minimum of likelihood fn
soln = minimize(log_likelihood, guess, args=(x, y, sigmay))			#finding minimum of likelihood fn

nchain, dim = 50, 3													#50 chains in 3 d

pos = soln.x + 1e-4*np.random.randn(nchain, dim)					

sampler = emcee.EnsembleSampler(nchain, dim, log_probability, args=(x, y, sigmay))#MCMC
sampler.run_mcmc(pos, 4000)


samples = sampler.get_chain() 

tau = sampler.get_autocorr_time()
print("Auto-correlation time: ", tau)

fig1, ax = plt.subplots(3, 1, sharex='col', figsize= (8, 6))	#plotting the chains for the parameters
ax[0].plot(samples[:, :, 0], 'r.', markersize=0.5) # a values 
ax[0].set_ylabel('a')

ax[1].plot(samples[:, :, 1], 'y.', markersize=0.5) # b values
ax[1].set_ylabel('b')

ax[2].plot(samples[:, :, 2], 'g.', markersize=0.5) # c values
ax[2].set_xlabel('steps')
ax[2].set_ylabel('c')

fig1.tight_layout()
plt.show()

medians = np.median(samples, axis=0)

flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)#making the sample by discarding the first 100 chains

a_true, b_true, c_true = np.median(flat_samples, axis=0)

labels = ["a", "b", "c"]

fig2 = corner.corner(flat_samples, labels=labels, truths=[a_true, b_true, c_true])#joint and marginalised PDF of the parameters

plt.show()

fig3 = plt.figure()
x0 = np.linspace(40, 300, num=500)										#plotting the best-fit model and 200 other models

inds = np.random.randint(len(flat_samples), size=200)
for ind in inds:
    sample = flat_samples[ind]
    plt.plot(x0, np.dot(np.vander(x0, 3), sample[:3]), 'y', alpha=0.1)
	
plt.errorbar(x, y, yerr=sigmay, fmt=".k", capsize=0, label="data points")
plt.plot(x0, a_true * x0**2 + b_true*x0 + c_true, "k", label="truth")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Best fit model")
plt.legend()
plt.show()
