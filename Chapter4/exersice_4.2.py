import turtle

bob = turtle.Turtle()

def lines(t, n, length, angle):
    """Рисует черепашкой t последовательно n отрезков линии длинной length
     с отклонением следующего отрезка под углом angle"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)


lines(bob,5,100 ,10)
