
# In[8]:


import powerlaw
import math
import matplotlib.pyplot as plt
from matplotlib.pylab import plot
import numpy as np
import idlsave
import statistics as stats

# In[9]:

z = np.zeros((19,10000))

for p in range(0,19):
    file = 'zk'+str(10*p+10)+'mil.sav'
    s = idlsave.read(file)
    b = s['zk'+str(10*p+10)+'mil']
    for i in range(len(b)-1):
        a=np.array(b[i])
        for j in range(len(a[0])): 
            for k in range(len(a[1])):
                if 0.20<abs(a[j,k])<0.25:
                    z[p][i]=z[p][i]+1
           
'''
np.concatenate((a, b), axis=None)

zff = z[0]/4096                
plt.plot(zff[36449:39357])
plt.show()
mean(zff)
print(stats.mean(zff))
print(stats.pvariance(zff))
max(zff)
'''