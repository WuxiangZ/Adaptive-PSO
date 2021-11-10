#------------------------------------------------------------------------------+
#
#	wuxiang Z.OUC 

#	自适应权重调整PSO
#	Last update: 2021-Nov-11
	#拷贝源：https://github.com/nathanrooy/particle-swarm-optimization
#	Python 3.8
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from random import random
from random import uniform
import matplotlib.pyplot as plt

#--- MAIN ---------------------------------------------------------------------+

class Particle:
    def __init__(self, x0):
        self.position_i=[]          # particle position
        self.velocity_i=[]          # particle velocity
        self.pos_best_i=[]          # best position individual
        self.err_best_i=-1          # best error individual
        self.err_i=-1               # error individual

        for i in range(0,num_dimensions):
            self.velocity_i.append(uniform(-1,1))
            self.position_i.append(x0[i])

    # evaluate current fitness
    def evaluate(self,costFunc):
        self.err_i=costFunc(self.position_i)

        # check to see if the current position is an individual best
        if self.err_i<self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.position_i.copy()
            self.err_best_i=self.err_i
                    
    # update new particle velocity
    def update_velocity(self,pos_best_g,w):
        # w=0.8      # constant inertia weight (how much to weigh the previous velocity)
        c1=2.0        # cognative constant
        c2=2.0     # social constant
        
        for i in range(0,num_dimensions):
            r1=random()
            r2=random()
            
            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social

    # update the particle position based off new velocity updates
    def update_position(self,bounds):
        for i in range(0,num_dimensions):
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]
            
            # adjust maximum position if necessary
            if self.position_i[i]>bounds[i][1]:
                self.position_i[i]=bounds[i][1]

            # adjust minimum position if neseccary
            if self.position_i[i]<bounds[i][0]:
                self.position_i[i]=bounds[i][0]
        
        

def minimize(costFunc, x0, bounds, num_particles, maxiter, verbose=False):
    global num_dimensions

    num_dimensions=len(x0)
    err_best_g=-1                   # best error for group
    pos_best_g=[]                   # best position for group
    # establish the swarm
    swarm=[]
    for i in range(0,num_particles):
        swarm.append(Particle(x0))

    # begin optimization loop
    i=0
    solus = []
    while i<maxiter:
        if verbose: print(f'iter: {i:>4d}, best solution: {err_best_g:10.6f}')
            
        # cycle through particles in swarm and evaluate fitness
        for j in range(0,num_particles):
            swarm[j].evaluate(costFunc)

            # determine if current particle is the best (globally)
            if swarm[j].err_i<err_best_g or err_best_g==-1:
                pos_best_g=list(swarm[j].position_i)
                err_best_g=float(swarm[j].err_i)
        
        w = 0.8
        # wlist = []
        w_min = 0.4
        w_max = 0.8
        # cycle through swarm and update velocities and position
        fitness_total = []
        fitness_sum = 0
        fitness_max = 0
        for j in range(0,num_particles):
            fitness_total.append(swarm[j].position_i) #将历史适应度值加入列表
            fitness_j = costFunc(swarm[j].position_i)  #计算当前适应度值
            fitness_sum +=fitness_j   #计算当前适应度值总和
            if fitness_max<fitness_j:
                fitness_max = fitness_j    #记录目前适应度值最大值
            if j!=0:
                fitness_avg = fitness_sum/j  #计算当前avg适应度值
                if fitness_j>=fitness_avg:
                    if fitness_avg != fitness_max:
                        w = w_min + (w_max - w_min)*(fitness_max - fitness_j)/(fitness_max - fitness_avg)
                    else:  #调整w
                        w = w_max
                else:
                    w = w_max
            # wlist.append(w)
            
            swarm[j].update_velocity(pos_best_g,w)  #更新速度
            swarm[j].update_position(bounds)       #更新位置
            
        solus.append(err_best_g)
#选择20、50代观察w变化
        # if i==20:
        #     wlist1 = wlist
        # if i==50:
        #     wlist2 = wlist
        i+=1

    # print final results
    if verbose:
        # print('\nFINAL SOLUTION:')
        # print(f'   > {pos_best_g}')
        print(f'   > {err_best_g}\n')
        

    return err_best_g, pos_best_g

#--- END ----------------------------------------------------------------------+
