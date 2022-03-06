"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Dirac Delta Functions
Author       : Chitrak Roychowdhury
"""


#Dirac Delta Function
#\epsilon ---> 0
#func = 1/(np.sqrt(2*np.pi*\epsilon*i))*np.exp((x**2*i)/2*\epsilon)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

a = 1.0                #peak position of delta function
x1 = a-5; x2 = a+5 #x-range for plotting peak of delta func
i = np.sqrt(-1)

#Representation of Dirac Delta function 
def ddf(x,eps):
    return 1/(np.sqrt(2*np.pi*eps*i))*np.exp((x**2*i)/2*eps)
ddf=np.vectorize(ddf)

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
plt.xlim(-5,7)
plt.ylim(0,5)
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
