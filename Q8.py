# theta1 is wrt ground
# theta2 is wrt a1
# a0 is length of first link
# a1 is length of second link

from sympy import Point, Polygon
import math
import matplotlib.pyplot as plt
from tqdm import tqdm

a0=1
a1=1

# obstacles=(Polygon((0.25, 0.25), (0, 0.75), (-0.25, 0.25)),)

# obstacles=(Polygon((-0.25, 1.1), (-0.25, 2), (0.25, 2), (0.25, 1.1)),
#            Polygon((-2, -2), (-2, -1.8), (2, -1.8), (2,-2)))

obstacles=(Polygon((-0.25, 1.1), (-0.25, 2), (0.25, 2), (0.25, 1.1)),
           Polygon((-2, -0.5), (-2, -0.3), (2, -0.3), (2,-0.5)))

p0=(0,0)
m1=20
m2=20
points=[]
for theta1 in tqdm(range(int(360/m1))):
    # print(theta1)
    for theta2 in range(int(360/m2)):
        p1=((a0*(math.cos(math.radians(theta1*m1)))),
            (a0*(math.sin(math.radians(theta1*m1)))))
        p2=((a0*(math.cos(math.radians(theta1*m1)))+a1*(math.cos(math.radians(theta1*m1)+math.radians(theta2*m2)))),
            (a0*(math.sin(math.radians(theta1*m1)))+a1*(math.sin(math.radians(theta1*m1)+math.radians(theta2*m2)))))
        links=(Polygon(p0,p1),Polygon(p1,p2))
        intersect=0
        # print(theta1,theta2)
        for obstacle in obstacles:
            for link in links:
                if len(link.intersection(obstacle))!=0:
                    intersect=1
                    plt.plot(theta1*m1,theta2*m2,'ko')
                    points.append((theta1*m1,theta2*m2))
                    pass
                pass
            pass
        pass
    pass
# print(points)
plt.show()