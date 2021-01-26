from tkinter import Tk
from tkinter import *
from tkinter import font
root=Tk()
def print_letter():
    global letter
    print(letter.get())


ff=font.Font(size='25')
head=Label(root,text="Hangman Game")
head['font']=ff
head.pack()
f1=Frame(root)
f2=Frame(root)
f1.pack()
f2.pack()
imgg=PhotoImage(file='C:\\Users\\ELCOT\\PycharmProjects\\hangman\\img\\hangman_step6.png')
img=Label(f1,image=imgg)
img['font']=ff
img.pack()
dash=Label(f1,text='- '*7)
dash['font']=ff
dash.pack()
chance=Label(f1,text="chances left is : 10")
chance['font']=ff
chance.pack()
present=Label(f1,text="Letter found")
present['font']=ff
present.pack()
letter=Entry(f2)
letter['font']=ff
letter.grid(row=0,column=0)
btn=Button(f2,text="Guess",command=print_letter)
btn['font']=ff
btn.grid(row=0,column=1)
root.mainloop()
