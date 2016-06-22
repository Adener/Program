# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 15:50:56 2016

@author: Administrator
"""

import math
import matplotlib.pyplot as plt
import numpy as np
###
GM_s=4*math.pi**2
GM_J=1.9/2000.0*GM_s
dt=0.005
end_t=1000
###
m=[]
dm=0.001
delta_a=[]
for j in range(30):
        l=0
        delta=0
        x_J=[5.200]
        v_x_J=[0]
        y_J=[0]
        v_y_J=[2.755]
        m.append(3.320+j*dm)
        x_a=[m[j]]
        v_x_a=[0]
        y_a=[0]
        v_y_a=[2*math.pi/m[j]**0.5]
        t=[0]
        ###
        ###
        for i in range(int(end_t/dt)):
                 v_x_J.append(v_x_J[i]-GM_s*x_J[i]*dt/((x_J[i]**2+y_J[i]**2)**(3.0/2.0)))
                 x_J.append(x_J[i]+v_x_J[i+1]*dt)
                 v_y_J.append(v_y_J[i]-GM_s*y_J[i]*dt/((x_J[i]**2+y_J[i]**2)**(3.0/2.0)))
                 y_J.append(y_J[i]+v_y_J[i+1]*dt)
                 v_x_a.append(v_x_a[i]-GM_s*x_a[i]*dt/((x_a[i]**2+y_a[i]**2)**(3.0/2.0))+GM_J*(x_J[i]-x_a[i])*dt/(((x_a[i]-x_J[i])**2+(y_a[i]-y_J[i])**2)**(3.0/2.0)))
                 x_a.append(x_a[i]+v_x_a[i+1]*dt)
                 v_y_a.append(v_y_a[i]-GM_s*y_a[i]*dt/((x_a[i]**2+y_a[i]**2)**(3.0/2.0))+GM_J*(y_J[i]-y_a[i])*dt/(((x_a[i]-x_J[i])**2+(y_a[i]-y_J[i])**2)**(3.0/2.0)))
                 y_a.append(y_a[i]+v_y_a[i+1]*dt)
                 delta=delta+abs(x_a[i]-x_a[0])
        delta_a.append(delta/(end_t*m[j]/dt))
        print j
###
plt.scatter(m,delta_a,marker='o',color='b',label='$\delta r-r$,$gap:1/2$')
#plt.plot(m,delta_a,'--' ,label='$\delta r-r$,$gap:1/2$')
plt.title(u'$\delta r-r$',fontsize=14)
plt.xlabel(u'$r/AU$',fontsize=14)
plt.ylabel(u'$\delta r/AU$',fontsize=14)
plt.legend(fontsize=12,loc='best')
plt.savefig("12.2.png")
plt.show()