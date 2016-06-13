def v(t,dt):
    v = [0 for i in range(int(t/dt+1))]
    g = -9.8
    for i in range(int(t/dt)):
        v[i+1] = v[i] + g*dt
    return v

v_n = v(10,0.1)
t_n = [0.1*i for i in range(101)]

import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8,6))

plt.scatter(t_n,v_n,s=5,color='blue',label='numerial')

t_e = np.linspace(0,10,101,endpoint=True)
v_e = -9.8 * t_e
plt.plot(t_e,v_e,color='red',label='exact')

plt.xticks(np.linspace(0,10,11,endpoint=True))
plt.yticks(np.linspace(-100,0,11,endpoint=True))
plt.xlabel('t/s')
plt.ylabel('v/(m/s)')
plt.legend(loc='upper left',frameon=True)
plt.savefig('ex1.png')
plt.show()

