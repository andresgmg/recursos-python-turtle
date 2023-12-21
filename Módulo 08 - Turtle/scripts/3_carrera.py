import turtle
import random
import tkinter

# personalizacion de la ventana
window = turtle.Screen()
window.title("Carrera de tortugas")
window.bgcolor("#68a0ed")
window.setup(600, 600)
window.setworldcoordinates(0, 600, 600, 0)

tortugas = []

colores = [
    "yellow",
    "orange",
    "red",
    "brown",
    "purple",
    "blue",
    "cyan",
    "green",
    "black",
    "white",
]

for indice, color in enumerate(colores):
    tortuga = turtle.Turtle()
    tortuga.shape("turtle")
    tortuga.color(color)
    tortuga.pensize(2)
    tortuga.speed(2)
    tortuga.penup()
    tortuga.goto(10, indice * 40 + 100)
    tortuga.pendown()
    tortugas.append(tortuga)

run = True
while run:
    for tortuga in tortugas:
        distancia = random.randint(0, 20)
        tortuga.forward(distancia)
        if tortuga.xcor() >= 580:
            tkinter.messagebox.showinfo(
                title="Fin de la carrera!",
                message=f"Ha ganado la tortuga {tortuga.color()[0].upper()}",
            )
            run = False
            break


turtle.mainloop()
