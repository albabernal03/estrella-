import turtle


puntas_estrella= int(input('Seleccione el número de puntas de la estrella:'))

longitud=100
num1=180
num2=360    
num3= 120

if puntas_estrella == 9 and 36 and 18:
    angulo= (num2/puntas_estrella) + num3
else:
     angulo= num1 - (num2/puntas_estrella)

for i in range (puntas_estrella):
    turtle.forward(longitud)
    turtle.right(angulo)

turtle.showturtle()
