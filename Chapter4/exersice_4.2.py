import turtle
import math

bob = turtle.Turtle()

def lines(t, n, length, angle):
    """Рисует черепашкой t последовательно n отрезков линии длинной length
     с отклонением следующего отрезка под углом angle"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Рисует дугу с помощью t черепашки пр радиусу r c углом angle"""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle / 2)
    lines(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def petal(t, r, angle):
    """Рисует лепесток с помощью t черепашки пр радиусу r c углом angle """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

petal(bob,100,50)

turtle.exitonclick()