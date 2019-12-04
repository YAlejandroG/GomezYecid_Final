import numpy as np
import matplotlib.pyplot as plt

U = np.loadtxt("Ejercicio17.dat")

plt.figure()

time = np.linspace(0,0.5,np.shape(U)[0])
x = np.linspace(0,2,np.shape(U)[1])

plt.plot(x,U[0,:],label='t = 0')
plt.plot(x,U[-1,:],label='t = 0.5')
    
plt.grid()
plt.legend()
plt.xlabel('X (m)')
plt.ylabel('U')

plt.savefig("resultado.png")