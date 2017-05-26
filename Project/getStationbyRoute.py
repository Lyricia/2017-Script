import urllib.request
import urllib.parse
from xml.dom import pulldom

def getStationInfoByRoute(routeID):
    key = '?serviceKey=TPp1KG1HsvfuMpXci0dkTYUCv7kljFQbDg%2FSySWRADJwGhzJ3dMBk%2FHDzyACWywjlGuiX3ycKh1NZ4ISvWExTg%3D%3D'
    serverurl = 'http://ws.bus.go.kr/api/rest/'
    service = 'busRouteInfo'
    methodname = 'getStaionByRoute'
    url = serverurl + service +'/'+ methodname + key +'&busRouteId=' + routeID

    req = urllib.request.Request(url)
    req.get_method = lambda: "GET"
    response_body = urllib.request.urlopen(req).read().decode("utf-8")

    rawdata = pulldom.parseString(response_body)
    datalist = list()
    for event, node in rawdata:
        if event == pulldom.START_ELEMENT and node.tagName == 'itemList':
            data = dict()
            rawdata.expandNode(node)
            data['StationName'] = node.childNodes[15].childNodes[0].data
            data['begintime'] = node.childNodes[1].childNodes[0].data
            data['lasttime'] = node.childNodes[7].childNodes[0].data
            data['direction'] = node.childNodes[4].childNodes[0].data
            data['StationID'] = node.childNodes[16].childNodes[0].data
            data['IsBusArrived'] = False
            datalist.append(data)


    return datalist