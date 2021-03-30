canvasWidth = 600
canvasHeight = 600
size = canvasWidth / 20;
import time
import random
from tkinter import * 

root = Tk()

canvas = Canvas(root, width=600, height=600)
canvas.pack()

class Snake :
    def __init__(self) :
        self.size = size
        self.color = 'green'
        self.x = 0
        self.y = 0 
        self.speed = self.size
        self.speedX = self.size
        self.speedY = 0
        self.tail = [[0, 0]]
    def show(self) :
        for i in range(len(self.tail)) :
            el = self.tail[i];
            # self.object = canvas.create_rectangle(el[0], el[1], self.size, self.size, fill=self.color)

    def update(self) :
        self.x += self.speedX
        self.y += self.speedY
        del self.tail[0]
        self.tail.append([self.x, self.y])
        for i in range(len(self.tail) - 1) :
            self.snakeCollision(self.tail[i])
    
    def move(direction, self) :
        if event.keysym == "Up" :
            canvas.move(rect, 0, -3)
        if event.keysym == "Down" :
            canvas.move(rect, 0, 3)
        if event.keysym == "Left" :
            canvas.move(rect, -3, 0)
        if event.keysym == "Right" :
            canvas.move(rect, 3, 0)
        canvas.bind_all("<KeyPress>", move_rectangle)

    def wallCollision(self) :
        return (self.x + self.size > canvasWidth) or (self.x < 0) or (self.y < 0) or (self.y + self.size > canvasHeight)
    def eat(food, self) :
            return food.x == self.x and food.y == self.y
    def grow(self) :
        self.tail.push([self.x, self.y])
    def getLength(self) :
        return len(self.tail)
    def gameOver(self) :
        canvas.create_text(100 , 10 , fill="black",font="Times 20", text="Click the bubbles that are multiples of two.")
        import sys
        print("qer")
    def snakeCollision(tail, self) :
        if (tail[0] == self.x and tail[1] == self.y) :
            self.gameOver()
class Food :
    def __init__(self) :
        self.x = None;
        self.y = None;
        self.color = 'red'
        self.size = size;
    def show(self) :
        canvas.create_rectangle(self.x, self.y, self.size, self.size, fill=self.color)
    def getRandomSpot(self) :
        return int(random.randint(0, size / 2)) * size
    def pickLocation(self) :
        self.x = self.getRandomSpot();
        self.y = self.getRandomSpot();
# class Score() :
#     def __init__(self) :
#         self.score = 0
#     def show(self) :
#         ctx.fillStyle = 'blue'
#         ctx.textAlign = 'center'
#         ctx.textBaseline = 'middle'
#     def update(score, self) :
#         self.score = score

s = Snake()
f = Food()
# score = Score()
f.pickLocation()
def keyPressEvent(event) :
    s.move(event.keyCode);
def game() :
    # ctx.clearRect(0, 0, canvas.clientWidth, canvas.clientHeight)
    s.show()
    f.show()
    # score.show()
    s.update()
    # score.update(s.getLength())
    if (s.wallCollision()) :
        s.gameOver()
    if (s.eat(f)) :
        s.grow()
        f.pickLocation();
# document.addEventListener('keypress', keyPressEvent)
while True :
    game()
    time.sleep(0.150)
    root.mainloop()