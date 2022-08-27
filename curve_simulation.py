# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 16:25:30 2022

@author: vjonak
"""

import numpy as np
import matplotlib.pyplot as plt

""" NOT WORKING NOW """

def rotate_object(point, origin, angleDeg):
    """ 
    Rotate NCAP object around given point by given angle
    Rotation clockwise NORTH = 0°
    The angle should be given in radians.
    """
    import math
    
    ox, oy = origin
    px, py = point
    
    angle = math.radians(angleDeg)
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def head2angle(h):
    return (((h)-90)*-1)%360


alpha = 72 #deg
r = 120 #m
_dir = 'R'

head = 90#deg


E = np.linspace(0,15,150)
N = [e*np.tan(np.deg2rad(head2angle(head))) for e in E]

x0 = E[-1]
y0 = N[-1]

X = []
Y = []


if _dir == "R":
    bulhar = -1
else:
    bulhar = 1
    
for i in range(0, (alpha+1)*5):
    dx = bulhar*r*np.cos(np.deg2rad(i/5)) + x0
    dy = r*np.sin(np.deg2rad(i/5)) + y0
    X.append(dx)
    Y.append(dy)


_X = []
_Y = []

for i in range(len(X)):
    x, y = rotate_object([X[i], Y[i]], [X[0], Y[0]], -head)
    _X.append(x)
    _Y.append(y)
    
shiftX = _X[0] - E[-1]
shiftY = _Y[0] - N[-1]

__X = [x-shiftX for x in _X]
__Y = [y-shiftY for y in _Y]


fig, axes = plt.subplots(1,1)
axes.plot(E, N, lw=2, color='r')

axes.scatter(x0, y0)
axes.plot([x0, X[-1]], [y0, Y[-1]], lw=0.5, ls='--', c='k')
axes.plot([x0, X[0]], [y0, Y[0]], lw=0.5, ls='--', c='k')
axes.scatter(X, Y, s=1)
axes.scatter(_X, _Y, s=1)

axes.scatter(__X, __Y, s=2)

axes.set_aspect('equal')
plt.show()