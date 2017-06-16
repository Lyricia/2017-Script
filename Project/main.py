from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
import urllib.request
import urllib.parse
from xml.dom.minidom import parse, parseString # minidom 모듈의 파싱 함수를 임포트합니다.
from xml.etree import ElementTree
from xml.dom import pulldom
from LoadRouteList import *
from getRouteInfo import *
from getStationbyRoute import *
from getCurrentBusPosbyRoute import *
from getStationInfo import *
from getStationbyRoute import *
from getStationID import *
import webbrowser
from EmailSender import *

key = '?serviceKey=TPp1KG1HsvfuMpXci0dkTYUCv7kljFQbDg%2FSySWRADJwGhzJ3dMBk%2FHDzyACWywjlGuiX3ycKh1NZ4ISvWExTg%3D%3D'
serverurl = 'http://ws.bus.go.kr/api/rest/busRouteInfo/'

#routelist['dummydata'] = '000000001'

#loadRouteListfromAPI()

routelist = loadRouteListfromFile()
#routelist = loadRouteListfromAPI()
print(routelist)


testBusRouteID = routelist['광진01']
#104900005
#05533
#05158

RouteBaseInfo = getRouteInfo(testBusRouteID)
RouteStationData = getStationInfoByRoute(testBusRouteID)
#
#print(RouteBaseInfo['EndStation'])
#Route1 = list()
#Route2 = list()
#for data in RouteStationData:
#    if (RouteBaseInfo.get('EndStation') == data.get('direction') and
#                data.get('direction') != data.get('StationName')):
#        Route1.append(data)
#    elif (data.get('direction') == data.get('StationName') or
#          RouteBaseInfo.get('EndStation') != data.get('direction')):
#        Route2.append(data)
#
#routeinfo = getStationInfoByRoute(testBusRouteID)
#
#datalist = getStationInfo('05158')
#
#print('')

#CurrentBusPos = getCurrentBusPosByRoute(testBusRouteID)
#for data in CurrentBusPos:
#    #arrivetime = getStationInfo(RouteStationData[int(data.get('StationIndex'))].get('StationID'))
#    print(data.get('StationIndex'))
#    print(RouteStationData[int(data.get('StationIndex'))].get('StationID'))

list = getStationID('테크')
print(getStationInfo(list[23]['StID']))

#SendEmail(list, 'ST')

routetmp = '104900005'
tmpurl = 'http://bus.go.kr/realBusLine6.jsp?strbusid={0}&wbustp=N'.format(routetmp)

#webbrowser.open(tmpurl)