from tkinter import *
from tkinter import font
from tkinter import messagebox

from LoadRouteList import *
from getRouteInfo import *
from getStationbyRoute import *
from getCurrentBusPosbyRoute import *
from getStationInfo import *


g_Tk = Tk()
g_Tk.geometry("700x800+750+200")

def InitTopText():
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[Seoul Bus]")
    MainText.pack()
    MainText.place(x=20)


def InitRenderText():
    global txtOutput, txtOutput2
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    #text box frame 1
    txtFrame = Frame(g_Tk, borderwidth=1, relief="sunken")
    txtOutput = Text(txtFrame, font = TempFont, wrap=NONE, height=28, width=27, borderwidth=0)
    vscroll = Scrollbar(txtFrame, orient=VERTICAL, command=txtOutput.yview)
    txtOutput['yscroll'] = vscroll.set

    vscroll.pack(side="right", fill="y")
    txtOutput.pack(side="left", fill="both", expand=True)

    txtFrame.place(x=30, y=200)
    txtOutput.configure(state="disabled")

    #text box frame 2
    txtFrame2 = Frame(g_Tk, borderwidth=1, relief="sunken")
    txtOutput2 = Text(txtFrame2, font = TempFont, wrap=NONE, height=28, width=27, borderwidth=0)
    vscroll2 = Scrollbar(txtFrame2, orient=VERTICAL, command=txtOutput2.yview)
    txtOutput2['yscroll'] = vscroll2.set

    vscroll2.pack(side="right", fill="y")
    txtOutput2.pack(side="left", fill="both", expand=True)

    txtFrame2.place(x=330, y=200)
    txtOutput2.configure(state="disabled")

    #Search Box


def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    InputLabel = Text(g_Tk, wrap=NONE, font = TempFont, height=1, width=25, borderwidth=1)
    InputLabel.pack()
    InputLabel.place(x=30, y=105)
    InputLabel.bind('<Return>', disableEnter)

def disableEnter(event):
    return 'break'

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="Search", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def SearchButtonAction():
    global SearchListBox, userInput, RouteBaseInfo, RouteStationData

    print("search")
    userInput = InputLabel.get("1.0", END)
    userInput = userInput.replace('\n','')
    if userInput in routelist:
        RouteBaseInfo = getRouteInfo(routelist[userInput])
        RouteStationData = getStationInfoByRoute(routelist[userInput])
        InitData(routelist[userInput])
        RenderInfo()
    else:
        messagebox.showerror('Error','Invalid Route Name')

def key(event):
    if event.char == 't':
        txtOutput.configure(state="normal")

        txtOutput.insert(END, input)
        txtOutput.configure(state="disabled")

    elif event.char == 'y':
        txtOutput2.configure(state="normal")

        txtOutput2.insert(END, "abab\n")
        txtOutput2.configure(state="disabled")

    elif event.char == 'q':
        quit()

def InitData(RouteID):
    global Route1, Route2

    RouteBaseInfo = getRouteInfo(RouteID)
    RouteStationData = getStationInfoByRoute(RouteID)

    Route1 = list()
    Route2 = list()
    Route1Counter = 0
    Route2Counter = 0
    for data in RouteStationData:
        if (RouteBaseInfo.get('EndStation') == data.get('direction') and
                    data.get('direction') != data.get('StationName')):
            data['index'] = Route1Counter
            Route1.append(data)
            Route1Counter += 1

        elif (data.get('direction') == data.get('StationName') or
                      RouteBaseInfo.get('EndStation') != data.get('direction')):
            data['index'] = Route2Counter
            Route2.append(data)
            Route2Counter += 1

    CurrentBusPos = getCurrentBusPosByRoute(RouteID)

    txtOutput.configure(state="normal")
    txtOutput2.configure(state="normal")
    for item in CurrentBusPos:
        BusIndex = int(item.get('StationIndex')) - 1
        if BusIndex < Route1.__len__():
            Route1[BusIndex]['IsBusArrived'] = True
        elif BusIndex >= Route1.__len__():
            BusIndex = BusIndex - Route1.__len__()
            Route2[BusIndex]['IsBusArrived'] = True


def BindPostionToRoute(Route1, Route2, pos):
    pass

def RenderInfo():
    txtOutput.delete('1.0', END)
    txtOutput2.delete('1.0', END)
    txtOutput.configure(state="normal")
    txtOutput2.configure(state="normal")
    for item in Route1:
        if item['IsBusArrived']:
            txtOutput.insert(END, '-> ')
        else:
            txtOutput.insert(END, '   ')
        txtOutput.insert(END, item['StationName'])
        txtOutput.insert(END, '\n')

    for item in Route2:
        if item['IsBusArrived']:
            txtOutput2.insert(END, '-> ')
        else:
            txtOutput2.insert(END, '   ')
        txtOutput2.insert(END, item['StationName'])
        txtOutput2.insert(END, '\n')
    txtOutput.configure(state="disabled")
    txtOutput2.configure(state="disabled")

g_Tk.bind("<Key>", key)

InitTopText()
InitRenderText()
InitInputLabel()
InitSearchButton()


routelist = loadRouteListfromFile()
testBusRouteID = routelist['507']

RouteBaseInfo = getRouteInfo(testBusRouteID)
RouteStationData = getStationInfoByRoute(testBusRouteID)

InitData(testBusRouteID)

RenderInfo()


g_Tk.mainloop()

