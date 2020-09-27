from sympy import Point, Polygon
import math
import matplotlib.pyplot as plt
from tqdm import tqdm

a0=1.2
a1=1

# obstacles=(Polygon((-0.25, 1.1), (-0.25, 2), (0.25, 2), (0.25, 1.1)),
#            Polygon((-2, -2), (-2, -1.8), (2, -1.8), (2,-2)))

obstacles=(Polygon((-0.25, 1.1), (-0.25, 2), (0.25, 2), (0.25, 1.1)),)

# links=(Polygon(p0,p1),Polygon(p1,p2))

p0=(0,0)

m1=1
m2=1

check=[]
for theta1 in range(int(360/m1)):
    p1=((a0*(math.cos(theta1*m1))),
        (a0*(math.sin(theta1*m1))))
    links=(Polygon(p0,p1))
    for obstacle in obstacles:
        if len(links.intersection(obstacle))!=0:
            check.append(theta1)
            print(theta1)
            pass
        pass
    pass
print(check)