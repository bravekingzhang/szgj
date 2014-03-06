#!/usr/bin/env python
#coding:utf-8
import web,models,json
class index:
    def GET(self):
        return open("index.html","r").read()

class bus_ctrl:
    def GET(self):
        d = web.input()
        lineName = d.line
        lat = d.lat
        lng = d.lng
        d_list = list() 
        lines = models.getLines(lineName,lat,lng)
        for line in lines:
            b_list = list()
            buses = models.getBuses(line["lineId"],line["stations"])
            for bus in buses:
                b_list.append({
                    "lat":bus["lat"],
                    "lng":bus["lng"],
                    "name":bus["name"],
                    "waittime":bus["waittime"]
                })
            d_list.append({
                "lineId": line["lineId"],
                "lineName":line["lineWay"],
                "buses":b_list
            })

        return json.dumps({"lines":d_list})
    

    """
        {
            "lines":[
                {    
                    "lineName":"where to where",
                    "buses":[
                        "lat":
                        "lng":
                        "name":
                    ]
                }
            ]
        }
    """


