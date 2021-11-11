# Adaptive-PSO

## Theory

**PSO CODE Source From https://github.com/nathanrooy/particle-swarm-optimization** 

​		在基本粒子群算法的迭代公式惯性权重w是定值，但随着迭代次数的增加，问题的求解细节也会有所改变，固定值在整体求解的过程中存在不少缺陷。因而，引入变动的惯性权重，以动态适应问题的求解流程。

+ 一个较大的惯性权重w有利于全局搜索 

+ 一个较小的惯性权重w有利于局部搜索

+ 适应度越小，说明距离最优解越近，此时更需要局部搜索

+ 适应度越大，说明距离最优解越远，此时更需要全局搜索 


  **w 变化公式：**
  ![image](https://user-images.githubusercontent.com/62392713/141245569-1a373d04-eb1e-46b0-9e09-e1abc8d686d9.png)

## Usage

​		如果您是用来测试算法，那可以自己设计适应度函数以及配置参数，可以直接参考 https://img.shields.io/github/workflow/status/nathanrooy/particle-swarm-optimization

**	test04.py**致力于利用多点**DOA**估计得到角度值以及探测阵列源自身的位置坐标联合求解探测目标的三维坐标位置

已知三阵源位置：

+ node1  **坐标(0,0,-50)   DOA估计角度为（45.4，97.5523）**
+ node2 **(250,250\*sqrt(3),-50)  （33.713，102.78）**
+ node3 **(500,0,-50) （69.4439，99.9574）**

**探测目标位置（800,800，-200）**则定义适应度函数如下

```Python
def fitness(lis:list): 
	#优化函数函数体
    #未知数个数对应lis长度
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
```

##  end

如果还有机会的话，还会 git DOA算法，以及设计好DOA与PSO的接口
