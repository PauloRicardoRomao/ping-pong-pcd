import turtle
from turtle import *



#Configuração da janela

janela = turtle.Screen()
janela.title("Ping Pong")
janela.bgcolor("black")
janela.setup(width=800, height=600)
janela.tracer(0)


#Raquetes

#Raquete esquerda

raq_esq = turtle.Turtle()
raq_esq.speed(0)
raq_esq.shape("square")
raq_esq.color("white")
raq_esq.shapesize(stretch_wid=6, stretch_len=1)
raq_esq.penup()
raq_esq.goto(-350,0)

#Raquete direita

raq_dir = turtle.Turtle()
raq_dir.speed(0)
raq_dir.shape("square")
raq_dir.color("white")
raq_dir.shapesize(stretch_wid=6, stretch_len=1)
raq_dir.penup()
raq_dir.goto(350,0)

#Bola

bola = turtle.Turtle()
bola.speed(40)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = -0.2

#Placar

plc_esq = 0
plc_dir = 0

display_plc = turtle.Turtle()
display_plc.speed(0)
display_plc.color("white")
display_plc.penup()
display_plc.hideturtle()
display_plc.goto(0, 260)
display_plc.write("Esquerda: 0     Direita: 0", align="center", font=("Courier", 24, "normal"))



#Movimento das raquetes (para cima e para baixo)

#Movimento da raquete esquerda

def raq_esq_c():
    y = raq_esq.ycor()
    if y < 250:
        y += 20
    raq_esq.sety(y)


def raq_esq_b():
    y = raq_esq.ycor()
    if y > -240:
        y -= 20
    raq_esq.sety(y)


#Movimento da raquete direita

def raq_dir_c():
    y = raq_dir.ycor()
    if y < 250:
        y += 20
    raq_dir.sety(y)


def raq_dir_b():
    y = raq_dir.ycor()
    if y > -240:
        y -= 20
    raq_dir.sety(y)


#Atribuindo funções as teclas w, sc(para esquerda), seta para cima e seta para baixo (para direita)

janela.listen()
janela.onkeypress(raq_esq_c, "w")
janela.onkeypress(raq_esq_b, "s")
janela.onkeypress(raq_dir_c, "Up")
janela.onkeypress(raq_dir_b, "Down")


#Execução do jogo

while True:
    janela.update()

    #Movimento da bola

    bola.sety(bola.ycor() + bola.dy)
    bola.setx(bola.xcor() + bola.dx)

    #Verificação das bordas do display

    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        plc_esq += 1
        display_plc.clear()
        display_plc.write(f"Esquerda: {plc_esq}     Direita: {plc_dir}", align="center", font=("Courier", 24, "normal"))
    
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        plc_dir += 1
        display_plc.clear()
        display_plc.write(f"Esquerda: {plc_esq}     Direita: {plc_dir}", align="center", font=("Courier", 24, "normal"))
    
    
    #Verificação das batidas nas raquetes

    if (-350 < bola.xcor() < -340) and (raq_esq.ycor() - 50 < bola.ycor() < raq_esq.ycor() + 50):
        bola.setx(-340)
        bola.dx *= -1

    if (340 < bola.xcor() < 350) and (raq_dir.ycor() - 50 < bola.ycor() < raq_dir.ycor() + 50):
        bola.setx(340)
        bola.dx *= -1
    
    