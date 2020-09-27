import multiprocessing
from sympy import Point, Polygon
import math
import matplotlib.pyplot as plt

a0=1
a1=1

obstacles=(Polygon((-0.25, 1.1), (-0.25, 2), (0.25, 2), (0.25, 1.1)),
           Polygon((-2, -2), (-2, -1.8), (2, -1.8), (2,-2)))

p0=(0,0)
m1=10
m2=10
points=[]

def sum_up_to(theta1):
    for theta2 in range(int(360/m2)):
        p1=((a0*(math.cos(theta1*m1))),
            (a0*(math.sin(theta1*m1))))
        p2=((a0*(math.cos(theta1*m1))+a1*(math.cos(theta1*m1+theta2*m2))),
            (a0*(math.sin(theta1*m1))+a1*(math.sin(theta1*m1+theta2*m2))))
        links=(Polygon(p0,p1),Polygon(p1,p2))
        print(theta1,theta2)
        for obstacle in obstacles:
            for link in links:
                if len(link.intersection(obstacle))!=0:
                    # plt.plot(theta1*m1,theta2*m2,'ko')
                    points.append((theta1,theta2))
                    pass
                pass
            pass
    return points


a_pool = multiprocessing.Pool()


p=a_pool.map(sum_up_to,range(int(360/m1))) #518400


# plt.show()
print(p)
# plt.show()