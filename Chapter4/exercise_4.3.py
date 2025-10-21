import math
import turtle

bob = turtle.Turtle()

def draw_triangle(t, r, angle):
    """Рисуем равнобедренный треугольник с помощью черепашки Т:
    r: длинна бедра
    angle: радиус вершинного угла в градусах
    y: координата"""

    y = r * math.sin(angle * math.pi / 180)

    t.rt(angle)
    t.fd(r)
    t.lt(90+angle)
    t.fd(2*y)
    t.lt(90+angle)
    t.fd(r)
    t.lt(180-angle)

draw_triangle(bob, 50, 30)