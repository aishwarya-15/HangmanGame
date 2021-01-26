import sys
from tkinter import Tk
from tkinter import *
from tkinter import font
global hid_input,hid_word,chances,dashes
def hide():
    global hid_word,hid_input,dashes,chances
    hid_word=hid_input.get()
    hid_input.grid_remove()
    dashes = ['-'] * len(hid_word)
    chances= 10

def get_move():
    global hid_word,chances,letter_input,chance,hid_input,present,dash
    letter=letter_input.get().lower()
    if len(letter)>1:
        present['text']="Please enter only letter!!"
        present.pack()
    else:
        if letter in hid_word:
            present['text']="Guessed letter present in word!!"
            for x in range(len(hid_word)):
                if letter==hid_word[x]:
                    dashes[x]=letter
        else:
            present['text']="Guessed letter not present in word!"
        chances-=1
        dash['text']=''.join([x +' ' for x in dashes])
        dash.pack()
        chance['text']="chances left : "+str(chances)
        chance.pack()
        check_win()
    letter_input.delete(0,'end')
def check_win():
    global chances,hid_word,dashes
    global present,dash,chance
    if chances==0:
        present['text']="You lost! The hidden word was "+hid_word
        present.pack()
        chance.pack_forget()
    else:
        #str_dashes=''.join(dashes)
        if dash['text'].find('-')==-1:
            present['text']="Hurrah!! You won the game!!!"
            present.pack()
            chance.pack_forget()

root = Tk()
ff = font.Font(size='25')
head = Label(root, text="Hangman Game")
head['font'] = ff
head.pack()
f0 = Frame(root)
f1 = Frame(root)
f2 = Frame(root)
f = Frame(root)
f0.pack()
f.pack()
f1.pack()
f2.pack()
hid =Label(f0,text="Set the hidden word:")
hid['font'] =ff
hid.pack()
hid_input = Entry(f)
hid_input['font'] = ff
hid_input.grid(row=0, column=1)
btnn = Button(f, text="Hide",command=hide)
btnn['font'] = font.Font(size='19')
btnn.grid(row=0, column=2)
imgg = PhotoImage(file='C:\\Users\\ELCOT\\PycharmProjects\\hangman\\img\\hangman_step6.png')
img = Label(f1, image=imgg)
img['font'] = ff
img.pack()
dash = Label(f1, text='- ' * 7)
dash['font'] = ff
dash.pack()
chance = Label(f1)
chance['font'] = ff
chance.pack()
present = Label(f1, text="Start the Game")
present['font'] = ff
present.pack()
letter_input = Entry(f2)
letter_input['font'] = ff
letter_input.grid(row=0, column=0)
btn = Button(f2, text="Guess", command=get_move)
btn['font'] = font.Font(size='19')
btn.grid(row=0, column=1)
root.mainloop()
