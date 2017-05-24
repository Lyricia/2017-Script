import urllib.request
import urllib.parse
from xml.dom import pulldom

def getCurrentBusPosByRoute(routeID):
    key = '?serviceKey=TPp1KG1HsvfuMpXci0dkTYUCv7kljFQbDg%2FSySWRADJwGhzJ3dMBk%2FHDzyACWywjlGuiX3ycKh1NZ4ISvWExTg%3D%3D'
    serverurl = 'http://ws.bus.go.kr/api/rest/'
    service = 'buspos'
    methodname = 'getBusPosByRtid'
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
            data['StationIndex'] = node.childNodes[15].childNodes[0].data
            data['vehicleID'] = node.childNodes[18].childNodes[0].data

            datalist.append(data)


    return datalist

