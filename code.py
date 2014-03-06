#!/usr/bin/env python
#coding:utf-8
import web



urls = (
    "/","ctrl.index",
    "/bus","ctrl.bus_ctrl"
)

app = web.application(urls,globals())
if __name__ == "__main__":
    app.run()


