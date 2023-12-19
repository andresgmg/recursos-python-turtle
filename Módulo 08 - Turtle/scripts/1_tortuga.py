import turtle

# personalizacion de la ventana
window = turtle.Screen()
window.title("Pruebas con turtle")
window.bgcolor("#68a0ed")
window.setup(800, 800)
window.setworldcoordinates(0, 800, 800, 0)

# personalizacion de la pluma
kame = turtle.Turtle()
kame.shape("turtle")
kame.color("darkgreen")
kame.pensize(2)
kame.speed(2)

# instrucciones de la pluma

for i in range(1, 10):
    kame.penup()
    kame.goto(i * 25, i * 25)
    kame.pendown()
    kame.circle(i * 25)

turtle.mainloop()
