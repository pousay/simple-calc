#modules
#dev: telegram => @Better_call_p0ry
from tkinter import *
import time

#app
window = Tk()
window.maxsize(260,430)
window.minsize(260,430)
window.title('MyCalculator')
window.configure(bg = "gray5")

#text
operator = ""



#functions

def clean():
    global operator
    operator = ""
    lblmain.config(text = "",bg = 'gray12',font=(("Arial",15,"bold")),fg = "white")
    lblmain.place(x = 15,y = 20,width=230,height=50)

def back():
    global operator

    operator = operator[:-1]

    lblmain.config(text = operator,bg = 'gray12',font=(("Arial",15,"bold")),fg = "white")
    lblmain.place(x = 15,y = 20,width=230,height=50)
def equel() :
    global operator

    if len(operator) < 18 :
        oper = eval(operator)
        operator = str(oper)
        lblmain.config(text = oper,bg = 'gray12',font=(("Arial",15,"bold")),fg = "white")
        lblmain.place(x = 15,y = 20,width=230,height=50)
    else: 
        lblmain.config(text = "to much numbers",bg = 'gray12',font=(("Arial",15,"bold")),fg = "white")
        lblmain.place(x = 15,y = 20,width=230,height=50)

def handleEvents(num):
    global operator
    if num == 0 and len(operator) <= 1 and operator[0] == 0:
        operator = "" 
    else : 
        operator = operator + str(num)
    lblmain.config(text = operator,bg = 'gray12',font=(("Arial",15,"bold")),fg = "white")
    lblmain.place(x = 15,y = 20,width=230,height=50)









#label
lblmain = Label(text = "",bg = 'gray12',font=(("Arial",15,"bold")),fg = "white")
lblmain.place(x = 15,y = 20,width=230,height=50)

#buttons
#row 1
btnclean = Button(text = " Clean ",font = ("Arial",15,"bold"),bg = "lawn green",command=clean)
btnclean.place(x = 15,y=150,width=120,height=40)

btndarsad = Button(text = "%",font=("Arial",15,"bold"),bg = "lawn green",command= lambda :handleEvents('/100'))
btndarsad.place(x = 140,y=150,width=50,height=40)

btntaq = Button(text = "÷",font=("Arial",25,"bold"),bg ="lawn green",command= lambda :handleEvents("/"))
btntaq.place(x = 195,y = 150,width=50,height=40)


#row
btn7 = Button(text = '7',font =("Arial",20,"bold"),bg = "snow4",command= lambda:handleEvents(7))
btn7.place(x = 15,y = 205,height=40,width=50)

btn8 = Button(text = "8",font =("Arial",20,"bold"),bg = "snow4",command= lambda:handleEvents(8))
btn8.place(x = 75,y = 205,height=40,width=50)

btn9 = Button(text = "9",font =("Arial",20,"bold"),bg = "snow4",command= lambda:handleEvents(9))
btn9.place(x = 135,y = 205,height=40,width=50)

btnx = Button(text = "X",font =("Arial",20,"bold"),bg = "lawn green",command=lambda :handleEvents("*"))
btnx.place(x = 195,y = 205,height=40,width=50)



#row 3
btn4 = Button(text = "4",font =("Arial",20,"bold"),bg = "snow4",command=lambda : handleEvents(4))
btn4.place(x = 15,y = 260,height=40,width=50)

btn5 = Button(text = "5",font =("Arial",20,"bold"),bg = "snow4",command=lambda : handleEvents(5))
btn5.place(y=260,x=75,height=40,width=50)

btn6 = Button(text = "6",font =("Arial",20,"bold"),bg = "snow4",command=lambda : handleEvents(6))
btn6.place(y=260,x = 135,height=40,width=50)

btnmenha = Button(text = "-",font =("Arial",20,"bold"),bg = "lawn green",command=lambda :handleEvents("-"))
btnmenha.place(y=260,x = 195,height=40,width=50)



#row 4
btn1 = Button(text = "1",font = ("Arial",20,"bold"),bg = "snow4",command=lambda : handleEvents(1))
btn1.place(y = 315,x = 15,width=50,height=40)

btn2 = Button(text = "2",font = ("Arial",20,"bold"),bg = "snow4",command=lambda : handleEvents(2))
btn2.place(y = 315,x = 75,width=50,height=40)

btn3 = Button(text = "3",font = ("Arial",20,"bold"),bg = "snow4",command=lambda : handleEvents(3))
btn3.place(y = 315,x = 135,width=50,height=40)

btnplus = Button(text = "+",font = ("Arial",20,"bold"),bg = "lawn green" ,command= lambda :handleEvents('+'))
btnplus.place(y = 315,x = 195,width=50,height=40)

#row akhar(5)

btn0 = Button(text = " 0 ",font = ("Arial",15,"bold"),bg = "snow4",command=lambda :handleEvents(0))
btn0.place(x = 15,y=370,width=120,height=40)

btndot = Button(text = ".",font=("Arial",15,"bold"),bg = "snow4",command=lambda :handleEvents("."))
btndot.place(x = 140,y=370,width=50,height=40)

btneq = Button(text = "=",font=("Arial",25,"bold"),bg = "lawn green",command=equel)
btneq.place(x = 195,y = 370,width=50,height=40)

btnback = Button(text = "back",fg="black",font=("Arial",15,"bold"),bg = "lawn green",command=back)
btnback.place(x = 15,y = 100,width=230,height=40)





window.mainloop()
