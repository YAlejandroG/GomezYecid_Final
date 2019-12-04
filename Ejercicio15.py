import numpy as np
import matplotlib.pylab as plt

xk = np.loadtxt('valores.txt')

def Probabilidad(xk,sigma):
    p = 1
    for x in xk:
        p *= np.exp(-x**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))
    return p/9

MH = [np.random.random()]

for i in range(10**5):
    mh = MH[-1]+np.random.random()-0.5
    
    if Probabilidad(xk,MH[-1])==0:
        r = 1
    else:
        r = min(1,Probabilidad(xk,mh)/Probabilidad(xk,MH[-1]))
    a = np.random.random()
    
    if a<r:
        MH.append(mh)
    else:
        MH.append(MH[-1])

MH = np.array(MH)
prom = np.round(MH.mean(),3)
desv = np.round(MH.std(),3)

plt.figure()
plt.hist(MH,density=True,bins=50,color='g')
plt.ylabel('P({xk}|$\sigma$)*P($\sigma$)')
plt.xlabel('$\sigma$')
plt.title('$\sigma_{prom}$ = '+str(prom)+', $\sigma_{desv}$ = '+str(desv))
plt.savefig('sigma.png')