from tkinter import*
from tkinter import messagebox as mb
root=Tk()
root.title("Visual Memory")
import random

#l1=Label(text="Memorize the buttons which light up!",fg="red",font="Helvetica")
#l1.grid(row=0,column=1)
z=set()
w=set()

def click1():
    #z.add(b1)
    b1['bg']='lightgrey'
    checking(b1)
    ad(b1)
def click2():
    #z.add(b2)
    b2['bg']='lightgrey'
    checking(b2)
    ad(b2)
def click3():
    #z.add(b3)
    b3['bg']='lightgrey'
    checking(b3)
    ad(b3)
def click4():
    #z.add(b4)
    b4['bg']='lightgrey'
    checking(b4)
    ad(b4)
def click5():
    #z.add(b5)
    b5['bg']='lightgrey'
    checking(b5)
    ad(b5)
def click6():
    #z.add(b6)
    b6['bg']='lightgrey'
    checking(b6)
    ad(b6)
def click7():
    #z.add(b7)
    b7['bg']='lightgrey'
    checking(b7)
    ad(b7)
def click8():
    #z.add(b8)
    b8['bg']='lightgrey'
    checking(b8)
    ad(b8)
def click9():
    #z.add(b9)
    b9['bg']='lightgrey'
    checking(b9)
    ad(b9)

b1=Button(root,text="",padx=20,pady=20,bg="white",command=click1)
b1.grid(row=1,column=0)
b2=Button(root,text="",padx=20,pady=20,bg="white",command=click2)
b2.grid(row=1,column=1)
b3=Button(root,text="",padx=20,pady=20,bg="white",command=click3)
b3.grid(row=1,column=2)
b4=Button(root,text="",padx=20,pady=20,bg="white",command=click4)
b4.grid(row=2,column=0)
b5=Button(root,text="",padx=20,pady=20,bg="white",command=click5)
b5.grid(row=2,column=1)
b6=Button(root,text="",padx=20,pady=20,bg="white",command=click6)
b6.grid(row=2,column=2)
b7=Button(root,text="",padx=20,pady=20,bg="white",command=click7)
b7.grid(row=3,column=0)
b8=Button(root,text="",padx=20,pady=20,bg="white",command=click8)
b8.grid(row=3,column=1)
b9=Button(root,text="",padx=20,pady=20,bg="white",command=click9)
b9.grid(row=3,column=2)
    
butset=set([b1,b2,b3,b4,b5,b6,b7,b8,b9])

def colorswitch(x):
        x.config(bg='grey')
        x.after(2000,lambda: x.config(bg='white'))
        
y=set(random.sample(butset,4))
for i in y:
    colorswitch(i)

def ad(r):
    if r in y:
        w.add(r)
        if len(w)==4:
            import Visual445
            root.destroy()
            exit()
            
def checking(s):
    if s in y:
        l2=Label(root,text='Correct!')
        l2.grid(row=4,column=1)
    else:
        l2=Label(root,text='Incorrect!')
        l2.grid(row=4,column=1)
        mb.showinfo("Visual memory","Oops, thanks for playing!")
        root.destroy()
        exit()

root.mainloop()
