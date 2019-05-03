import time
import numpy as np
from vpython import*

scene = canvas(width=1400, height=750)

xaxis = curve(vector(30,0,0), vector(-30,0,0))
yaxis = curve(vector(0,30,0), vector(0,-30,0))
zaxis = curve(vector(0,0,30), vector(0,0,-30))
xaxis.width = 10

sun = sphere(pos=vector(0,0,0), radius=1, color=color.yellow)
earth = sphere(pos=vector(0,4,0), radius=0.5,)
earth.texture = textures.earth

ball2 = sphere(pos=vector(0,4,0), radius=0.5, color=color.red)
dt = 0.01

shapes.line()

while 1:
    dt+=0.01
    rate(50)

    earth.pos = vector(25 * cos(dt), 25 * sin(dt), 0)
    ball2.pos = vector(25 * sin(dt)*sin(dt), 0, 25 * cos(dt)*sin(dt))

