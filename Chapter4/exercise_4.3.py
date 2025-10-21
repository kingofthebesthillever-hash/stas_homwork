import math
import turtle

bob = turtle.Turtle()


def draw_triangle(t, r, angle):
    """Рисуем равнобедренный треугольник с помощью черепашки Т:
    r: длинна бедра
    angle: радиус вершинного угла в градусах
    y: координата"""

    y = r * math.sin(angle * math.pi / 180)  # тригонометрическая функция для конвертации координат

    t.rt(angle)
    t.fd(r)
    t.lt(90 + angle)
    t.fd(2 * y)
    t.lt(90 + angle)
    t.fd(r)
    t.lt(180 - angle)


def draw_polygon(t, n, r):
    """Рисуем многоугольник с помощью черепашки Т:
    n: количество сегментов
    r: длинна радиальных спиц"""
    angle = 360.0 / n
    for i in range(n):
        draw_triangle(t, r, angle / 2)
        t.lt(angle)
    t.pu()                              # перемещаем перо на r * 2 + 10
    t.fd(r * 2 + 10)
    t.pd()


draw_polygon(bob, 5, 30)
draw_polygon(bob, 6, 30)
draw_polygon(bob, 7, 30)
