import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math as math
from scipy.stats import poisson
import math
import scipy as scipy



l = 25  #lambda for poisson
sig = 5 #sigma for gaussian
mean = 25   #mean for gaussian
size = 1000000   #size of the array
size2 = 1000

x = np.linspace(0, 25, size)


#randomly generated gaussian and poisson equations
H1 = np.random.normal(mean, sig, size)
H0 = np.random.poisson(l, size)


H02 = np.random.poisson(l, size2)
H12 = np.random.normal(mean, sig, size2)


#plotting histogram over each other
plt.figure()
plt.hist(H0, 50, density=True,label="Poisson, $\lambda$ = 25",alpha=0.5, color="blue")
plt.hist(H1, 50, density=True, label="gaussian, $\sigma$ = 5 mean=25",color="orange",alpha = 0.5)
plt.legend()
plt.title("Gaussian vs Poisson Function with 1000000 Data Points")
plt.xlabel("Data Points")
plt.ylabel("Probability")
plt.grid(True)
plt.savefig("gaussvspoisson1000000points.png")

plt.show()


plt.figure()
plt.hist(H02, 50, density=True,label="Poisson, $\lambda$ = 25",alpha=0.5, color="red")
plt.hist(H12, 50, density=True, label="gaussian, $\sigma$ = 5, mean=25",color="green",alpha = 0.5)
plt.legend()
plt.title("Gaussian vs Poisson Function with 1000 Data Points")
plt.xlabel("Data Points")
plt.ylabel("Probability")
plt.grid(True)
plt.savefig("gaussvspoisson1000points.png")
plt.show()










temp0= 0

LLR1 = np.log(H0/H1)
LLR2 = np.log(H02/H12)

y = np.quantile(LLR1, 0.5)
y2 = np.quantile(LLR2, 0.5)

plt.figure()
plt.hist(LLR1, 500, density=True,alpha=0.5, color="red",label="1000000 data points")
plt.hist(LLR2, 50, density=True,alpha=0.5, color="blue",label="1000 data points")
plt.title("Likelihood ratio between Gaussian and Poisson with different sample sizes")
plt.xlabel("log(P(x|$\lambda$)/g(x))")
plt.ylabel("Entries")
plt.grid(True)
#plt.axvline(y, color = "black",label = "LLR1 0.5 quantile")
#plt.axvline(y2, color="green",label=" LLR2 0.5 quantile")
#plt.xlim([-1,3])
plt.legend()
plt.savefig("Likelihood_ratios.png")
plt.show()








