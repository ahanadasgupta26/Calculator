from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="black")

equation=""

def show(val):
    global equation
    equation+=val
    res.config(text=equation)

def clear():
    global equation
    equation=""
    res.config(text=equation)

def cal():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    res.config(text=result)

def backspace():
    global equation
    equation = equation[:-1]
    res.config(text=equation)

res=Label(root,width=30,height=2,text="",font=("arial",30))
res.pack()

but1=Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark blue",command=lambda:clear())
but1.place(x=10,y=100)

but2=Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("%"))
but2.place(x=150,y=100)

but3=Button(root,text="⌫",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:backspace())
but3.place(x=290,y=100)

but4=Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("/"))
but4.place(x=430,y=100)

but5=Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("7"))
but5.place(x=10,y=200)

but6=Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("8"))
but6.place(x=150,y=200)

but7=Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("9"))
but7.place(x=290,y=200)

but8=Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("*"))
but8.place(x=430,y=200)

but9=Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("4"))
but9.place(x=10,y=300)

but10=Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("5"))
but10.place(x=150,y=300)

but11=Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("6"))
but11.place(x=290,y=300)

but12=Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("-"))
but12.place(x=430,y=300)

but13=Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("1"))
but13.place(x=10,y=400)

but14=Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("2"))
but14.place(x=150,y=400)

but15=Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("3"))
but15.place(x=290,y=400)

but16=Button(root,text="0",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("0"))
but16.place(x=10,y=500)

but17=Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("."))
but17.place(x=150,y=500)

but18=Button(root,text="=",width=10,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="orange",padx=10,command=lambda:cal())
but18.place(x=290,y=500)

but19=Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="white",bg="dark slate gray",command=lambda:show("+"))
but19.place(x=430,y=400)

root.mainloop()