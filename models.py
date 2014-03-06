#!/usr/bin/env python
#coding:utf-8

import web,json,urllib2


def getLines(name,lat,lng):
    lines = get(name)
    if lines:
        return lines
    else:
        lines = getLinesFromApi(name,lat,lng)
        save(lines)
        return lines

def getLinesFromApi(lineName,lat,lng):
    lineName = lineName.upper()
    data = getUrl("http://busapi.gpsoo.net/v1/bus/get_lines_by_city?line_name="+lineName+"&city_id=860515&type=handset&mapType=BAIDU_MAP")
    data = json.loads(data)
    l_list = list()
    for line in data["data"]:
        s_data = json.loads(getUrl("http://busapi.gpsoo.net/v1/bus/mbcommonservice?method=getlineinfo&lng="+lng+"&lat="+lat+"&sublineID="+line["id"]+"&mapType=BAIDU_MAP"))
        stations = get3Stations(s_data)
        l_list.append({
            "lineId": line["id"],
            "lineWay": line["start_station"]+"->"+line["end_station"],
            "stations":stations
        })
    return l_list

def get3Stations(s_data):
    currentStation = s_data["data"]["station"]["id"]
    stations = s_data["data"]["subline"]["station"]
    s_list = [currentStation]
    s_index = 0
    for s in stations:
        if s["id"] == currentStation:
            break
        s_index +=1
    if s_index+5 < len(stations)-1:
        s_list.append(stations[s_index+5]["id"])
    if s_index+10 < len(stations)-1:
        s_list.append(stations[s_index+10]["id"])
    return s_list


def getBuses(lineId,stations):
    buses = list()
    busids = list()
    for station in stations:
        b_data =json.loads(getUrl("http://busapi.gpsoo.net/v1/bus/mbcommonservice?method=getnearcarinfo&sublineID="+lineId+"&mapType=BAIDU_MAP&stationId="+station+"&ids="))
        for s in b_data["data"]:
            if not s["carid"] in busids:
                buses.append(s)
                busids.append(s["carid"])
    return buses


        
def getUrl(url):
    req = urllib2.Request(url)
    print url
    req.add_header("User-Agent","SZYXWNew/3.1 CFNetwork/672.0.8 Darwin/14.0.0")
    resp = urllib2.urlopen(req)
    return resp.read()

def save(obj):
    ## half hour
    pass

def get(name):
    return None



##print getBuses("99315",["1559205","1559217","1555233"])

