import turtle
from random import randint
screen = turtle.getscreen()
risovalka = turtle.Turtle()
inp = int(input("Num: "))
for i in range(10) :
    risovalka.pendown()
    risovalka.right(90)
    risovalka.forward(inp)
    risovalka.backward(inp)
    risovalka.penup()
    risovalka.left(90)
    risovalka.forward(inp / 10)
risovalka.ht()
first = turtle.Turtle()
first.color("red")
first.penup()
first.right(90)
first.forward(inp / 5)
first.left(90)
first.backward(15)
second = turtle.Turtle()
second.color("green")
second.penup()
second.right(90)
second.forward(inp / 5 + inp / 5)
second.left(90)
second.backward(15)
third = turtle.Turtle()
third.color("blue")
third.penup()
third.right(90)
third.forward(inp / 5 + inp / 2.5)
third.left(90)
third.backward(15)
fourth = turtle.Turtle()
fourth.color("purple")
fourth.penup()
fourth.right(90)
fourth.forward(inp / 5 + inp / 5 + inp / 5 + inp / 5)
fourth.left(90)
fourth.backward(15)
finish = False
listik = [first, second, third, fourth]
f = 0
s = 0
t = 0
fo = 0
winner = 0
while not finish :
    for i in listik :
        j = randint(1, inp / 10)
        for d in range(j) :
            i.forward(1)
            if i.pos()[0] > (inp - 11) :
                finish = True
                winner = i
                break
for k in listik :
    if k != winner :
        k.ht()
winner.goto(inp / 2 - 50,-inp / 2)
winner.write("Winner", move=False, align="left", font=("Impact", 30, "normal"))
winner.goto(inp / 2,-inp / 2)
screen.mainloop()
