#verification of BOUT++ code and linear theory on Firehose instability

import matplotlib.pyplot as plt
from matplotlib import *

import numpy as np
from numpy import *

m=linspace(6,12,7)
L=6.4
wavelength=L/m
k=2*pi/wavelength
gammatheory=k
gammasimul=[5.91,6.85,7.78,9.20,9.88,10.82,11.70]

plt.figure()
plt.subplot(1,2,1)
plt.plot(m,gammatheory,'b',m,gammasimul,'rd',linewidth=1.5)
plt.legend((r'Theory',r'Simulation'),'best',shadow=True)
plt.title(r'Dispersion relation of firehose instability,$\beta_{par}-\beta_\perp=4.0$',fontsize=15)
plt.xlabel(r'm',fontsize=18)
plt.ylabel(r'$\gamma(v_A/a)$',fontsize=18)
plt.xlim([5,13])
plt.ylim([5,13])
plt.grid(True)

omegatheory=k/sqrt(2)
omegasimul=[4.16,4.84,5.52,6.15,6.90,7.60,8.16]
plt.subplot(1,2,2)
plt.plot(m,omegatheory,'b',m,omegasimul,'rd',linewidth=1.5)
plt.legend((r'Theory',r'Simulation'),'best',shadow=True)
plt.title(r'Dispersion relation of firehose instability,$\beta_{par}-\beta_\perp=1.0$',fontsize=15)
plt.xlabel(r'm',fontsize=18)
plt.ylabel(r'$\omega(v_A/a)$',fontsize=18)
plt.xlim([5,13])
plt.ylim([3,10])
plt.grid(True)

plt.figure()
ratio=[2.5,3,3.5,4,4.5,5]
betadiff=[3,4,5,6,7,8]
ratio1=np.arange(2.0,6.0,0.1)
betadiff1=ratio1*2-2.0
k1=7.85
gammatheory1=sqrt(ratio1-2)*k1
gammasimul1=[5.64,7.78,9.69,11.18,12.49,13.68]
plt.plot(betadiff1,gammatheory1,'b',betadiff,gammasimul1,'rd',linewidth=1.5)
plt.legend((r'Theory',r'Simulation'),'best',shadow=True)
plt.title(r'Dispersion relation of firehose instability,$m=8$',fontsize=15)
plt.xlabel(r'$\beta_{par}-\beta_\perp$',fontsize=18)
plt.ylabel(r'$\gamma(v_A/a)$',fontsize=18)
plt.xlim([2,10])
plt.ylim([0,15])
plt.grid(True)

plt.show()
