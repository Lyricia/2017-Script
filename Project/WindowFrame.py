from tkinter import *
from tkinter import font

g_Tk = Tk()
g_Tk.geometry("500x600+750+200")

def InitTopText():
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[Seoul Bus]")
    MainText.pack()
    MainText.place(x=20)


def InitRenderText():
    global txtOutput, txtOutput2

    #text box frame 1
    txtFrame = Frame(g_Tk, borderwidth=1, relief="sunken")
    txtOutput = Text(txtFrame, wrap=NONE, height=28, width=24, borderwidth=0)
    vscroll = Scrollbar(txtFrame, orient=VERTICAL, command=txtOutput.yview)
    txtOutput['yscroll'] = vscroll.set

    vscroll.pack(side="right", fill="y")
    txtOutput.pack(side="left", fill="both", expand=True)

    txtFrame.place(x=10, y=200)
    txtOutput.configure(state="disabled")

    #text box frame 2
    txtFrame2 = Frame(g_Tk, borderwidth=1, relief="sunken")
    txtOutput2 = Text(txtFrame2, wrap=NONE, height=28, width=24, borderwidth=0)
    vscroll2 = Scrollbar(txtFrame2, orient=VERTICAL, command=txtOutput2.yview)
    txtOutput2['yscroll'] = vscroll2.set

    vscroll2.pack(side="right", fill="y")
    txtOutput2.pack(side="left", fill="both", expand=True)

    txtFrame2.place(x=200, y=200)
    txtOutput2.configure(state="disabled")

    #Search Box


def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=20, weight='bold', family='Consolas')
    InputLabel = Text(g_Tk, wrap=NONE, font = TempFont ,height=1, width=10, borderwidth=1)
    InputLabel.pack()
    InputLabel.place(x=10, y=105)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="검색", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def SearchButtonAction():
    global SearchListBox, input

    input = InputLabel.get("1.0", END)
    txtOutput.configure(state="normal")

    txtOutput.insert(END, input)
    txtOutput.configure(state="disabled")

def key(event):
    if event.char == 't':
        txtOutput.configure(state="normal")

        txtOutput.insert(END, input)
        txtOutput.insert(END, "\n")
        txtOutput.configure(state="disabled")

    elif event.char == 'y':
        txtOutput2.configure(state="normal")

        txtOutput2.insert(END, "abab\n")
        txtOutput2.configure(state="disabled")

    elif event.char == 'q':
        quit()


g_Tk.bind("<Key>", key)

InitTopText()
InitRenderText()
InitInputLabel()
InitSearchButton()


g_Tk.mainloop()

