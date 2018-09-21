import PIL.ImageTk
import PIL.Image
import time
from random import randint
import math
from tkinter import *

from bot import main
import subprocess
from multiprocessing import Process,Queue,Pipe

diamond_count = 3000
data_diamonds = []
delete_diamonds = []
running = True

root = Tk()

canvas = Canvas(root, width=500, height=250)
root.resizable(width=False, height=False)

class CanvasObject():

    def __init__(self, x,y,canvas, img):
        self.x = x
        self.y = y
        self.image = PIL.Image.open(img)
        self.canvas = canvas
        self.canvasImage = PIL.ImageTk.PhotoImage(self.image)
        self.angle = 0

    def update(self):
        rotatedimg = PIL.ImageTk.PhotoImage(self.image.rotate(self.angle))
        self.canvasImage = rotatedimg
        self.canvas.create_image(self.x, self.y, image=self.canvasImage)
        # print(time.time())

minerbody = CanvasObject(350, 150, canvas, "images/miner_body.png")
minerfeet = CanvasObject(345, 185, canvas, "images/miner_legs.png")
minerpick = CanvasObject(330, 155, canvas, "images/miner_pickaxe.png")
rock      = CanvasObject(200, 185, canvas, "images/rock.png")

def quit():
    global running
    running = False

def init():
    root.title('Data Mine')
    canvas.pack()

    bot = subprocess.Popen(['python','bot.py'])
    #output = subprocess.check_output('bot.py',shell=True)

    while running:
        #print(bot.stdout.readline)
        visual_update()
    root.mainloop()

def visual_update():
    #test.update(canvas)
    #canvas.create_image(test.x, test.y, image=test.canvasImage)
    minerbody.angle = math.sin(time.time() * 7) * 10
    minerpick.angle = abs(math.sin(time.time() *7)) * -90 +90
    if(minerpick.angle>80):
        #print(diamond_count)
        mine_data_diamonds(canvas)
    canvas.update()
    time.sleep(0.03)

    #print(minerpick.angle)
    minerfeet.update()
    minerpick.update()
    minerbody.update()
    rock.update()
    updatediamonds(canvas)


 #representation of the data scraped by spawning diamonds

def updatediamonds(canvas):
    if(len(data_diamonds)>0):
        index = 0
        while index <len(data_diamonds):
            diamond = data_diamonds[index]
            diamond.update()
            diamond.angle+= diamond.spin
            diamond.x+=diamond.dx
            diamond.y+=diamond.dy
            diamond.dy+= 1.2

            if diamond.y>300:
                data_diamonds.pop(index)
            index+=1
    #garbage collection
    if(len(delete_diamonds)>1):
        for diamond in delete_diamonds:
           canvas.delete(diamond)
           data_diamonds.remove(diamond)

        delete_diamonds.clear()

def mine_data_diamonds(canvas):
    global diamond_count
    if diamond_count>0:
        diamond = CanvasObject(200, 185, canvas, "images/gem.png")
        data_diamonds.append(diamond)
        diamond.spin = randint(-30,30)
        diamond.dx = randint(-4,4)
        diamond.dy = randint(-15,-2)
        diamond_count-= 1



if __name__ == '__main__':
    init()
else:
    print("visual.py imported")