from tkinter import *

g_Tk = Tk()
g_Tk.geometry("700x800+750+200")
def function():
    selection = var.get()

    if  selection == 1:
        print("1")

    elif selection == 2:
        print("2")
        # User-defined

    else:#selection==0
        print("no")

        #No choice

var = IntVar()
r1 = Radiobutton(g_Tk, text = "default", variable = var, value = 1)
r2 = Radiobutton(g_Tk, text = "user-defined", variable = var, value = 2)

r1.place(x=20)
r2.place(x=70)


SearchButton = Button(g_Tk, text="Search", command=function)
SearchButton.pack()


mainloop()