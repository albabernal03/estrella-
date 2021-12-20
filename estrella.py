import turtle

#Para mostrar el puntero

turtle.showturtle()

#Seleccionar color de relleno
turtle.fullcolor('yellow')
turtle.begin_fill()

longitud=100
angulo=160

for i in range (10):
    turtle.forward(longitud)
    turtle.right(angulo)

