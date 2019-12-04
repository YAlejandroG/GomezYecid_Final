import numpy as np
import matplotlib.pylab as plt

data = np.loadtxt('monthrg.dat')

tiempo = data[:,0]
manchas = data[:,3]

tiempo = tiempo[3480:]
manchas = manchas[3480:]

def fourier(signal):
    N = len(signal)
    Fo = []
    for n in range(N):
        fo = np.complex(0,0)
        for k in range(N):
            exp = np.complex(0,2*np.pi*n*k/N)
            fo += signal[k]*np.exp(-exp)
        fo = np.sqrt(fo.imag**2+fo.real**2)/N
        if fo<0.3:
            fo = 0
        Fo.append(fo)
    return np.array(Fo)[1]

T = fourier(manchas)
print('Periodo de la variacion: ',T,' años')

t = np.linspace(0,tiempo.max()-tiempo.min(),200)
onda = manchas.mean()*np.cos(2*np.pi*t/T)+manchas.mean()

plt.figure(figsize=(10,5))
plt.scatter(tiempo,manchas,s=5,c='k')
plt.plot(t+tiempo.min(),onda,c='g')
plt.savefig('solar.png')