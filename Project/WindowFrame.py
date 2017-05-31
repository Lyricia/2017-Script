from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import ttk

from LoadRouteList import *
from getRouteInfo import *
from getStationbyRoute import *
from getCurrentBusPosbyRoute import *
from getStationInfo import *
from getStationbyRoute import *


g_Tk = Tk()
g_Tk.geometry("700x800+750+200")

def InitTopText():
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[Seoul Bus]")
    MainText.pack()
    MainText.place(x=20)
    g_Tk.bind("<Key>", key)

def InitRenderText():
    global txtOutput, txtOutput2, RouteSearchBox
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')

    #text box frame 1
    txtFrame = Frame(frame2, borderwidth=1, relief="sunken")
    txtOutput = Text(txtFrame, font = TempFont, wrap=NONE, height=28, width=27, borderwidth=0)
    vscroll = Scrollbar(txtFrame, orient=VERTICAL, command=txtOutput.yview)
    txtOutput['yscroll'] = vscroll.set

    vscroll.pack(side="right", fill="y")
    txtOutput.pack(side="left", fill="both", expand=True)

    txtFrame.place(x=0, y=0)
    txtOutput.configure(state="disabled")

    #text box frame 2
    txtFrame2 = Frame(frame2, borderwidth=1, relief="sunken")
    txtOutput2 = Text(txtFrame2, font = TempFont, wrap=NONE, height=28, width=27, borderwidth=0)
    vscroll2 = Scrollbar(txtFrame2, orient=VERTICAL, command=txtOutput2.yview)
    txtOutput2['yscroll'] = vscroll2.set

    vscroll2.pack(side="right", fill="y")
    txtOutput2.pack(side="left", fill="both", expand=True)

    txtFrame2.place(x=300, y=0)
    txtOutput2.configure(state="disabled")

    #Search Box
    txtFrame3 = Frame(frame1, borderwidth=1, relief="sunken")
    RouteSearchBox = Text(txtFrame3, font=TempFont, wrap=NONE, height=28, width=27, borderwidth=0)
    vscroll3 = Scrollbar(txtFrame3, orient=VERTICAL, command=RouteSearchBox.yview)
    RouteSearchBox['yscroll'] = vscroll3.set

    vscroll3.pack(side="right", fill="y")
    RouteSearchBox.pack(side="left", fill="both", expand=True)

    txtFrame3.place(x=0, y=0)
    RouteSearchBox.configure(state="disabled")

def InitSearchBox():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    InputLabel = Text(g_Tk, wrap=NONE, font = TempFont, height=1, width=25, borderwidth=1)
    InputLabel.pack()
    InputLabel.place(x=30, y=105)
    InputLabel.bind('<Return>', eventEnter)

def eventEnter(event):
    SearchButtonAction()
    return 'break'

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="Search", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)

def callback(event, tag, cat):
    global RouteBaseInfo, RouteStationData, InputLabel

    index = event.widget.index("@%s,%s" % (event.x, event.y))
    idx = int(index[0:index.find('.')]) - 1

    if cat == 'route':
        tag = 'tag_route' + str(idx)
        selectRoute = event.widget.get('%s.first' % tag, '%s.last' % tag)
        InputLabel.delete('1.0', END)
        InputLabel.insert(END, selectRoute)
        Tab.select(frame2)
        RouteBaseInfo = getRouteInfo(routelist[selectRoute])
        RouteStationData = getStationInfoByRoute(routelist[selectRoute])
        InitData(routelist[selectRoute])
        RenderInfo()
    elif cat == 'stationA' or cat == 'stationB':
        if cat == 'stationB':
            idx = idx + len(Route1)
            tag = 'tag_station' + str(idx)
        else:

            tag = 'tag_station' + str(idx)
        selectRoute = event.widget.get('%s.first' % tag, '%s.last' % tag)
        arrivaldata = getStationInfo(RouteStationData[idx].get('StationID'))
        for data in arrivaldata:
            pass


        messagebox.showinfo(selectRoute, 'First Bus : {0}\nSecond Bus : {1}'.
                            format(arrivaldata['arrivetime1'],arrivaldata['arrivetime2']))
        print('')


    print(selectRoute)

def SearchButtonAction():
    global SearchListBox, userInput, RouteBaseInfo, RouteStationData

    print("search")
    userInput = InputLabel.get("1.0", END)
    userInput = userInput.replace('\n','')
    if userInput in routelist:
        Tab.select(frame2)
        RouteBaseInfo = getRouteInfo(routelist[userInput])
        RouteStationData = getStationInfoByRoute(routelist[userInput])
        InitData(routelist[userInput])
        RenderInfo()

    else:
        Tab.select(frame1)
        dataexist = 0
        datacounter = 0
        RouteSearchBox.configure(state = 'normal')
        RouteSearchBox.delete('1.0', END)
        for data in routelist:
            if userInput in data:
                tag = "tag_route" + str(datacounter)
                if datacounter%2 == 0:
                    RouteSearchBox.tag_config(tag, foreground="blue")
                else:
                    RouteSearchBox.tag_config(tag, foreground="green")
                RouteSearchBox.tag_bind(tag, '<Button-1>', lambda e: callback(e, tag, 'route'))
                RouteSearchBox.insert(END, data, tag)
                RouteSearchBox.insert(END, '\n')
                dataexist = 1
                datacounter+=1
        RouteSearchBox.configure(state="disabled")

        if not dataexist:
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
    global Route1, Route2, CurrentBusPos

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
    datacount = 0
    txtOutput.delete('1.0', END)
    txtOutput2.delete('1.0', END)
    txtOutput.configure(state="normal")
    txtOutput2.configure(state="normal")
    for item in Route1:
        tag = "tag_station" + str(datacount)
        txtOutput.tag_config(tag, foreground = 'blue')
        txtOutput.tag_bind(tag, '<Button-1>', lambda e: callback(e, tag, 'stationA'))
        if item['IsBusArrived']:
            txtOutput.insert(END, '-> ')
        else:
            txtOutput.insert(END, '   ')
        txtOutput.insert(END, item['StationName'], tag)
        txtOutput.insert(END, '\n')
        datacount += 1

    for item in Route2:
        tag = "tag_station" + str(datacount)
        txtOutput2.tag_config(tag, foreground='blue')
        txtOutput2.tag_bind(tag, '<Button-1>', lambda e: callback(e, tag, 'stationB'))
        if item['IsBusArrived']:
            txtOutput2.insert(END, '-> ')
        else:
            txtOutput2.insert(END, '   ')
        txtOutput2.insert(END, item['StationName'], tag)
        txtOutput2.insert(END, '\n')
        datacount += 1

    txtOutput.configure(state="disabled")
    txtOutput2.configure(state="disabled")

def InitTab():
    global Tab, frame1, frame2, frame3
    Tab = ttk.Notebook()
    Tab.pack()
    Tab.place(x=25, y=175)

    frame1 = ttk.Frame(Tab, width=600, height=550, relief=SOLID)
    frame2 = ttk.Frame(Tab, width=600, height=550, relief=SOLID)
    frame3 = ttk.Frame(Tab, width=600, height=550, relief=SOLID)

    Tab.add(frame1, text="노선검색")
    Tab.add(frame2, text="노선정보")
    Tab.add(frame3, text="   ")



InitTab()
InitTopText()
InitRenderText()
InitSearchBox()
InitSearchButton()
routelist = loadRouteListfromFile()


g_Tk.mainloop()

