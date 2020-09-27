import math
import matplotlib.pyplot as plt
import numpy as np
# from threedplot import rotate

def leastY(listofpoints):
    """
    docstring
    """
    checkallx=[]
    for i in listofpoints:
        checkallx.append(i[0])
    minx=min(checkallx)
    xindex=checkallx.index(minx)
    listofpoints=np.roll(listofpoints,-xindex,axis=0)
    checkally=[]
    for i in listofpoints:
        checkally.append(i[1])
    miny=min(checkally)
    yindex=checkally.index(miny)
    listofpoints=np.roll(listofpoints,-yindex,axis=0)
    return listofpoints

def Cspace(obstacle,robot):
    """
    docstring
    """
    i=0
    j=0
    finalx=[]
    finaly=[]
    v=obstacle
    w=robot
    while i<len(v) and j<len(w):
        finalx.append(v[i][0]+w[j][0])
        finaly.append(v[i][1]+w[j][1])
        if i==(len(v)-1):
            j=j+1
            continue
        elif j==(len(w)-1):
            i=i+1
            continue
        anglev=math.degrees(math.atan2((v[i+1][1]-v[i][1]),(v[i+1][0]-v[i][0])))
        anglew=math.degrees(math.atan2((w[j+1][1]-w[j][1]),(w[j+1][0]-w[j][0])))
        if anglev<0:
            anglev=360+anglev
            pass
        if anglew<0:
            anglew=360+anglew
            pass
        # print("angle= ")
        # print(anglev,anglew)
        if anglev<anglew:
            i=i+1
            pass
        elif anglev>anglew:
            j=j+1
            pass
        else:
            i=i+1
            j=j+1
            pass
        pass
    # print(finalx,finaly)
    # plt.fill(finalx,finaly)
    # plt.show()
    return np.vstack((finalx,finaly))

if __name__ == "__main__":
    v=np.array(((0,0),(1,2),(0,2)))
    w=np.array(((-1,-2),(0,-2),(0,0)))
    # w=np.array(((-2,-3),(-1,-3),(-1,-1)))
    v=np.vstack((v,v[0]))
    w=np.vstack((w,w[0]))
    # w=np.hstack((w,np.ones((len(w),1))))
    # w=rotate(v,np.transpose(w),20*0.0174)
    final=Cspace(v,w)
    plt.fill(final[0],final[1])
    plt.show()
    # print(leastY(((1,2),(-1,3),(3,-2))))