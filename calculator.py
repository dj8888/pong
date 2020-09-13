from tkinter import *

root=Tk()
root.geometry("150x150")
root.resizable(0,0)

currequa=""
equation=StringVar()                            #StringVar() is used. Hence we can use equation.set(" ")














calculation=Label(root,textvariable=equation)

#equation is a sting variable. Calculation label is
#udated automatically each time equation is updated. 

equation.set("Enter your Equation:")
calculation.grid(columnspan=4)


def btnPress(num):
    global currequa                             #neccesary to put global for function to be able edit the global variable's value
    currequa=currequa+str(num)
    equation.set(currequa)

def equalpressed():
    global currequa
    ans=str(eval(currequa))
    equation.set(ans)
    currequa=ans

def clear():
    global currequa
    currequa=""
    equation.set(currequa)

Button0=Button(root,text="0",command=lambda:btnPress(0))
Button0.grid(row=4,column=1)

#lamba is known as anonymous function,works just like a normal function, but is instantaneously defined, it always returns a predefined statement,can be put anywhere a function is expected.
#syntax is lambda:action 
#in this case helps us to pass a parameter to the btnPress function

Button1=Button(root,text="1",command=lambda:btnPress(1))
Button1.grid(row=3,column=0)
Button2=Button(root,text="2",command=lambda:btnPress(2))
Button2.grid(row=3,column=1)
Button3=Button(root,text="3",command=lambda:btnPress(3))
Button3.grid(row=3,column=2)
Button4=Button(root,text="4",command=lambda:btnPress(4))
Button4.grid(row=2,column=0)
Button5=Button(root,text="5",command=lambda:btnPress(5))
Button5.grid(row=2,column=1)
Button6=Button(root,text="6",command=lambda:btnPress(6))
Button6.grid(row=2,column=2)
Button7=Button(root,text="7",command=lambda:btnPress(7))
Button7.grid(row=1,column=0)
Button8=Button(root,text="8",command=lambda:btnPress(8))
Button8.grid(row=1,column=1)
Button9=Button(root,text="9",command=lambda:btnPress(9))
Button9.grid(row=1,column=2)
plus=Button(root,text="+",command=lambda:btnPress("+"),bg="blue",fg="white")
plus.grid(row=1,column=4)
minus=Button(root,text="-",command=lambda:btnPress("-"),bg="blue",fg="white")
minus.grid(row=2,column=4)
multiply=Button(root,text="*",command=lambda:btnPress("*"),bg="blue",fg="white")
multiply.grid(row=3,column=4)
divide=Button(root,text="/",command=lambda:btnPress("/"),bg="blue",fg="white")
divide.grid(row=4,column=4)
equals=Button(root,text="=",command=equalpressed,bg="red",fg="white")
equals.grid(row=4,column=2)
clear=Button(root,text="C",command=clear,bg="red",fg="white")
clear.grid(row=4,column=0)



root.mainloop()
