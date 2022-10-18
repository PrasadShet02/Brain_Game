from tkinter import*
root=Tk()
root.title("A Brain Game")

def mq():
        import maths_quiz
def nm():
        import number_memory
def vm():
        import visual_memory

b101=Button(root,text='Maths Quiz',bg='lightblue',command=mq)
b201=Button(root,text='Number Memory',bg='lightblue',command=nm)
b301=Button(root,text='Visual Memory',bg='lightblue',command=vm)
b101.grid(row=0,column=0)
b201.grid(row=0,column=1)
b301.grid(row=0,column=2)

root.mainloop()
