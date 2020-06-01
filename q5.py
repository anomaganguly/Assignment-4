#Random numbers distributed according to Gaussian distribution

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

x1 = np.random.rand(10000)							#Uniform random numbers in 0 to 1
x2 = np.random.rand(10000)
y1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)	#Box Muller transformation from uniform pdf to normal pdf
y2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

x = np.linspace(-4, 4, num=100)						#100 uniformly spaced points from -4 to +4
nd =  norm.pdf(x , 0, 1)							#Normal pdf

figure, axes = plt.subplots(figsize=(6,8), nrows = 2, ncols = 1)	#plotiing
plt.title("Normal PDF")

axes[0].hist(y1, density=True)						#density histogram
axes[0].plot(x, nd, 'r')							#plotting true normal pdf
axes[0].set_xlabel('x1')
axes[0].set_ylabel('PDF')

axes[1].hist(y1, density=True)
axes[1].plot(x, nd, 'r')
axes[1].set_xlabel('x2')
axes[1].set_ylabel('PDF')

figure.tight_layout()
plt.show()