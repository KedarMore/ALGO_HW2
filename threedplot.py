import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from minkowski import Cspace #2D
from minkowski import leastY
import math

def rotate(obstacle,robot,angle):
    """
    docstring
    """
    xtotal=0
    ytotal=0
    for i in range(len(robot)):
        xtotal=xtotal+robot[0][i]
        ytotal=ytotal+robot[1][i]
        pass
    # centroid=((xtotal/(len(robot))),(ytotal/(len(robot))))
    centroid=(-0.5,-1)
    T1=[(1,0,-centroid[0]),
        (0,1,-centroid[1]),
        (0,0,1)]
    R=[(math.cos(angle),-math.sin(angle),0),
       (math.sin(angle),math.cos(angle),0),
       (0,0,1)]
    T2=[(1,0,centroid[0]),
        (0,1,centroid[1]),
        (0,0,1)]
    # robot=T2*R*T1*robot
    robot=np.matmul(T2,np.matmul(R,np.matmul(T1,robot)))
    print(robot)
    # robot=np.matmul(R,robot)
    # robot=mirror(centroid,robot) #mirror
    # dist=[]
    # for i in range(len(robot)):
    #     dist.append(math.sqrt((robot[0][i])**2 + (robot[1][i])**2))
    # print(dist)
    # mindist=min(dist)
    # ind=dist.index(mindist)
    # T=[(1,0,-robot[0][ind]),
    #    (0,1,-robot[1][ind]),
    #    (0,0,1)]
    # robot=np.matmul(T,robot)
    # print(robot)
    return robot

def mirror(centroid,robot):
    """
    docstring
    """
    a=centroid[1]/centroid[0]
    # a=10
    b=-1
    c=0
    x=[]
    y=[]
    for i in range(len(robot)):
        temp = -2 * (a * robot[i][0] + b * robot[i][1] + c) /(a * a + b * b) 
        x.append(temp * a +  robot[i][0])
        y.append(temp * b + robot[i][1])
        pass
    ans=np.vstack((np.transpose(x),np.transpose(y),np.ones((1,len(x)))))
    ans=np.fliplr(ans)
    return ans

# zoff=1
# v=np.array(((0,0),(1,2),(0,2)))
# w=np.array(((-1,-2),(0,-2),(0,0)))
# v=np.vstack((v,v[0]))
# w=np.vstack((w,w[0]))
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# for i in range(360):
#     l=Cspace(v,w)
#     z=(np.ones((len(l[0]))))*zoff
#     zoff=zoff+0.1
#     ax.plot_trisurf(l[0],l[1],z)
# plt.show()

if __name__ == "__main__":
    zoff=1
    v=np.array(((0,0),(1,2),(0,2))) #obstacle
    v=np.vstack((v,v[0]))
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for angle in range(360):
        w=np.array(((-1,-2),(0,-2),(0,0))) #robot intial
        # w=np.array(((-1,0),(-1,-2),(0,0)))
        w=np.vstack((w,w[0]))
        w=np.hstack((w,np.ones((len(w),1)))) #add column

        w=rotate(v,np.transpose(w),np.radians(angle)) #rotate
        # print(np.transpose(w))
        w=leastY(np.transpose(w)) #roll
        l=Cspace(v,w)
        # print(l)
        z=(np.ones((len(l[0]))))*zoff
        zoff=zoff+1
        ax.plot_trisurf(l[0],l[1],z,alpha=0.1,color='black')
    plt.show()
    # print(mirror((-1,-2),np.array(((0,0),(-1,0),(-1,-2)))))
    pass