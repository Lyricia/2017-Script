import webbrowser

from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import ttk

from LoadRouteList import *
from getRouteInfo import *
from getCurrentBusPosbyRoute import *
from getStationInfo import *
from getStationbyRoute import *
from getStationID import *
from EmailSender import *
import loadmod
import savemod

g_Tk = Tk()
g_Tk.geometry("700x800+750+200")
bookmarklist = list()

def MainInit():
    global routelist, routelist_inv
    InitTab()
    InitTopText()
    InitRenderText()
    InitSearchBox()
    InitRadioBtn()
    InitButton()
    InitBmkBtns()

    try:
        routelist = loadRouteListfromFile()
    except:
        routelist = loadRouteListfromAPI()
    routelist_inv = {v: k for k, v in routelist.items()}


    g_Tk.bind("<Key>", key)

def LoadBmkList():
    global BookmarkBox, bookmarklist
    BookmarkBox.delete(0, END)
    bookmarklist = loadmod.fileload(list()).split()
    for data in enumerate(bookmarklist):
        if data[0] % 2==0 :
            BookmarkBox.insert(END, data[1])

def SaveBmkList():
    global bookmarklist
    if savemod.filesave(bookmarklist) == 0:
        print("asd")

def EmailSendBtn():
    if bookmarklist:
        if SendEmail(bookmarklist):
            messagebox.showinfo("E-Mail", "Send Email Success")
    else:
        print("Empty Bookmark")

def InitRadioBtn():
    global r_Route, r_Station, radiovar
    radiovar = IntVar()
    radiovar.set(1)
    r_Route = Radiobutton(g_Tk, text="Route", variable = radiovar,  value=1)
    r_Station = Radiobutton(g_Tk, text="Station", variable = radiovar, value=2)
    r_Route.place(x=30, y= 130)
    r_Station.place(x=100, y= 130)

def InitTopText():
    TempFont = font.Font(g_Tk, size=40, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[Seoul Bus]")
    MainText.pack()
    MainText.place(x=20, y=10)

def InitRenderText():
    global txtOutput, txtOutput2, RouteSearchBox, BookmarkBox
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')

    #text box frame 1
    txtFrame = Frame(frame2, borderwidth=1, relief="sunken")
    txtOutput = Text(txtFrame, font = TempFont, wrap=NONE, height=28, width=31, borderwidth=0)
    vscroll = Scrollbar(txtFrame, orient=VERTICAL, command=txtOutput.yview)
    txtOutput['yscroll'] = vscroll.set

    vscroll.pack(side="right", fill="y")
    txtOutput.pack(side="left", fill="both", expand=True)

    txtFrame.place(x=0, y=0)
    txtOutput.configure(state="disabled")

    #text box frame 2
    txtFrame2 = Frame(frame2, borderwidth=1, relief="sunken")
    txtOutput2 = Text(txtFrame2, font = TempFont, wrap=NONE, height=28, width=31, borderwidth=0)
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

    #Bookmark Frame box
    txtFrame4 = Frame(frame3, borderwidth=1, relief="sunken")
    BookmarkBox = Listbox(txtFrame4, font=TempFont, height=28, width=27, borderwidth=0)
    vscroll4 = Scrollbar(txtFrame4, orient=VERTICAL, command=BookmarkBox.yview)
    BookmarkBox['yscroll'] = vscroll4.set

    vscroll4.pack(side="right", fill="y")
    BookmarkBox.pack(side="left", fill="both", expand=True)

    txtFrame4.place(x=0, y=0)
    BookmarkBox.configure(state='normal')


def InitSearchBox():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    InputLabel = Text(g_Tk, wrap=NONE, font = TempFont, height=1, width=25, borderwidth=1)
    InputLabel.pack()
    InputLabel.place(x=30, y=100)
    InputLabel.bind('<Return>', eventEnter)

def InitTab():
    global Tab, frame1, frame2, frame3
    Tab = ttk.Notebook()
    Tab.pack()
    Tab.place(x=25, y=175)

    frame1 = ttk.Frame(Tab, width=600, height=540, relief=SOLID)
    frame2 = ttk.Frame(Tab, width=600, height=540, relief=SOLID)
    frame3 = ttk.Frame(Tab, width=600, height=540, relief=SOLID)
    Tab.add(frame1, text="   검색   ")
    Tab.add(frame2, text=" 노선정보 ")
    Tab.add(frame3, text=" BOOKMARK ")

def eventEnter(event):
    SearchButtonAction()
    return 'break'

def InitButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family='Consolas')
    SearchButton = Button(g_Tk, font=TempFont, text="Search", command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.config(width=8, height=2)
    SearchButton.place(x=330, y=95)

    openbrowserbutton = Button(g_Tk, font=TempFont, text="ROUTE MAP", command=BrowserBtnAction)
    openbrowserbutton.pack()
    openbrowserbutton.config(width=10, height=2)
    openbrowserbutton.place(x=425, y=95)

    RefreshBtn = Button(g_Tk, font=TempFont, text="Refresh", command=RefreshBtnAction)
    RefreshBtn.pack()
    RefreshBtn.config(width = 10, height = 2)
    RefreshBtn.place(x=540, y=95)

    AddBookMarkBtn = Button(g_Tk, font=TempFont, text="Add\nBookMark", command=AddBookMarkBtnAction)
    AddBookMarkBtn.pack()
    AddBookMarkBtn.config(width = 10, height = 2)
    AddBookMarkBtn.place(x=540, y=35)

    AddEmailingBtn = Button(g_Tk, font=TempFont, text="Send Email", command=EmailSendBtn)
    AddEmailingBtn.pack()
    AddEmailingBtn.config(width = 10, height = 2)
    AddEmailingBtn.place(x=425, y=35)

def RefreshBtnAction():
    if Tab.index(Tab.select()) == 1 :
        SearchButtonAction()
    messagebox.showinfo("refresh", "Refresh")

def InitBmkBtns():
    TempFont = font.Font(frame3, size=12, family='Consolas')
    EraseBmkBtn = Button(frame3, font=TempFont, text="Erase\nBookmark", command=EraseBmkBtnAction)
    EraseBmkBtn.pack()
    EraseBmkBtn.config(width=13, height=2)
    EraseBmkBtn.place(x=300, y=35)

    GotoInfoBtn = Button(frame3, font=TempFont, text="Go to\nInformation", command=GotoBmkInfoBtnAction)
    GotoInfoBtn.pack()
    GotoInfoBtn.config(width=13, height=2)
    GotoInfoBtn.place(x=450, y=35)

    SaveBmkListBtn = Button(frame3, font=TempFont, text="Save\nBookMark", command=SaveBmkList)
    SaveBmkListBtn.pack()
    SaveBmkListBtn.config(width=13, height=2)
    SaveBmkListBtn.place(x=300, y=100)

    LoadBmkListBtn = Button(frame3, font=TempFont, text="Load\nBookMark", command=LoadBmkList)
    LoadBmkListBtn.pack()
    LoadBmkListBtn.config(width=13, height=2)
    LoadBmkListBtn.place(x=450, y=100)

def BrowserBtnAction():
    tmp = InputLabel.get("1.0", END).replace('\n','')
    try:
        if routelist[tmp] : pass
        tmpurl = 'http://bus.go.kr/realBusLine6.jsp?strbusid={0}&wbustp=N'.format(routelist[tmp])
        webbrowser.open(tmpurl)

    except:
        messagebox.showerror("Error", "Invalid Input")

def GotoBmkInfoBtnAction():
    global RouteBaseInfo, RouteStationData
    try:
        index = int(BookmarkBox.curselection()[0])
        routeid = routelist[BookmarkBox.get(index)]
        Tab.select(frame2)
        RouteBaseInfo = getRouteInfo(routeid)
        RouteStationData = getStationInfoByRoute(routeid)
        InitData(routeid)
        RenderInfo()
    except:
        messagebox.showerror("Select Item","Select Item")
        return

def EraseBmkBtnAction():
    try:
        index = int(BookmarkBox.curselection()[0])
        bookmarklist.remove(BookmarkBox.get(index))
        bookmarklist.remove(routelist[BookmarkBox.get(index)])
        BookmarkBox.delete(index)
    except:
        messagebox.showerror("Select Item","Select Item")
        return

def AddBookMarkBtnAction():
    tmp = InputLabel.get("1.0", END).replace('\n', '')
    try:
        if routelist[tmp] in bookmarklist:
            messagebox.showerror("Duplicated!", "Duplicated Input!")
            return
        bookmarklist.append(tmp)
        bookmarklist.append(routelist[tmp])
        BookmarkBox.insert(END, tmp)

    except:
        messagebox.showerror("Invalid Input", "Invalid Input!")
        print('invalid')
    pass

def SearchButtonAction():
    global SearchListBox, userInput, RouteBaseInfo, RouteStationData, StList
    radiobtnsel = radiovar.get()
    print("search")
    userInput = InputLabel.get("1.0", END)
    userInput = userInput.replace('\n','')
    if radiobtnsel == 1:
        try:
#            if routelist[userInput] : pass
            RouteBaseInfo = getRouteInfo(routelist[userInput])
            RouteStationData = getStationInfoByRoute(routelist[userInput])
            InitData(routelist[userInput])
            Tab.select(frame2)
            RenderInfo()
        except:
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
                    datacounter += 1
            RouteSearchBox.configure(state="disabled")

            if not dataexist:
                messagebox.showerror('Error','Invalid Route Name')

    elif radiobtnsel == 2:
        Tab.select(frame1)
        datacounter = 0
        StList = getStationID(userInput)

        if not StList:
            messagebox.showerror("Error!", "No Elements!")
            return

        RouteSearchBox.configure(state='normal')
        RouteSearchBox.delete('1.0', END)
        for data in StList:
            tag = "tag_StSearch" + str(datacounter)
            if datacounter % 2 == 0:
                RouteSearchBox.tag_config(tag, foreground="blue")
            else:
                RouteSearchBox.tag_config(tag, foreground="green")
            RouteSearchBox.tag_bind(tag, '<Button-1>', lambda e: callback(e, tag, 'StSearch'))
            RouteSearchBox.insert(END, data['StName'], tag)
            RouteSearchBox.insert(END, '\n')
            datacounter += 1
        RouteSearchBox.configure(state="disabled")

    else:
        print("N")

def callback(event, tag, cat):
    global RouteBaseInfo, RouteStationData, InputLabel

    index = event.widget.index("@%s,%s" % (event.x, event.y))
    idx = int(index[0:index.find('.')]) - 1

    if cat == 'route':
        tag = 'tag_route' + str(idx)
        userInput = event.widget.get('%s.first' % tag, '%s.last' % tag)
        InputLabel.delete('1.0', END)
        InputLabel.insert(INSERT, userInput)
        Tab.select(frame2)
        RouteBaseInfo = getRouteInfo(routelist[userInput])
        RouteStationData = getStationInfoByRoute(routelist[userInput])
        InitData(routelist[userInput])
        RenderInfo()

    elif cat == 'stationA' or cat == 'stationB':
        if cat == 'stationB':
            idx = idx + len(Route1)
            tag = 'tag_station' + str(idx)
        else:
            tag = 'tag_station' + str(idx)

        arrivaldata = getStationInfo(RouteStationData[idx].get('StationID'))

        tmp = str()
        for dataset in arrivaldata:
            tmp += routelist_inv[dataset['RouteID']] + '\n'
            tmp += dataset['arrivetime1'] + '\n'
            tmp += dataset['arrivetime2'] + '\n' + '\n'

        messagebox.showinfo('{0}'.format(RouteStationData[idx].get('StationName')), tmp)

    elif cat == 'bmk':
        userInput = bookmarklist[idx]
        InputLabel.delete('1.0', END)
        InputLabel.insert(INSERT, userInput)
        Tab.select(frame2)
        RouteBaseInfo = getRouteInfo(routelist[userInput])
        RouteStationData = getStationInfoByRoute(routelist[userInput])
        InitData(routelist[userInput])
        RenderInfo()
        pass

    elif cat == 'StSearch':
        arrivaldata = getStationInfo(StList[idx]['StID'])
        tmp = str()
        for dataset in arrivaldata:
            tmp += routelist_inv[dataset['RouteID']] + '\n'
            tmp += dataset['arrivetime1'] + '\n'
            tmp += dataset['arrivetime2'] + '\n' + '\n'

        messagebox.showinfo('test', tmp)

        print('stsearch')



def key(event):
    if event.char == 'q':
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

def main():
    MainInit()

    g_Tk.mainloop()

main()