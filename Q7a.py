import math
import matplotlib.pyplot as plt

def plot(a0,t0,a1,t1,a2,t2):
    """
    Plots the kinematic chain
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

    x,y=plot(a0,t0,a1,t1,a2,t2)
    print("\nPoint 0 is: (0,0)")
    print("\nPoint 1 is: ("+str(round((x[0]),3))+","+str(round((y[0]),3))+")")
    print("\nPoint 2 is: ("+str(round((x[0]+x[1]),3))+","+str(round((y[0]+y[1]),3))+")")
    print("\nFinal position is: ("+str(round((x[0]+x[1]+x[2]),3))+","+str(round((y[0]+y[1]+y[2]),3))+")")

    plt.annotate("Start\n(0,0)",(0,0))
    plt.annotate("("+str(round((x[0]),3))+","+str(round((y[0]),3))+")",(x[0],y[0]))
    plt.annotate("("+str(round((x[0]+x[1]),3))+","+str(round((y[0]+y[1]),3))+")",(x[0]+x[1],y[0]+y[1]))
    plt.annotate("End effector\n("+str(round((x[0]+x[1]+x[2]),3))+","+str(round((y[0]+y[1]+y[2]),3))+")",(x[0]+x[1]+x[2],y[0]+y[1]+y[2]))
    plt.title("Q7 Forward Kinematics")
    plt.show()
    pass