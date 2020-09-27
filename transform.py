import math
import numpy as np
import matplotlib.pyplot as plt

w=np.array(((-1,-2),(0,-2),(0,0),(-1,-2)))
one=np.ones((len(w),1))
w=np.hstack((w,one))
print(w)

theta=0.1
rMatrix=[(math.cos(theta),-math.sin(theta),0),(math.sin(theta),math.cos(theta),0),(0,0,1)]

x=np.matmul(rMatrix,np.transpose(w))

x=x[:-1,:]
print(x)
plt.plot(w.T[0],w.T[1])
plt.plot(x[0],x[1])
plt.show()