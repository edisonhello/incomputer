from visual import *

test = sphere(pos=(0,10,0))

ball1 = sphere(radius=0.2, pos=(-1,0,0), color=color.green)
ball2 = sphere(radius=ball1.radius, pos=(sqrt(3)/2,0.5,0.5), color=color.blue)
ball3 = sphere(radius=0.2, pos=ball2.pos-(0,0,1),color=color.red)

arrow1 = arrow(pos=ball1.pos, axis=ball2.pos-ball1.pos, color=color.white)
arrow2 = arrow(pos=ball1.pos, axis=ball3.pos-ball1.pos, color=color.yellow)
