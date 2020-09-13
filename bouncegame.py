from tkinter import *
import random
import time
tk=Tk()
tk.title("Bounce!")
tk.resizable(0,0)
#makes the window not resizable
tk.wm_attributes("-topmost",1)
#to place the windows in front of all other windows
canvas=Canvas(tk,width=500,height=500,bd=0,highlightthickness=0)
#bd is border and highlight thickness is related to it
canvas.pack()
tk.update()


class Ball:
    def __init__(self,canvas,color,paddle):

        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        #x1,y1 for top left, x2,y2 for bottom right, since its a square a circle is formed, radius=7.5
        self.canvas.move(self.id,245,100)
        start=[-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
                           #this function returns canvas.height
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
        
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
                return True
            return False

    
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        #self. is ussed since canvas is passed as a parameter and and must be initialised for
        #use in this function
        pos=self.canvas.coords(self.id)
                 #returns an array [x1,y1,x2,y2]
        if pos[1]<=0:
            self.y=3
            #reverses the vertical direction
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
            canvas.create_text(245,100,text="GAME OVER!!")
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
        if self.hit_paddle(pos)== True:
            self.y=-3


class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,380)
        self.x=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
            self.x=0
    def turn_left(self,evt):
        self.x=-2
    def turn_right(self,evt):
        self.x=2



paddle=Paddle(canvas,"blue")
ball=Ball(canvas,"red",paddle)



while 1:
    if ball.hit_bottom==True:
        break
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    ball.draw()
    paddle.draw()
