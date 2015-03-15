from math import sin,cos,sqrt,pi
from model import *

def dart_star():
    a0y = -1
    a0x = 0.0
    b0y = -0.5
    b0x = sqrt(4/phi**2 - 1)/2
    c0y = 0.0
    c0x = 0.0

    a1y = -1.0
    a1x = 0.0
    b1y = -0.5
    b1x = -sqrt(4/phi**2 - 1)/2
    c1y = 0.0
    c1x = 0.0


    halfdartpoints = [  (a0x,a0y,b0x,b0y,c0x,c0y),
                        (a1x,a1y,b1x,b1y,c1x,c1y)]

    tiles = []
    for i in range(5):
        d = i*2*pi/5
        for point in halfdartpoints:
            ax,ay,bx,by,cx,cy = point
            
            Ax = (ax*cos(d) - ay*sin(d))
            Ay = (ax*sin(d) + ay*cos(d))

            Bx = (bx*cos(d) - by*sin(d))
            By = (bx*sin(d) + by*cos(d))

            Cx = (cx*cos(d) - cy*sin(d))
            Cy = (cx*sin(d) + cy*cos(d))

            tiles.append(HalfDart((Ax,Ay),(Bx,By),(Cx,Cy)))

    return tiles
