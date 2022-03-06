"""
Registration : 012-1111-0461-20
Roll         : 203012-21-0008 
Description  : Dirac Delta Functions
Author       : Chitrak Roychowdhury
"""


#Dirac Delta Function
#Representation using Limit of Sequence of Rectangles
#\epsilon ---> 0
#func = 0          for x > \epsilon/2
#     = 1/\epsilon for (-\epsilon/2)< x < (\epsilon/2)      
#     = 0          for x < (-\epsilon/2)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

a = 1.0 #peak position of delta function
x1 = a-0.1; x2 = a+0.1 #x-range for plotting peak of delta func

#determining delta function by rectangle
def ddf(x,eps):
    if(-eps/2.0 < x and x < eps/2):
        val=1.0/eps
    else:
        val=0
    return val
ddf=np.vectorize(ddf)
print("Representation of Delta Function Limit of sequence of Rectangles")

#Plot
eps=0.1
x=np.linspace(x1,x2,1000)
s=np.arange(1,5)
for i in s:
    eps=eps/i
    plt.plot(x,ddf(x-a,eps),ls="solid",lw="2",label='$\epsilon=%f$'%(eps))

plt.xlabel("$x \longrightarrow$")
plt.ylabel ("$\delta(x-a)$")
plt.title("Delta Function")
plt.legend(loc="best")
plt.grid(True)
plt.xlim(0,2)
plt.ylim(0,250)
plt.xticks()
plt.yticks()
plt.axvline(0, c='gray',ls='--', lw=1)
plt.axhline(0, c='gray',ls=':', lw=1)
plt.show()

#verification of intrgration of del(x-a)g(x) for limit -inf to +inf = g(a)

#function given
g = lambda x: x**2

#evaluating intrgral
x = np.linspace(a-eps,a+eps,1000)
I = simps(g(x)*ddf(x-a,eps),x)

#Exact result
exact = g(a)

#Print
print("Calculated Result",I, "Exact Value",exact)
