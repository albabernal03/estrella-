<h1 align="center">	✨Estrellas✨</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/albabernal03/estrella-)

***
<h2>¿De qué trata esta tarea?</h2>

En esta tarea hemos utilizado el módulo conocido como 'turtle' que permite crear gráficos de tortuga. La tortuga se puede entender como el "puntero" al cual se le da órdenes para dibujar una figura. En esta tarea al usuario se le pregunta el número de puntas que quiere que tenga su estrella y gracias al turtle este nos muestra una pestaña gráfica y nos lo dibuja.

***

<h2>Diagrama de flujo:</h2>

![diagrama de flujo](https://user-images.githubusercontent.com/91721875/146826242-1e4568db-0442-404a-bf79-78a827c3954c.jpg)



***

<h2>Código:</h2>


```
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


```
***
