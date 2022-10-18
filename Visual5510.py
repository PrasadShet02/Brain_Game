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
def click10():
    #z.add(b1)
    b10['bg']='lightgrey'
    checking(b10)
    ad(b10)
def click11():
    #z.add(b11)
    b11['bg']='lightgrey'
    checking(b11)
    ad(b11)
def click12():
    #z.add(b3)
    b12['bg']='lightgrey'
    checking(b12)
    ad(b12)
def click13():
    #z.add(b13)
    b13['bg']='lightgrey'
    checking(b13)
    ad(b13)
def click14():
    #z.add(b14)
    b14['bg']='lightgrey'
    checking(b14)
    ad(b14)
def click15():
    #z.add(b6)
    b15['bg']='lightgrey'
    checking(b15)
    ad(b15)
def click16():
    #z.add(b16)
    b16['bg']='lightgrey'
    checking(b16)
    ad(b16)
def click17():
    #z.add(b17)
    b17['bg']='lightgrey'
    checking(b17)
    ad(b17)
def click18():
    #z.add(b18)
    b18['bg']='lightgrey'
    checking(b18)
    ad(b18)
def click19():
    #z.add(b3)
    b19['bg']='lightgrey'
    checking(b19)
    ad(b19)
def click20():
    #z.add(b20)
    b20['bg']='lightgrey'
    checking(b20)
    ad(b20)
def click21():
    #z.add(b21)
    b21['bg']='lightgrey'
    checking(b21)
    ad(b21)
def click22():
    #z.add(b6)
    b22['bg']='lightgrey'
    checking(b22)
    ad(b22)
def click23():
    #z.add(b23)
    b23['bg']='lightgrey'
    checking(b23)
    ad(b23)
def click24():
    #z.add(b24)
    b24['bg']='lightgrey'
    checking(b24)
    ad(b24)
def click25():
    #z.add(b25)
    b25['bg']='lightgrey'
    checking(b25)
    ad(b25)

b1=Button(root,text="",padx=20,pady=20,bg="white",command=click1)
b1.grid(row=0,column=0)
b2=Button(root,text="",padx=20,pady=20,bg="white",command=click2)
b2.grid(row=0,column=1)
b3=Button(root,text="",padx=20,pady=20,bg="white",command=click3)
b3.grid(row=0,column=2)
b4=Button(root,text="",padx=20,pady=20,bg="white",command=click4)
b4.grid(row=0,column=3)
b5=Button(root,text="",padx=20,pady=20,bg="white",command=click5)
b5.grid(row=0,column=4)
b6=Button(root,text="",padx=20,pady=20,bg="white",command=click6)
b6.grid(row=1,column=0)
b7=Button(root,text="",padx=20,pady=20,bg="white",command=click7)
b7.grid(row=1,column=1)
b8=Button(root,text="",padx=20,pady=20,bg="white",command=click8)
b8.grid(row=1,column=2)
b9=Button(root,text="",padx=20,pady=20,bg="white",command=click9)
b9.grid(row=1,column=3)
b10=Button(root,text="",padx=20,pady=20,bg="white",command=click10)
b10.grid(row=1,column=4)
b11=Button(root,text="",padx=20,pady=20,bg="white",command=click11)
b11.grid(row=2,column=0)
b12=Button(root,text="",padx=20,pady=20,bg="white",command=click12)
b12.grid(row=2,column=1)
b13=Button(root,text="",padx=20,pady=20,bg="white",command=click13)
b13.grid(row=2,column=2)
b14=Button(root,text="",padx=20,pady=20,bg="white",command=click14)
b14.grid(row=2,column=3)
b15=Button(root,text="",padx=20,pady=20,bg="white",command=click15)
b15.grid(row=2,column=4)
b16=Button(root,text="",padx=20,pady=20,bg="white",command=click16)
b16.grid(row=3,column=0)
b17=Button(root,text="",padx=20,pady=20,bg="white",command=click17)
b17.grid(row=3,column=1)
b18=Button(root,text="",padx=20,pady=20,bg="white",command=click18)
b18.grid(row=3,column=2)
b19=Button(root,text="",padx=20,pady=20,bg="white",command=click19)
b19.grid(row=3,column=3)
b20=Button(root,text="",padx=20,pady=20,bg="white",command=click20)
b20.grid(row=3,column=4)
b21=Button(root,text="",padx=20,pady=20,bg="white",command=click21)
b21.grid(row=4,column=0)
b22=Button(root,text="",padx=20,pady=20,bg="white",command=click22)
b22.grid(row=4,column=1)
b23=Button(root,text="",padx=20,pady=20,bg="white",command=click23)
b23.grid(row=4,column=2)
b24=Button(root,text="",padx=20,pady=20,bg="white",command=click24)
b24.grid(row=4,column=3)
b25=Button(root,text="",padx=20,pady=20,bg="white",command=click25)
b25.grid(row=4,column=4)
    
butset=set([b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25])

def colorswitch(x):
        x.config(bg='grey')
        x.after(2000,lambda: x.config(bg='white'))
        
y=set(random.sample(butset,10))
for i in y:
    colorswitch(i)

def ad(r):
    if r in y:
        w.add(r)
        if len(w)==10:
            import Visual6611
            root.destroy()
            exit()

def checking(s):
    if s in y:
        l2=Label(root,text='Correct!')
        l2.grid(row=5,column=2)
    else:
        l2=Label(root,text='Incorrect!')
        l2.grid(row=5,column=2)
        mb.showinfo("Visual memory","Oops, thanks for playing! You cleared 6 levels!")
        root.destroy()
        exit()

root.mainloop()
