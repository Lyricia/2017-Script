import urllib.request
import urllib.parse
from xml.dom import pulldom
import pickle

def loadRouteListfromAPI():
    key = '?serviceKey=TPp1KG1HsvfuMpXci0dkTYUCv7kljFQbDg%2FSySWRADJwGhzJ3dMBk%2FHDzyACWywjlGuiX3ycKh1NZ4ISvWExTg%3D%3D'
    serverurl = 'http://ws.bus.go.kr/api/rest/'
    service = 'busRouteInfo'
    method = 'getBusRouteList'

    routelist = dict()

    url = serverurl + service +'/'+ method + key

    req = urllib.request.Request(url)
    req.get_method = lambda: "GET"
    response_body = urllib.request.urlopen(req).read().decode("utf-8")

    # xmlfunc("rawdata.xml")

    # tree = ElementTree.fromstring("rawdata.xml")
    rawdata = pulldom.parseString(response_body)

    for event, node in rawdata:
        if event == pulldom.START_ELEMENT and node.tagName == 'itemList':
            # Following statement only prints '<p/>'
            rawdata.expandNode(node)
            # Following statement prints node with all its children '<p>Some text <div>and more</div></p>'
            routeID = node.childNodes[0].childNodes[0].data
            routename = node.childNodes[1].childNodes[0].data
            routelist[routename] = routeID

    print("Load Complete")

    f = open("data.txt", 'wb')
    pickle.dump(routelist, f)
    f.close()

    print("Data Dump to txt Complete")

    return routelist


def loadRouteListfromFile():
    f = open("data.txt", 'rb')
    routelist = pickle.load(f)
    f.close()
    return routelist