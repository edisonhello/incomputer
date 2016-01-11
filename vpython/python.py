from visual import *
import math


scene.range = 2
ball = sphere(radius= 0.3, color=color.blue, pos=(0,0,0))
cc   = sphere(radius= 0.2, color=color.red , pos=(0,1,0))

line = curve(color=color.cyan)
line2 = curve(color=color.red)

i=0

while 1:
  rate(100)
  i=i+1
  #print i
  
  line.append(pos=ball.pos)
  line.pos-=(0,0.01,0)
  line2.append(pos=cc.pos)
  ball.pos=(sin(i*pi/180),0,0)
  cc.pos  =(sin(i*pi/180),cos(i*pi/180),0)
