from flask import Flask, render_template, jsonify, request, json, redirect
import colorsys
from random import random
import urllib.request as req
import statistics as stat

app = Flask(__name__)

colours = {'red': (255, 0, 0),
           'green': (0, 255, 0),
           'blue': (0, 0, 255),
           'orange': (255, 165, 0),
           'yellow': (255, 255, 0),
           'yel_grn': (255, 255, 0),
           'off': (0,0,0) }


def randc():
    r,g,b = colorsys.hsv_to_rgb(random(), 1, 1.0)
    return [int(r*1024), int(g*1024), int(b*1024)]

@app.route("/")
def root():
    return jsonify({"msg":"OK"})

@app.route("/test")
def test():
    c = randc()
    return jsonify({"r":c[0], "g":c[1], "b":c[2], "w":0}) 

@app.route("/abdn_mean")
def abdn_mean():
    url="http://api.luftdaten.info/v1/filter/area=57,-2,20"
    # TODO: get a real location for this

    resp = req.urlopen(url)
    data = json.loads(resp.read().decode("utf-8"))

    pm2 = []
    pm10 = []

    for reading in data:
        for val in reading['sensordatavalues']:
            if val['value_type'] == "P1":
                pm10.append(float(val['value']))
            if val['value_type'] == "P2":
                pm2.append(float(val['value']))

    pm2_mean = stat.mean(pm2)
    pm10_mean = stat.mean(pm10)
    c = colours['green']
    if pm2_mean > 20 or pm10_mean > 45:
        c = colours['red']

    return jsonify({"r":c[0], "g":c[1], "b":c[2], "w":0})
