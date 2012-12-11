#generate 32*32 initial planar grid

from netCDF4 import Dataset

import numpy as np
from numpy import *

grid=Dataset('firehose.nc','w')

x=grid.createDimension('x',32)
y=grid.createDimension('y',128)

grid.createVariable('nx','i4',())
grid.createVariable('ny','i4',())
grid.variables['nx'][:]=32
grid.variables['ny'][:]=128

dx=grid.createVariable('dx','f4',('x','y',))
dy=grid.createVariable('dy','f4',('x','y',))
dx[:,:]=0.05
dy[:,:]=0.05

rho=grid.createVariable('rho0','f4',('x','y',))
rho[:,:]=1.0

Pperp=grid.createVariable('Pperp0','f4',('x','y',))
Pperp[:,:]=1.0

Ppar=grid.createVariable('Ppar0','f4',('x','y',))
Ppar[:,:]=5.0

vx=grid.createVariable('v0_x','f4',('x','y',))
vy=grid.createVariable('v0_y','f4',('x','y',))
vz=grid.createVariable('v0_z','f4',('x','y',))
vx[:,:]=0.0
vy[:,:]=0.0
vz[:,:]=0.0

Bx=grid.createVariable('B0x','f4',('x','y',))
By=grid.createVariable('B0y','f4',('x','y',))
Bz=grid.createVariable('B0z','f4',('x','y',))
Bx[:,:]=0.0
By[:,:]=1.0
Bz[:,:]=0.0

grid.close()




