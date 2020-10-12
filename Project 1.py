# Mini Project

import turtle
from math import sin, radians, pi

# 4.3 Cvicenia

#1

# def square(t):
#     for i in range(4):
#         t.fd(10)
#         t.lt(90)

# bob = turtle.Turtle()
# square(bob)

#2

# def square(t, length):
#     for i in range(4):
#         t.fd(length)
#         t.lt(90)

# bob = turtle.Turtle()
# square(bob, 100)

#3

# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)

# bob = turtle.Turtle()
# polygon(bob, 30, 3)

#4

# def polygon(t, length, n):
#     for i in range(n):
#         t.fd(length)
#         t.lt(360/n)

# def circle(t, r):
#     circumference = 2 * pi * r
#     n = int(circumference / 3) + 3
#     length = circumference / n
#     polygon(t, length, n)


    
# bob = turtle.Turtle()

# circle(bob, 60)


#5
# def polyline(t, n, length, angle):
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)



# def arc(t, r, angle):
#     arc_length = 2 * pi * r * angle / 360
#     n = int(arc_length / 3) + 1
#     step_length = arc_length / n
#     step_angle = float(angle) / n
#     polyline(t, n, step_length, step_angle)


# bob = turtle.Turtle()

# arc(bob, 120, 90)

# kvety bez stonky



def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def arc(t, r, angle):
    arc_length = 2 * pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def calculationOfR(t, stonkaHeight, angleStonka):
    r = (stonkaHeight/2) / sin(radians(angleStonka/2))
    arc(t, r, angleStonka)

def stonka(t, stonkaHeight, angleStonka):
    t.rt(90+angleStonka/2)
    calculationOfR(t, stonkaHeight, angleStonka)
    t.lt(180- angleStonka/2)

def listy(t, angleGround, widthList, lenghtList):
    t.lt(90 - angleGround - widthList / 2)

    for i in range(2):
        calculationOfR(t, lenghtList, widthList)
        t.lt(180-widthList)

    t.rt(180 - 2 * angleGround)

    for _ in range(2):
        calculationOfR(t, lenghtList, widthList)
        t.lt(180 - widthList)

    t.lt(-angleGround + widthList / 2)

def move(t, length, stonkaHeight):
    t.pu()
    t.fd(length)
    t.lt(90)
    t.fd(stonkaHeight)
    t.rt(90)
    t.pd()

    
def flower(t, n, r, angle, stonkaHeight, angleStonka, angleGround, widthList, lenghtList, ):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)
    stonka(t, stonkaHeight, angleStonka)
    listy(t, angleGround, widthList, lenghtList)
    move(t, 200, stonkaHeight)
    
   

bob = turtle.Turtle()
bob.speed(0)


move(bob, -200, 0)
flower(
    bob, 
    n = 7, 
    r = 60.0,
    angle =  60.0,
    stonkaHeight = 100,
    angleStonka = 30,
    angleGround = 30,
    widthList = 100,
    lenghtList = 40,

)


flower(
    bob, 
    n = 10, 
    r = 40.0,
    angle =  80.0,
    
    stonkaHeight = 120,
    angleStonka = 45,
    
    angleGround = 70,
    widthList = 10,
    lenghtList = 150,

)



flower(
    bob, 
    n = 20, 
    r = 140.0,
    angle =  20.0,

    stonkaHeight = 140,
    angleStonka = 70,    
    
    angleGround = 40,
    widthList = 120,
    lenghtList = 100,

)
screen = turtle.Screen()
screen.mainloop()


