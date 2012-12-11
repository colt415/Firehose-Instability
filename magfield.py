from boutdata import collect

import numpy as np
from numpy import *

Bx=collect('Bx',path='/home/colt/Research/BOUT/examples/Firehose/data')

import matplotlib.pyplot as plt
from matplotlib import *

xlen=32
ylen=128
Bxdata=zeros([ylen,xlen])
Bjdata=zeros(ylen)
Bfield=zeros([2,ylen])
dely=0.05
delx=0.05

plt.figure()

for i in range(4):
  Bxdata=Bx[7*i,:,:,1]
  plt.subplot(2,2,i+1)
  for j in range(8):
    Bjdata=Bxdata[4*j,:]
    Bfield[0,0]=4*j*delx
    Bfield[1,0]=0
    for k in range(ylen-1):
      Bfield[0,k+1]=Bfield[0,k]+Bjdata[k]*delx/(Bjdata[k]**2+1)**2
      Bfield[1,k+1]=Bfield[1,k]+dely/(Bjdata[k]**2+1)**2
      
    plt.plot(Bfield[1,:],Bfield[0,:],'b',linewidth=1.5)
    
  plt.grid(True)
  plt.title(r'Magnetic field line, t= '+ str(7*i) +r'/100 s, $\beta_{par}-\beta{\perp}=4.0$,$m=8$,$\delta B/B=0.1$',fontsize=15)
  plt.xlabel(r'y')
  plt.ylabel(r'x')
  plt.ylim([0.1,1.3])
  plt.xlim([0.0,6.0])

plt.show()

#the rest program check the divergence of B
"""
tlen=61
t=linspace(0,0.6,tlen)
divB=zeros(tlen)
for i in range(tlen):
  for j in range(xlen-1):
    for k in range(ylen-1):
      divB[i]=divB[i]+(Bx[i,j+1,k,1]-Bx[i,j,k,1])/delx


plt.figure()
plt.plot(t,divB[:],linewidth=1.5)
plt.ylim([-1e-7,1e-7])
plt.show()
"""
    
    
