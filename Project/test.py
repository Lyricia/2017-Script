from tkinter import *

def showgui():
    win = Tk()

    area = Text(win, width = 50, height = 20)
    area.pack()

    new = """Lots of text here
    and here
    and here..."""
    area.insert("1.0", new)

    area.tag_add(SEL, "1.0", END)
    area.focus_set()
    win.mainloop()

if __name__ == "__main__":
    showgui()