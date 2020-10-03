# check if the links can be overlapping

import math
from Q7a import plot
import matplotlib.pyplot as plt

if __name__ == "__main__":

    a0=float(input("\nEnter the length of the first link: "))
    a1=float(input("\nEnter the length of the second link: "))
    a2=float(input("\nEnter the length of the third link: "))

    x=float(input("\nEnter end-effector x value: "))
    y=float(input("\nEnter end-effector y value: "))

    minr=2*max(a0,a1,a2)-(a0+a1+a2)
    maxr=a0+a1+a2
    if minr<0:
        minr=0
    if math.sqrt(pow(x,2)+pow(y,2))<minr or maxr<math.sqrt(pow(x,2)+pow(y,2)):
        print("not possible")
        pass
    else:# put code here
        # angle=math.atan2(y,x)# point after two links
        # x1=x-((a2*x)/(math.sqrt(x**2+y**2))) # new point
        # y1=y-((a2*y)/(math.sqrt(x**2+y**2)))
        # # two link inverse
        # theta2=math.acos((1/(2*a0*a1))*((x1**2+y1**2)-(a0**2+a1**2)))
        # print(math.degrees(theta2))
        # theta1=math.atan2(y1,x1)-math.atan2((a1*math.sin(theta2)),(a0+a1*math.cos(theta2)))
        # print(math.degrees(theta1))
        flag=0
        for t1 in range(360):
            for t2 in range(360):
                p1=(a0*math.cos(math.radians(t1)),a0*math.sin(math.radians(t1)))
                p2=(x+a2*math.cos(math.radians(t2)),y+a2*math.sin(math.radians(t2)))
                dist=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
                if dist<(a1+0.0001) and dist>(a1-0.0001):
                # if dist==a1:
                    print("found")
                    flag=1
                    theta1=math.radians(t1)
                    if math.atan2((p2[1]-p1[1]),(p2[0]-p1[0]))<0:
                        theta2=math.radians(360)+math.atan2((p2[1]-p1[1]),(p2[0]-p1[0]))-theta1
                        pass
                    else:
                        theta2=math.atan2((p2[1]-p1[1]),(p2[0]-p1[0]))-theta1
                        pass
                    theta3=math.radians(t2)-math.radians(180)-theta2-theta1
                    # print(theta1,theta2,theta3)
                    # break
                pass
            # if flag==1:
            #     break
            pass
        # print(plot(a0,theta1,a1,theta2,a2,(-theta1-theta2+angle)))
        plot(a0,theta1,a1,theta2,a2,theta3)
        plt.xlim(-(a0+a1+a2),(a0+a1+a2))
        plt.ylim(-(a0+a1+a2),(a0+a1+a2))
        print(math.degrees(theta1),math.degrees(theta2),math.degrees(theta3))
        plt.show()
        pass