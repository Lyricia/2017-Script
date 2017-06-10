from tkinter import *

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

    master.quit()

master = Tk()
var = IntVar()
Label(master, text = "Select OCR language").grid(row=0, sticky=W)
Radiobutton(master, text = "default", variable = var, value = 1).grid(row=1, sticky=W)
Radiobutton(master, text = "user-defined", variable = var, value = 2).grid(row=2, sticky=W)
Button(master, text = "OK", command = function).grid(row=3, sticky=W)

mainloop()