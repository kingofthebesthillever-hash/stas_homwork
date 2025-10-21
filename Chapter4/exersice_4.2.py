import turtle
import math

bob = turtle.Turtle()
bob.speed(10)

def lines(t, n, length, angle):
    """Рисует черепашкой t последовательно n отрезков линии длинной length
     с отклонением следующего отрезка под углом angle"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    """Рисует дугу с помощью t черепашки по радиусу r c углом angle"""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    t.lt(step_angle / 2)
    lines(t, n, step_length, step_angle)
    t.rt(step_angle / 2)

def petal(t, r, angle):
    """Рисует лепесток с помощью t черепашки по радиусу r c углом angle """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t, n, r, angle):
    """Рисует цветок с помощью t черепашки с
    n: количеством лепестков  c углом angle
    r: с радиусом дуги лепестка
    angle: angle (degrees) that subtends the arcs"""
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0 / n)


flower(bob, 7, 60, 60) # рисуем первый цветок

bob.penup()              # поднимаем и перемещаем перо
bob.goto(140, 0)
bob.pendown()

flower(bob, 10, 45, 90)  # второй цветок с новыми параметрами

bob.penup()             # поднимаем и перемещаем перо
bob.goto(280, 0)
bob.pendown()

flower(bob, 20, 120, 25) # третий цветок с новыми параметрами

turtle.exitonclick()
