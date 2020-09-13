from tkinter import *
import random
import time

tk=Tk()
tk.title("PONG!!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.config(bg="black")
#new command canvas.config
canvas.pack()
tk.update()


canvas.create_line(250,0,250,400,fill="white")

counter=0
counter2=0


class Ball:
    def __init__(self,canvas,color,paddle,paddle2):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,235,200)
        self.paddle=paddle
        self.paddle2=paddle2
        starts=[-3,3]
        random.shuffle(starts)
        self.x=starts[1]
        self.y=starts[0]
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
                
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.y=-3
        if pos[0]<=0:
            self.x=3
            self.score(True)
        if pos[2]>=500:
            self.x=-3
            self.score(False)
        if self.hit_paddle(pos)==True:
            self.x=3
        if self.hit_paddle2(pos)==True:
            self.x=-3
            
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[1]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
            if pos[0]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                return True
            return False
        
    def hit_paddle2(self,pos):
        paddle_pos2=self.canvas.coords(self.paddle2.id)
        if pos[1]>=paddle_pos2[1] and pos[1]<=paddle_pos2[3]:
            if pos[2]>=paddle_pos2[0] and pos[2]<=paddle_pos2[2]:
                return True
            return False

    def score(self,val):
        global counter
        global counter2

        if val==True:
            a=self.canvas.create_text(375,40,text=counter,font=("Arial",60),fill="white")
            canvas.itemconfig(a,fill="black")
            counter+=1
            a=self.canvas.create_text(375,40,text=counter,font=("Arial",60),fill="white")

        if val==False:
            b=self.canvas.create_text(125,40,text=counter2,font=("Arial",60),fill="white")
            canvas.itemconfig(b,fill="black")
            #canvas.itemcongig(item, congiguration)
            counter2+=1
            b=self.canvas.create_text(125,40,text=counter2,font=("Arial",60),fill="white")



        

class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,150,20,250,fill=color)
        self.y=3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("w",self.goup)
        self.canvas.bind_all("s",self.godown)



        
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=self.canvas_height:
            self.y=0

    def goup(self,evt):
        #evt parameter necessary to record event of key press, through bind/bind_all
        self.y=-3
    def godown(self,evt):
        self.y=3

class Paddle2:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(480,150,500,250,fill=color)
        self.y=3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<Up>",self.goup)
        self.canvas.bind_all("<Down>",self.godown)



        
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=0
        if pos[3]>=self.canvas_height:
            self.y=0

    def goup(self,evt):
        #evt parameter necessary to record event of key press, through bind/bind_all
        self.y=-3
    def godown(self,evt):
        self.y=3

paddle=Paddle(canvas,"yellow")

paddle2=Paddle2(canvas,"blue")

ball=Ball(canvas,"orange",paddle,paddle2)


while 1:
    ball.draw()
    paddle.draw()
    paddle2.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
