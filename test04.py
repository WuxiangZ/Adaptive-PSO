import pso_simple_ts as pso_simple
import math
initial = [600, 600, -400]        # initial starting location [x1,x2...]
# input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
bounds = [(501, 1000), (200, 1000), (-500, -100)]

def arctan(deg):
    return 180/math.pi*math.atan(deg)

def arccot(deg):
    return 180/math.pi*(math.pi/2-math.atan(deg))

def fitness(lis):
    x,y,z = lis[0], lis[1],lis[2]
    # a:方位角 b:俯仰角
    # node1(0,0,-50)
    a1 = (arctan(y/x)-45.4)**2
    b1 = (arccot((math.sqrt(x**2+y**2)/abs(z+50))) -7.5523)**2
    # node2(250,250*sqrt(3),-50)
    a2 = (arctan((y-250*math.sqrt(3))/(x-250)) -33.713)**2
    b2 = (arccot((math.sqrt((x-250)**2+(y-math.sqrt(3)*250)**2)/abs(z+50))) -12.78187)**2
    # node3(500,0,-50)
    a3 = (arctan(y/(x-500))-69.4439)**2
    b3 = (arccot((math.sqrt((x-500)**2+y**2)/abs(z+50)))-9.9574)**2
    return a1+a2+a3+b1+b2+b3

maxiter = 100  #最大迭代次数
num_particles=200  #随机粒子个数
err_best_g, pos_best_g = pso_simple.minimize(fitness, initial, bounds, num_particles=num_particles,
                                            maxiter=maxiter, verbose=True)
deviation = math.sqrt((800-pos_best_g[0])**2+(800-pos_best_g[1])**2+(-200-pos_best_g[2])**2)
                    #true position（800,800，-200）
    
print("Final deviation:")
print(err_best_g)
print(pos_best_g)
print(deviation)

# 改进算法
# Final deviation:
# 0.16836812046971786
# [796.7647544920934, 797.2894872813255, -199.54955460700853]
