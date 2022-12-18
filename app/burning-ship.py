import numpy as np
import matplotlib.pyplot as plt
from numba import jit


@jit
def burning_calc(imag, Nx, Ny, xmin, xmax, ymin, ymax, max_iteration):

    x=np.linspace(xmin, xmax, Nx)
    y=np.linspace(ymin, ymax, Ny)

    for i in range(Nx):
        for j in range(Ny):
            iteration=0
            c=x[i]+1j*y[j]
            z=0+0j
            while z.real**2+z.imag**2<4 and iteration < max_iteration:
                z=(abs(z.real)+1j*abs(z.imag))**2+c
                iteration=iteration+1
            imag[j][i]=np.log(iteration)

Nx=2000
Ny=2000
max_iteration=1000
imag=np.zeros((Nx, Ny))
xmax=-1.7
xmin=-1.8
ymax=0.02
ymin=-0.1
burning_calc(imag, Nx, Ny, xmin, xmax, ymin, ymax, max_iteration)
plt.figure(figsize=(15, 15))
plt.imshow(imag, extent=(xmin, xmax, ymin, ymax), cmap=plt.cm.afmhot)
# plt.colorbar()
plt.show()
