"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Dirac Delta Functions
Author       : Chitrak Roychowdhury
"""


#Dirac Delta Function
#Representation using Limit of Gaussian Function
#\epsilon ---> 0
#func =  1/(\epsilon*np.sqrt(2*np.pi))*np.exp(-x**2/(2*\epsilon**2))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

a = 1.0                #peak position of delta function
x1 = a-0.1; x2 = a+0.1 #x-range for plotting peak of delta func

#Representation of Dirac Delta function using Gaussian Function
def ddf(x,eps):
    return 1/(eps*np.sqrt(2*np.pi))*np.exp(-x**2/(2*eps**2))
ddf=np.vectorize(ddf)
print("Representation of Delta Function using Limit of Gaussian Function")

#Plot
eps = 0.1
x = np.linspace(x1, x2, 1000)
s = np.arange(1,5)
for i in s:
    eps = eps/i
    plt.plot(x,ddf(x-a,eps),label="$\epsilon=%f$"%(eps))

plt.xlabel("$x \longrightarrow$")
plt.ylabel ("$\delta(x-a)$")
plt.title("Delta Function")
plt.legend(loc="best")
plt.grid(True)
plt.xlim(0.5,1.5)
plt.ylim(0,100)
plt.xticks()
plt.yticks()
plt.axvline(0, c='gray',ls='--', lw=1)
plt.axhline(0, c='gray',ls=':', lw=1)
plt.show()

#verification of intrgration of del(x-a)g(x) for limit -inf to +inf = g(a)

#function given
def g(x):
    return x**2

#evaluating intrgral
xp = np.linspace(a-5*eps,a+5*eps,1000)
I = simps(g(xp)*ddf(xp-a,eps),xp)

#Exact result
exact = g(a)

#Print
print("Calculated Result",I, "Exact Value",exact)
