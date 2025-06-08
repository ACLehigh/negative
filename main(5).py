import tkinter as tk

from tkmacosx import Button

def Num():

    value=entry1.get()

    value=int(value)

    if value%2==0 and value<0:

        label2.configure(text=f'{value} is an even negative number.')

    elif value%2==1 and value<0:

        label2.configure(text=f'{value} is an odd negative number.')

    elif value%2==0 and value>0:

        label2.configure(text=f'{value} is an even positive number.')

    elif value%2==1 and value>0:

        label2.configure(text=f'{value} is an odd positive number.')

    else:

        label2.configure(text=f'Your number is zero.')

win=tk.Tk()

win.geometry("1920x1080")

label1=tk.Label(win,font=("Garamond", 35), text="Enter your integer.")

label1.place(relx=0.43,rely=0.1)

label2=tk.Label(win,font=("Garamond", 30))

label2.place(relx=0.457,rely=0.5)

entry1=tk.Entry(win,font=("Garamond", 20))

entry1.place(relx=0.45, rely=0.3)

button1=tk.Button(win,font=("Garamond", 15), text="Submit", command=Num)

button1.place(relx=0.52, rely=0.35)

win.mainloop()