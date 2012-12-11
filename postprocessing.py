#post precessing for firehose instability
#from boutdata import *
#from boututils import *
from boutdata import collect

#vx=collect('v_x',path='/home/colt/Research/BOUT/examples/Firehose/data')
#N=collect('density',path='/home/colt/Research/BOUT/examples/Firehose/data/neumann')
Bx=collect('Bx',path='/home/colt/Research/BOUT/examples/Firehose/data')
#Pperp=collect('perppressure',path='/home/colt/Research/BOUT/examples/Firehose/data')
import matplotlib.pyplot as plt
from matplotlib import *

import numpy as np
from numpy import *

#x=linspace(0,6.3,64)
#y=linspace(0,6.3,64)

x=linspace(0,1.55,32)
y=linspace(0,6.35,128)

[X,Y]=meshgrid(x,y)
print X.shape
print Y.shape
#print N[90,8:58,8:58,1].shape
plt.figure()
CS=plt.contourf(X,Y,Bx[200,:,:,1].T,20)
CB=plt.colorbar(CS,shrink=0.8,extend='both')
plt.title(r'$\delta B/B_0$, at $t=0$,$m=8$',fontsize=18)
plt.xlabel(r'x',fontsize=15)
plt.ylabel(r'y',fontsize=15)
plt.show()

from scipy import stats
t=linspace(0,0.2,201)
#t=linspace(0,0.50,51)
"""
logBx=log(Bx[10:41,24,16,1]/Bx[0,24,16,1])
slope, intercept, r_value, p_value, std_err = stats.linregress(t,logBx)
print slope
print intercept
print r_value
"""
ypos=52
delt=0.001
gamma=0.0
for i in range(9):
  A=Bx[i+10,16,ypos,1]/Bx[0,16,ypos,1]
  B=log(A+(A**2-1)**0.5)/((i+10)*delt)
#  B=arccos(A)/((i+10)*delt)
  print B
  gamma=gamma+B

gamma=gamma/(i+1)
print gamma


plt.figure()
plt.plot(t,Bx[0:201,16,ypos,1],linewidth=1.5)
plt.title(r'$x=0.8, y=2.5$,$\delta B(t=0)/B_0=0.01$, m=8',fontsize=18)
plt.xlabel(r'$t(a/v_A)$',fontsize=15)
plt.ylabel(r'$\delta B/B_0$',fontsize=15)
plt.grid(True)
#plt.plot(t,logBx,'rd',t,intercept+slope*t,linewidth=1.5)
plt.show()
