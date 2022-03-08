"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Dirac Delta Functions
Author       : Chitrak Roychowdhury
"""


#Dirac Delta Function
#Representation using  Modified Sinc Function
#\epsilon ---> 0
#func =  (1/(x*np.pi))*np.sin(x/\epsilon) for x!=0
#     =  (1/2 + 1/\epsilon)/np.pi         for x=0

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

a = 1.0                #peak position of delta function
x1 = a-5; x2 = a+5 #x-range for plotting peak of delta func

#Representation of Dirac Delta function using Modified Sinc Function
def ddf(x,eps):
    if x!=0:
        return 1/(2*np.pi)*(np.sin((1+2/eps)*x/2)/np.sin(x/2))
    else:
        return (1/2 + 1/eps)/np.pi 
ddf=np.vectorize(ddf)
print("Representation of Delta Function using  Modified Sinc Function")

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
plt.ylim(-30,80)
plt.xticks()
plt.yticks()
plt.axvline(0, c='gray',ls='--', lw=1)
plt.axhline(0, c='gray',ls=':', lw=1)
plt.show()

#verification of intrgration of del(x-a)g(x) for limit -inf to +inf = g(a)

#function given
def g(x):
    return np.sin(x)

#evaluating intrgral
xp = np.linspace(a-4.9*eps,a+4.9*eps,1000)
I = simps(g(xp)*ddf(xp-a,eps),xp)

#Exact result
exact = g(a)

#Print
print("Calculated Result",I, "Exact Value",exact)
