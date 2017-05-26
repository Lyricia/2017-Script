from tkinter import *
from tkinter import font

from LoadRouteList import *
from getRouteInfo import *
from getStationbyRoute import *
from getCurrentBusPosbyRoute import *
from getStationInfo import *


g_Tk = Tk()
g_Tk.geometry("500x700+750+200")

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
    txtOutput = Text(txtFrame, font = TempFont, wrap=NONE, height=28, width=24, borderwidth=0)
    vscroll = Scrollbar(txtFrame, orient=VERTICAL, command=txtOutput.yview)
    txtOutput['yscroll'] = vscroll.set

    vscroll.pack(side="right", fill="y")
    txtOutput.pack(side="left", fill="both", expand=True)

    txtFrame.place(x=30, y=200)
    txtOutput.configure(state="disabled")

    #text box frame 2
    txtFrame2 = Frame(g_Tk, borderwidth=1, relief="sunken")
    txtOutput2 = Text(txtFrame2, font = TempFont, wrap=NONE, height=28, width=24, borderwidth=0)
    vscroll2 = Scrollbar(txtFrame2, orient=VERTICAL, command=txtOutput2.yview)
    txtOutput2['yscroll'] = vscroll2.set

    vscroll2.pack(side="right", fill="y")
    txtOutput2.pack(side="left", fill="both", expand=True)

    txtFrame2.place(x=230, y=200)
    txtOutput2.configure(state="disabled")

    #Search Box


def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=20, weight='bold', family='Consolas')
    InputLabel = Text(g_Tk, wrap=NONE, font = TempFont, height=1, width=10, borderwidth=1)
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


routelist = loadRouteListfromFile()
testBusRouteID = routelist['광진01']

RouteBaseInfo = getRouteInfo(testBusRouteID)
RouteStationData = getStationInfoByRoute(testBusRouteID)

print(RouteBaseInfo['EndStation'])
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

CurrentBusPos = getCurrentBusPosByRoute(testBusRouteID)

txtOutput.configure(state="normal")

for item in CurrentBusPos:
    BusIndex = int(item.get('StationIndex'))
    if BusIndex < Route1.__len__():
        Route1[BusIndex]['IsBusArrived'] = True
    elif BusIndex >= Route1.__len__():
        BusIndex = BusIndex-Route1.__len__()
        Route2[BusIndex]['IsBusArrived'] = True

for item in Route1:
    if item['IsBusArrived']:
        txtOutput.insert(END, '◎ ')
    else:
        txtOutput.insert(END, '   ')
    txtOutput.insert(END, item['StationName'])
    txtOutput.insert(END, '\n')

txtOutput.configure(state="disabled")

g_Tk.mainloop()

