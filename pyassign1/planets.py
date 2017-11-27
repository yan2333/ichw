Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
import turtle
import math

bj=turtle.Screen()
bj.bgcolor("black")
colors=['red', 'yellow', 'blue', 'green', 'orange',
        'purple', 'brown', 'sea green']

a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()
d=turtle.Turtle()
e=turtle.Turtle()
f=turtle.Turtle()
g=turtle.Turtle()

A=[0,0.38,0.72,1,1.52,5.2,9.54]
B=[0,0.2883,0.7198,0.9986,1.4523,5.1397,9.3892]
T=[1,87.7,224.7,365.0,686.98,1083.18,2151.9]
hudu=[0,0,0,0,0,0,0]
t=0

for i in [a,b,c,d,e,f,g]:
    i.up()
    i.hideturtle()
    i.color(colors[t])
    i.speed(10)
    i.shape("circle")
    i.shapesize(t/10+0.1,t/10+0.1,0)
    if t!=0:
        i.goto(30*A[t],0)
    else:
        i.goto(0,0)
    t=t+1
    i.showturtle()
    i.down()
    
while t>0:
    t=0
    for i in [a,b,c,d,e,f,g]:
        if hudu[t]>2*math.pi:
            hudu[t]=hudu[t]-2*math.pi
        else:
            hudu[t]=hudu[t]+math.pi/T[t]
        i.goto(30*A[t]*math.cos(hudu[t]),30*B[t]*math.sin(hudu[t]))
        t=t+1
    
        
        

