from tkinter import *
win=Tk()
win.title("calculator")
win.geometry("400x400")
win.resizable(False,False)

def click(value):
    entry.insert(END,value)

def clear():
    entry.delete(0,END)

def delete():
    entry.delete(len(entry.get())-1,END)

def calculate():
    try:
        expression = entry.get()
        expression = expression.replace("x", "*")
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")



entry=Entry(win,font=("arial" ,30),border=10,justify=RIGHT)
entry.place(x=0,y=30,width=385,height=80)

b1=Button(win,text="%",font=("arial" ,20),background="red",command = lambda: click("%"))
b1.place(x=0,y=350,width=100)
b2=Button(win,text="0",font=("arial" ,20),background="green",command = lambda: click("0"))
b2.place(x=100,y=350,width=100)
b3=Button(win,text=".",font=("arial" ,20),background="red",command = lambda: click("."))
b3.place(x=200,y=350,width=100)
b4=Button(win,text="=",font=("arial" ,20),background="green",command = calculate)
b4.place(x=300,y=350,width=100)
b5=Button(win,text="1",font=("arial" ,20),background="green",command = lambda: click("1"))
b5.place(x=0,y=295,width=100)
b6=Button(win,text="2",font=("arial" ,20),background="red",command = lambda: click("2"))
b6.place(x=100,y=295,width=100)
b7=Button(win,text="3",font=("arial" ,20),background="green",command = lambda: click("3"))
b7.place(x=200,y=295,width=100)
b8=Button(win,text="+",font=("arial" ,20),background="red",command = lambda: click("+"))
b8.place(x=300,y=295,width=100)
b9=Button(win,text="4",font=("arial" ,20),background="red",command = lambda: click("4"))
b9.place(x=0,y=240,width=100)
b10=Button(win,text="5",font=("arial" ,20),background="green",command = lambda: click("5"))
b10.place(x=100,y=240,width=100)
b11=Button(win,text="6",font=("arial" ,20),background="red",command = lambda: click("6"))
b11.place(x=200,y=240,width=100)
b12=Button(win,text="-",font=("arial" ,20),background="green",command = lambda: click("-"))
b12.place(x=300,y=240,width=100)
b13=Button(win,text="7",font=("arial" ,20),background="green",command = lambda: click("7"))
b13.place(x=0,y=185,width=100)
b14=Button(win,text="8",font=("arial" ,20),background="red",command = lambda: click("8"))
b14.place(x=100,y=185,width=100)
b15=Button(win,text="9",font=("arial" ,20),background="green",command = lambda: click("9"))
b15.place(x=200,y=185,width=100)
b16=Button(win,text="x",font=("arial" ,20),background="red",command = lambda: click("x"))
b16.place(x=300,y=185,width=100)
b17=Button(win,text="Ac",font=("arial" ,20),background="red",command = clear)
b17.place(x=0,y=135,width=100)
b18=Button(win,text="del",font=("arial" ,20),background="green",command = delete)
b18.place(x=100,y=135,width=100)
b19=Button(win,text="//",font=("arial" ,20),background="red",command = lambda: click("//"))
b19.place(x=200,y=135,width=100)
b20=Button(win,text="/",font=("arial" ,20),background="green",command = lambda: click("/"))
b20.place(x=300,y=135,width=100)



win.mainloop()