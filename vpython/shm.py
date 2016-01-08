from visual import *
from math import *

zmx = 20
scene.range = zmx

i = 90

ball = sphere(radius=2, pos=(0,11,0), color=color.green)

while 1:
  rate(30)
  i=i+0.5
  ball.pos+=(0,2*sin(i/pi),0)
