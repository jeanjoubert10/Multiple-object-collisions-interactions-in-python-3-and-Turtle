
# Swap velocities with collisions as suggested by Christian Thompson (Youtube)..thanks
# tempx = i.x
# i.x = obj[j].x
# obj[j].x = i.x

import turtle
import random
import time
import os

win = turtle.Screen()
win.setup(1000,1000)
win.bgcolor('cyan')
win.tracer(0)
win.listen()


class Bubble(turtle.Turtle):
    def __init__(self, mass, nr):
        super().__init__(shape = 'circle')
        self.up()
        self.mass = mass
        self.goto(random.randint(-400, 400), random.randint(-400,400))
        self.shapesize(mass/20)
        self.radius = mass/2
        self.nr = nr
        self.list = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
        self.color(random.choice(self.list))
        self.bounce = 'ready'
        self.list = [-3, -2, -1, 1, 2, 3]
        self.xvelocity = random.choice(self.list)
        self.yvelocity = random.choice(self.list)
        

    def move(self):
        self.goto(self.xcor()+self.xvelocity, self.ycor()+ self.yvelocity)

        if (self.xcor()>= 495-self.radius and self.xvelocity>0) or (self.xcor()<= - 495+self.radius and self.xvelocity<0):
            self.xvelocity *= -1

        if (self.ycor()>= 495-self.radius and self.yvelocity>0) or (self.ycor()<= -495+self.radius and self.yvelocity<0):
            self.yvelocity *= -1
            
objList = []

for i in range(20):
    bubble = Bubble(random.randint(30,70), i)
    objList.append(bubble)


count = 0

while True:
    win.update()
    time.sleep(0.01)
    
    for i in objList:
        if i.bounce == 'wait' and count%10==0:
            i.bounce = 'ready'
        i.move()
        for j in range(len(objList)):
            if i.nr != objList[j].nr and i.bounce == 'ready':
                if i.distance(objList[j])<(i.radius+objList[j].radius):
                    i.bounce = 'wait'
                    os.system('afplay pop.wav&')
                    temp_x = i.xvelocity
                    temp_y = i.yvelocity
                    i.xvelocity = objList[j].xvelocity
                    i.yvelocity = objList[j].yvelocity
                    objList[j].xvelocity = temp_x
                    objList[j].yvelocity = temp_y
                    objList[j].bounce = 'wait'
    
    count += 1
     
        
   

    


        
