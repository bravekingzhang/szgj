#!/usr/bin/python
#coding:utf-8

import web

urls = (
    "/","ctrl.index",
    "/bus","ctrl.bus_ctrl"
)


app = web.application(urls,globals())
application = app.wsgifunc()
