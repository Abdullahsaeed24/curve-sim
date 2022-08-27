from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import seaborn as sns
import math 

def equationroots(a, b, c):
    
    
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    val1 = 0
    val2 = 0

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))

        val1 = (-b + sqrt_val)/(2 * a)
        val2 = (-b - sqrt_val)/(2 * a)
        return val1,val2

    elif dis == 0:

        print(" real and same roots")
        print(-b / (2 * a))
        val1 = -b / (2 * a)
        val2 = -b / (2 * a)
        return val1,val2

   # when discriminant is less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)
        return '#','#'


def create_curve(**p):
    
    if ("theta" in p) and ("yc" in p) and ("xc" in p) and("r" in p):
        
        stheta = p["theta"]
        yc = p["yc"]
        xc = p["xc"]
        r = p["r"]
        
        arcx_points = []
        arcy_points = []
        
        
        theta = stheta /100
        
        # calculating the points on trhe arc
        for i in range(0,100,1):    
           
            dx = r * np.cos(theta*i) + xc
            dy = r * np.sin(theta*i) + yc
            
            arcx_points.append(dx)
            arcy_points.append(dy)
    
    
    return arcx_points , arcy_points





def rotate(**p):
    
    
    if ("E" in p) and ("N" in p) and ("tangle" in p) and ("yc" in p) and ("xc" in p) and  ("rot_dir" in p):

        
        E = p["E"] 
        N = p["N"]
        angle = p["tangle"]
        yc = p["yc"]        
        xc = p["xc"]
        rot = p["rot_dir"]
        
        arcx_points=[]
        arcy_points=[]
        
        
        for i in range(0,100,1):
            
            if rot =="ccw":
                
                # counterclockwise rotation
                dx = ((E[i] - xc) * np.cos(angle) - (N[i] - yc ) * np.sin(angle)) + xc
                dy = ((E[i] - xc) * np.sin(angle) + (N[i] - yc ) * np.cos(angle)) + yc
            
            elif rot =="cw":
                
                # clockwise rotation
                dx = (E[i] - xc) * np.cos(angle) + (N[i] - yc) * np.sin(angle) + xc
                dy = -1*(E[i] - xc) * np.sin(angle) + (N[i] - yc) * np.cos(angle) + yc    
            
            
            arcx_points.append(dx)
            arcy_points.append(dy)


        arcx=[]
        arcy =[]

        
        for i in range(0,len(arcx_points),1):
            

            if rot =="ccw":
                
                arcx.append(arcx_points[len(arcx_points)-1-i])
                arcy.append(arcy_points[len(arcy_points)-1-i])
                    

            elif rot =="cw":
                
                return arcx_points,arcy_points
                pass
                        



        return arcx ,arcy


    


E = [1,2,3,4,5,6,7,8,9,10]
N = [2,4,6,8,10,12,14,16,18,20]






r = 10
angle =50

HeadingAngle = 45

a = 0
b = 0
c = 0

# needed symboles
u = 0
z = 0

x1 = E[-1]
y1 = N[-1]


# the 2nd or (last) point on Radius line
x2 = 0
y2 = 0

xc1 , xc2 = 0,0
yc1 , yc2 = 0,0


m1= 0 # slope of the previoues phase
m2= 0 # slope of the IN Curve Phase


m1 = (N[3]-N[2]) / (E[3]-E[2])

m2 = (1/m1)*-1


HeadingAngle = math.degrees(math.atan(m1))

u = (-1 * m2 * x1) + y1
z = u -  y1
c = (x1 * x1) + (z * z) - ( r * r)


a = 1+ (m2 * m2)
b = -2 * x1 + (2 * m2 * z)

xc1 , xc2 = equationroots(a,b,c)

# calculate yc1 , yc2 from this equation ----- >>> yc1 = m2 * xc1 +u , yc2 = m2*xc2 + u
yc1 =(m2 * xc1) + u
yc2 =(m2 * xc2) + u


angle_In_Rad = np.deg2rad(angle)
stotal = r * angle_In_Rad

theta =  angle_In_Rad /100


fig,ax= plt.subplots()

#ax.plot(arcx_points,arcy_points)
#ax.plot(arcx,arcy)

#ax.plot([xc1,xc2] , [yc1,yc2])
#ax.scatter(xc2,yc2)
#x.scatter(xc1,yc1)
#ax.scatter(E[-1],N[-1])

#ax.plot(e,n)
#ax.plot(E,N)
ax.set_aspect("equal")

plt.show()
