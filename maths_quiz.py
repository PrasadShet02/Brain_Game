from tkinter import *
import random

root=Tk()
root.title("Maths Quiz")
score=0
que_count=0
number_of_questions=10


def start_button():
    global que_count, user_input, score
    start_b=Button(root,text="Change Question",command=question_generator).grid(row=0, column=1)
    if (que_count<number_of_questions):
        question_generator()
        user_input=Entry(root,width=40,borderwidth=10)
        user_input.grid(column = 0 ,row = 2 ,  columnspan = 3 , padx = 20, pady = 30)
        que_count=que_count+1
    else:
        user_input=Label(root,text="YOUR SCORE IS "+str(score)).grid(column = 0 ,row = 2 ,  columnspan = 3 , padx = 20, pady = 30)
        bt0["state"]=DISABLED
        bt1["state"]=DISABLED
        bt2["state"]=DISABLED
        bt3["state"]=DISABLED
        bt4["state"]=DISABLED
        bt5["state"]=DISABLED
        bt6["state"]=DISABLED
        bt7["state"]=DISABLED
        bt8["state"]=DISABLED
        bt9["state"]=DISABLED
        bt0["state"]=DISABLED
        bts["state"]=DISABLED
        btd["state"]=DISABLED
        bte["state"]=DISABLED
        btc["state"]=DISABLED

def question_generator():
    global n1,n2,v
    n1=random.randint(10,21)
    n2=random.randint(3,11)
    a=[add_que,multiply_que,subtract_que,divide_que]
    v=random.choice(a)
    v()

def add_que():
    global l_que
    l_que=Label(root,text=str(n1)+" + "+str(n2),font="Times 32 bold").grid(row=1, column = 1)

def multiply_que():
    global l_que
    l_que=Label(root,text=str(n1)+" * "+str(n2),font="Times 32 bold").grid(row=1, column = 1)

def subtract_que():
    global l_que
    l_que=Label(root,text=str(n1)+" - "+str(n2),font="Times 32 bold").grid(row=1, column = 1)

def divide_que():
    global l_que
    l_que=Label(root,text=str(n1)+" / "+str(n2),font="Times 32 bold").grid(row=1, column = 1)


def click(number):
    global user_input
    current = user_input.get()
    user_input.delete(0,END)
    user_input.insert(0, str(current)+ str(number))


l_result=Label(root,text='')
l_result.grid(row=3,column=1)

def check_ans():
    global user_input
    global score
    if(user_input.get()==''):
        return
    z=float(user_input.get())
    if v==add_que:
        s=float(n1+n2)
        if(s==z):
            score=score+1
            l_result.config(text='CORRECT',fg="green")
            l_result.after(500,lambda : l_result.config(text=''))
        else:
            l_result.config(text='INCORRECT',fg="red")
            l_result.after(500,lambda : l_result.config(text=''))
            
            
    if v==multiply_que:
        s=float(n1*n2)
        if(s==z):
            score=score+1
            l_result.config(text='CORRECT',fg="green")
            l_result.after(500,lambda : l_result.config(text=''))
        else:
            l_result.config(text='INCORRECT',fg="red")
            l_result.after(500,lambda : l_result.config(text=''))
            
   

    if v==subtract_que:
        s=float(n1-n2)
        if(s==z):
            score=score+1
            l_result.config(text='CORRECT',fg="green")
            l_result.after(500,lambda : l_result.config(text=''))
        else:
            l_result.config(text='INCORRECT',fg="red")
            l_result.after(500,lambda : l_result.config(text=''))
            
    


    if v==divide_que:
        s=float(n1/n2)
        if(round(s,2)==round(z,2)):
            score=score+1
            l_result.config(text='CORRECT',fg="green")
            l_result.after(500,lambda : l_result.config(text=''))
        else:
            l_result.config(text='INCORRECT',fg="red")
            l_result.after(500,lambda : l_result.config(text=''))
            
    
    user_input.delete(0,END)

    start_button()

def clr():
    user_input.delete(0,END)



start_b=Button(root,text="START",command=lambda : start_button()).grid(row=0, column=1)

bt1 = Button(root, text = "1", padx = 40 , pady = 20, command = lambda : click(1))
bt2 = Button(root, text = "2", padx = 40 , pady = 20, command = lambda : click(2))
bt3 = Button(root, text = "3", padx = 40 , pady = 20, command = lambda : click(3))
bt4 = Button(root, text = "4", padx = 40 , pady = 20, command = lambda : click(4))
bt5 = Button(root, text = "5", padx = 40 , pady = 20, command = lambda : click(5))
bt6 = Button(root, text = "6", padx = 40 , pady = 20, command = lambda : click(6))
bt7 = Button(root, text = "7", padx = 40 , pady = 20, command = lambda : click(7))
bt8 = Button(root, text = "8", padx = 40 , pady = 20, command = lambda : click(8))
bt9 = Button(root, text = "9", padx = 40 , pady = 20, command = lambda : click(9))
bt0 = Button(root, text = "0", padx = 40 , pady = 20, command = lambda : click(0))
bts = Button(root, text = "-", padx = 40 , pady = 20, command = lambda : click("-"))
btd = Button(root, text = ".", padx = 40 , pady = 20, command = lambda : click("."))
bte = Button(root, text = "ENTER", padx = 40 , pady = 20, command = check_ans)
btc = Button(root, text = "CLEAR", padx = 40 , pady = 20, command = clr)


bt1.grid(row = 6, column = 0)
bt2.grid(row = 6, column = 1)
bt3.grid(row = 6, column = 2)

bt4.grid(row = 5, column = 0)
bt5.grid(row = 5, column = 1)
bt6.grid(row = 5, column = 2)

bt7.grid(row = 4, column = 0)
bt8.grid(row = 4, column = 1)
bt9.grid(row = 4, column = 2)

bt0.grid(row = 7, column = 0)
bte.grid(row = 8, column = 2)
btd.grid(row = 7, column = 1)
bts.grid(row = 7, column = 2)
btc.grid(row = 8, column = 1)

root.mainloop()