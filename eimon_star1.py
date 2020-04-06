get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pylab as plt

def gasket(pa, pb, pc, level, col):
    if level == 0:
        plt.fill([pa[0], pb[0], pc[0]], [pa[1], pb[1], pc[1]], col) 
        plt.hold(True)
    else:
        gasket(pa, (pa + pb) / 2., (pa + pc) / 2., level - 1, col) 
        gasket(pb, (pb + pa) / 2., (pb + pc) / 2., level - 1, col) 
        gasket(pc, (pc + pa) / 2., (pc + pb) / 2., level - 1, col)
        
        
A = np.array([-0.069332,28.001]) 
B = np.array([29.211,7.1528])
C = np.array([18.431,-27.138])
D = np.array([-17.51,-27.484]) 
E = np.array([-28.943,6.6004]) 

L = np.array([-6.8546,6.6731]) #np.array([-6.9,6.8])
K = np.array([6.9089,6.9188]) #np.array([7,6.9])
M = np.array([11.398,-6.099]) #np.array([11.4,-6.1])
N = np.array([0.40442,-14.388]) #np.array([0.35,-14.3])
O = np.array([-10.876,-6.4956]) #np.array([-10.85,-6.7])

level = 4
gasket(A, L, K, level, "r")
gasket(B, K, M, level, "r")
gasket(C, M, N, level, "r")
gasket(D, N, O, level, "r")
gasket(E, O, L, level, "r")
plt.fill([L[0],K[0],M[0],N[0],O[0]],[L[1],K[1],M[1],N[1],O[1]],'w')
plt.hold(False)
plt.title("LV.4")
plt.axis('equal')