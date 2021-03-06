import urllib.request
import urllib.parse
from xml.dom import pulldom

def getRouteInfo(routeID):
    key = '?serviceKey=TPp1KG1HsvfuMpXci0dkTYUCv7kljFQbDg%2FSySWRADJwGhzJ3dMBk%2FHDzyACWywjlGuiX3ycKh1NZ4ISvWExTg%3D%3D'
    serverurl = 'http://ws.bus.go.kr/api/rest/'
    service = 'busRouteInfo'
    methodname = 'getRouteInfo'
    url = serverurl + service +'/'+ methodname + key +'&busRouteId=' + routeID

    req = urllib.request.Request(url)
    req.get_method = lambda: "GET"
    response_body = urllib.request.urlopen(req).read().decode("utf-8")

    rawdata = pulldom.parseString(response_body)
    data = dict()
    for event, node in rawdata:
        if event == pulldom.START_ELEMENT and node.tagName == 'itemList':
            rawdata.expandNode(node)
            data['CorpName'] = node.childNodes[2].childNodes[0].data
            data['EndStation'] = node.childNodes[3].childNodes[0].data
            data['StartStation'] = node.childNodes[11].childNodes[0].data

    return data