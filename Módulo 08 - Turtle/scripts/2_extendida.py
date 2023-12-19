import turtle
import math

# personalizacion de la ventana
window = turtle.Screen()
window.title("Extendiendo una tortuga")
window.bgcolor("#68a0ed")
window.setup(500, 500)
window.setworldcoordinates(0, 500, 500, 0)


class Tortuga(turtle.Turtle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pensize(2)
        self.shape("turtle")
        self.color("darkgreen")

    def rectangulo(self, x, y, ancho, alto, color="black"):
        self.color(color)
        self.penup()
        self.goto(x - ancho / 2, y - alto / 2)  # vertice superior izquierda
        self.pendown()
        self.goto(x + ancho / 2, y - alto / 2)  # vertice superior derecho
        self.goto(x + ancho / 2, y + alto / 2)  # vertice inferior derecho
        self.goto(x - ancho / 2, y + alto / 2)  # vertice inferior izquierdo
        self.goto(x - ancho / 2, y - alto / 2)  # vertice superior izquierdo

    def poligono(self, lados, radio, color="black"):
        self.color(color)
        angulo = math.pi * 2 / lados
        ancho_ventana = window.screensize()[0] / 2
        alto_ventana = window.screensize()[1] / 2
        # teorema del seno y del coseno para dibujar el poligono
        x = radio * math.sin(angulo) + ancho_ventana
        y = radio * math.cos(angulo) + alto_ventana
        self.penup()
        self.goto(x, y)
        self.pendown()
        for i in range(lados + 1):
            x = radio * math.sin(angulo * i) + ancho_ventana
            y = radio * math.cos(angulo * i) + alto_ventana
            self.goto(x, y)


kame = Tortuga()

# para mostrar la funcion del rectangulo
# x, y = (250, 250)
# w, h = (50, 50)
# incrementar = 50
# for color in ["yellow", "blue", "red"] * 2:
#     kame.rectangulo(x, y, w, h, color=color)
#     w += incrementar
#     h += incrementar

# para mostrar la funcion del poligono
# los colores los multiplicamos por un numero alto para que no se acabe ese bucle
colores = ["yellow", "blue", "red"] * 100
for n, color in zip(range(4, 20), colores):
    kame.poligono(n, n * 10, color=color)

turtle.mainloop()
