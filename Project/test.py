from tkinter import *

top = Tk()
top.geometry("700x800+750+200")


def onselect(evt = 0):
    # Note here that Tkinter passes an event object to onselect()
    #w = evt.widget
    index = int(lb.curselection()[0])
    #value = w.get(index)
    value = lb.get(index)
    print('You selected item %d: "%s"' % (index, value))

openbrowserbutton = Button(top, command=onselect)
openbrowserbutton.pack()
openbrowserbutton.config(width=10, height=2)
openbrowserbutton.place(x=425, y=95)

lb = Listbox(top, name='lb')
lb.bind('<<ListboxSelect>>', onselect)

lb.insert(1, "Python")
lb.insert(2, "Perl")
lb.insert(3, "C")
lb.insert(4, "PHP")
lb.insert(5, "JSP")
lb.insert(6, "Ruby")

lb.pack()
top.mainloop()