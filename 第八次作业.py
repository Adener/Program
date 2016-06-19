from pylab import *
import sys
reload(sys)
sys.setdefaultencoding('gb18030')



class Harmonic(object):
    def __init__(self,_t, _omega, _theta, alpha= 3,k=1,_dt=0.5):
        self.t=[_t]
        self.k=1
        self.alpha=3
        self.omega=[_omega]
        self.theta=[q]
        self.end_time=100
        self.dt=_dt
    def calculate(self):
        for i in range(int(self.end_time/self.dt)):
        	self.omega.append(self.omega[i] -self.k  * self.theta[i]**self.alpha  * self.dt)
        	self.theta.append(self.theta[i] +  self.omega[i+1]  * self.dt)
        	self.t.append(self.dt*(i+1))
   

for q in (0.1,0.2,0.5):
    trejectory = Harmonic(0,0.01,_theta=q)
    trejectory.calculate()
    print trejectory.t[-1], trejectory.theta[-1]
    plot(trejectory.t,trejectory.theta, linestyle='-',label ="$\\theta_0$=" +str(q))
xlabel('time(s)')
ylabel('$\\theta$(rad)')
title('$\\theta-t$')
legend(loc="upper right")
show()

