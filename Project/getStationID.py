import urllib.request
import urllib.parse
from xml.dom import pulldom

def getStationID(searchinput):
    searchinput = urllib.parse.quote(searchinput)
    key = '?serviceKey=TPp1KG1HsvfuMpXci0dkTYUCv7kljFQbDg%2FSySWRADJwGhzJ3dMBk%2FHDzyACWywjlGuiX3ycKh1NZ4ISvWExTg%3D%3D'
    serverurl = 'http://ws.bus.go.kr/api/rest/'
    service = 'stationinfo'
    methodname = 'getStationByName'
    url = serverurl + service +'/'+ methodname + key +'&stSrch=' + searchinput

    req = urllib.request.Request(url)
    req.get_method = lambda: "GET"
    response_body = urllib.request.urlopen(req).read().decode("utf-8")

    rawdata = pulldom.parseString(response_body)
    datalist = list()
    for event, node in rawdata:
        if event == pulldom.START_ELEMENT and node.tagName == 'itemList':
            data = dict()
            rawdata.expandNode(node)
            if node.childNodes[0].childNodes[0].data != '0':
                data['StID'] = node.childNodes[0].childNodes[0].data
                data['StName'] = node.childNodes[4].childNodes[0].data
                datalist.append(data)


    return datalist

