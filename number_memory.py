from tkinter import *
import random
root=Tk()
root.title("Number memory")
i=0
s=0

def r():
    global y
    global i
    global s
    b1["state"]=DISABLED
    if i<5:

        y=str(random.randint(pow(10,i+2),pow(10,i+4)-1))
        l1=Label(root,text=str(y))
        l1.after(1500,lambda : l1.config(text=''))
        l1.grid(row=1)
        i=i+1
    else:
        l1=Label(root,text="YOUR SCORE IS "+str(s)).grid(row=1)
        b2["state"]=DISABLED
    
def gt():
    global y
    global z
    global i
    global s
    z=str(e1.get())
    if z==y:
        l2=Label(root,text="Correct",fg="green")
        l2.after(500,lambda : l2.config(text=''))
        l2.grid(row=3)
        s=s+1
        
    else:
        l2=Label(root,text="Incorrect",fg="red")
        l2.after(500,lambda : l2.config(text=''))
        l2.grid(row=3)
    
    e1.delete(0,END)
    r()


b1=Button(root,text="START",command=r)
b1.grid(row=0)
l1=Label(root,text="Enter the number displayed")
l1.after(1000,lambda : l1.config(text=''))
l1.grid(row=1)
e1=Entry(root,width = 35, borderwidth = 5)
e1.grid(row=2)
b2=Button(root,text="Enter",command=gt)
b2.grid(row=4)

root.mainloop()