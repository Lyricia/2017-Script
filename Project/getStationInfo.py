import urllib.request
import urllib.parse
from xml.dom import pulldom

def getStationInfo(stationID):
    key = '?serviceKey=TPp1KG1HsvfuMpXci0dkTYUCv7kljFQbDg%2FSySWRADJwGhzJ3dMBk%2FHDzyACWywjlGuiX3ycKh1NZ4ISvWExTg%3D%3D'
    serverurl = 'http://ws.bus.go.kr/api/rest/'
    service = 'stationinfo'
    methodname = 'getStationByUid'
    url = serverurl + service +'/'+ methodname + key +'&arsId=' + stationID

    req = urllib.request.Request(url)
    req.get_method = lambda: "GET"
    response_body = urllib.request.urlopen(req).read().decode("utf-8")

    data = dict()
    rawdata = pulldom.parseString(response_body)
    for event, node in rawdata:
        if event == pulldom.START_ELEMENT and node.tagName == 'itemList':
            rawdata.expandNode(node)
            data['arrivetime1'] = node.childNodes[3].childNodes[0].data
            data['arrivetime2'] = node.childNodes[4].childNodes[0].data


    return data
