"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Dirac Delta Function
Author       : Chitrak Roychowdhury
"""


#Dirac Delta Function
#Representation using Hermite Polynomial
#\epsilon ---> 0
#func = (1/np.sqrt(np.pi*\epsilon))*(np.exp(-x**2/\epsilon))*((-1/np.sqrt(\epsilon))**n)*hn(x/np.sqrt(\epsilon))

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite
from scipy.integrate import simps

n = 1                  #order of Hermite polynomial
a = 1.0                #peak position of delta function
x1 = a-5; x2 = a+5     #x-range for plotting peak of delta func
hn = hermite(n)

#Representation of Dirac Delta function 
def ddf(x,n,eps):
    return (1/np.sqrt(np.pi*eps))*(np.exp(-x**2/eps))*((-1/np.sqrt(eps))**n)*hn(x/np.sqrt(eps))
ddf=np.vectorize(ddf)
print("Representation of Dirac Delta function using Hermite polynomial")

#Plot
eps = 0.1
x = np.linspace(x1, x2, 10)
s = np.arange(1,5)
for i in s:
    eps = eps/i
    plt.plot(x,ddf(x-a,n,eps),label="$\epsilon=%f$"%(eps))

plt.xlabel("$x \longrightarrow$")
plt.ylabel ("$\delta(x-a)$")
plt.title("Delta Function")
plt.legend(loc="best")
plt.grid(True)
plt.xlim(-5,7)
plt.ylim(-1,1)
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
xp = np.linspace(a+16.8*eps,a-16.8*eps,10)
I = simps(g(xp)*ddf(xp-a,n,eps),xp)

#Exact result
exact = g(a)

#Print
print("Calculated Result",I, "Exact Value",exact)
