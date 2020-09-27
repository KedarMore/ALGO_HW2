import math
import matplotlib.pyplot as plt

def plot(a0,t0,a1,t1,a2,t2):
    """
    docstring
    """
    x=[a0*(math.cos(t0)),a1*(math.cos(t0+t1)),a2*(math.cos(t0+t1+t2))]
    y=[a0*(math.sin(t0)),a1*(math.sin(t0+t1)),a2*(math.sin(t0+t1+t2))]

    plt.plot([0,x[0],x[0]+x[1],x[0]+x[1]+x[2]],[0,y[0],y[0]+y[1],y[0]+y[1]+y[2]],'bo')

    plt.plot([0,x[0],x[0]+x[1],x[0]+x[1]+x[2]],[0,y[0],y[0]+y[1],y[0]+y[1]+y[2]],'r-')
    
    return x,y

if __name__ == "__main__":
    a0=float(input("\nEnter the length of the first link: "))
    t0=math.radians(float(input("\nEnter its angle (degrees) wrt the ground: ")))
    a1=float(input("\nEnter the length of the first link: "))
    t1=math.radians(float(input("\nEnter its angle (degrees) wrt the previous link: ")))
    a2=float(input("\nEnter the length of the first link: "))
    t2=math.radians(float(input("\nEnter its angle (degrees) wrt the previous link: ")))

    # x=[a0*(math.cos(t0)),a1*(math.cos(t0+t1)),a2*(math.cos(t0+t1+t2))]
    # y=[a0*(math.sin(t0)),a1*(math.sin(t0+t1)),a2*(math.sin(t0+t1+t2))]

    # plt.plot([0,x[0],x[0]+x[1],x[0]+x[1]+x[2]],[0,y[0],y[0]+y[1],y[0]+y[1]+y[2]],'bo')

    # plt.plot([0,x[0],x[0]+x[1],x[0]+x[1]+x[2]],[0,y[0],y[0]+y[1],y[0]+y[1]+y[2]],'r-')

    x,y=plot(a0,t0,a1,t1,a2,t2)

    print("\nFinal position is: ("+str(round((x[0]+x[1]+x[2]),3))+","+str(round((y[0]+y[1]+y[2]),3))+")")

    plt.show()
    pass