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

    for event, node in rawdata:
        if event == pulldom.START_ELEMENT and node.tagName == 'itemList':
            # Following statement only prints '<p/>'
            rawdata.expandNode(node)
            # Following statement prints node with all its children '<p>Some text <div>and more</div></p>'
            print(node.toxml())