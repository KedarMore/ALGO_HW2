from sympy import Point, Polygon, plot_implicit
import math
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np

a0=float(imput("\nEnter the Length of first link: "))
a1=float(imput("\nEnter the Length of second link: "))

# obstacles=(Polygon((0.25, 0.25), (0, 0.75), (-0.25, 0.25)),)

# obstacles=(Polygon((-0.25, 1.1), (-0.25, 2), (0.25, 2), (0.25, 1.1)),
#            Polygon((-2, -2), (-2, -1.8), (2, -1.8), (2,-2)))

# obstacles=(Polygon((-0.25, 1.1), (-0.25, 2), (0.25, 2), (0.25, 1.1)),
#            Polygon((-2, -0.5), (-2, -0.3), (2, -0.3), (2,-0.5)))

v=[]

noofobstacles=int(input("\nNumber of Obstacles?"))
for i in range(noofobstacles):
    v1=[]
    vertex=int(input("\nNumber of Vertices on obstacle "+str(i+1)+"?"))
    for j in range(vertex):
        v2=[]
        v2.append(float(input("\nx Coordinates of vertex "+str(j+1)+"?")))
        v2.append(float(input("\ny Coordinates of vertex "+str(j+1)+"?")))
        v1.append(v2)
        pass
    v.append(v1)
    pass
print(v)
inside=[]
obstacles=[]
coor=[]
ax=plt.subplot(1,2,1)
for i in range(noofobstacles):
    inside=[]
    coor=[]
    for j in range(vertex):
        inside.append((v[i][j][0],v[i][j][1]))
        coor.append((v[i][j][0],v[i][j][1]))
        pass
    poly=Polygon(*inside)
    obstacles.append(poly)
    coor=np.transpose(coor)
    ax.plot(coor[0],coor[1])
    ax.fill(coor[0],coor[1])
    pass
obstacles=tuple(obstacles)
plt.title("Obstacles")
plt.xlabel("X")
plt.ylabel("Y")
print(obstacles)

ay=plt.subplot(1,2,2)
p0=(0,0)
m1=30
m2=30
pointsx=[]
pointsy=[]
for theta1 in tqdm(range(int(360/m1)+1)):
    # print(theta1)
    for theta2 in tqdm(range(int(360/m2)+1)):
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
                    # ay.plot(theta1*m1,theta2*m2,'ko')
                    pointsx.append(theta1*m1)
                    pointsy.append(theta2*m2)
                    pass
                pass
            pass
        pass
    pass
# pointsx()
for x in range(len(pointsx)-1):
    dist=math.sqrt((pointsx[x]-pointsx[x+1])**2+(pointsy[x]-pointsy[x+1])**2)
    if dist==int(m1):
        ay.plot((pointsx[x],pointsx[x+1]),(pointsy[x],pointsy[x+1]),'k-')
        pass
    pass
new=sorted(zip(pointsy,pointsx))
points=np.array(new)
# print(points)
points=np.transpose(points)
pointsx=points[1]
pointsy=points[0]
for x in range(len(pointsx)-1):
    dist=math.sqrt((pointsx[x]-pointsx[x+1])**2+(pointsy[x]-pointsy[x+1])**2)
    if dist==int(m1):
        ay.plot((pointsx[x],pointsx[x+1]),(pointsy[x],pointsy[x+1]),'k-')
        pass
    pass
ay.plot(pointsx,pointsy,'ko')
plt.xlim(0,360)
plt.ylim(0,360)
plt.title("C-Space")
plt.xlabel("Theta 1")
plt.ylabel("Theta 2")
plt.show()