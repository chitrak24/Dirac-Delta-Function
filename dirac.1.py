"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Ploting Special Functions
Author       : Chitrak Roychowdhury
"""


#Dirac Delta Function
#Representation using Inverse Cosine hyperbolic square function 
#\epsilon ---> 0
#func = 1/(2*\epsilon*cosh(x/\epsilon)**2)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

a=1.0                # position of peak of delta function
x1,x2=-0.5+a,0.5+a   # x-range for plotting about the peak of delta function

# Defining delta function by Inverse cosine hyperbolic square
def delta(x,eps):
     return 1.0/(2.0*eps*np.cosh(x/eps)**2)
delta=np.vectorize(delta)
print("Representation of Delta Function using Inverse Cosine hyperbolic square function")

# plotting delta functions for different eps values
eps = 0.1
x = np.linspace(x1,x2,1000)
s = np.arange(1,5)
for i in s:
    eps=eps/(i)
    plt.plot(x,delta(x-a,eps),label="$\epsilon=%f$"%(eps))

plt.xlabel("$x \longrightarrow $")
plt.ylabel("$\delta\,(x-a)$")
plt.title("Delta function")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlim(0,2)
plt.ylim(0,120)
plt.axvline(0, c='gray',ls='--', lw=1)
plt.axhline(0, c='gray',ls=':', lw=1)
plt.legend(loc='best', fontsize=10)
plt.show()

# Verification of integration of del(x-a)g(x) for limit -inf to inf =g(a)

# Given function
def g(x):
    #return x**2
    #return np.exp(-x**2 + x + 1)
    return np.sin(x)

# evaluation of integration
xp=np.linspace(a-5.0*eps,a+5.0*eps,1000)
func=simps(g(xp)*delta(xp-a,eps),xp)

# Exact result
exact = g(a)

# Printing results
print ('calculated result =',func, 'exact value =',exact)
