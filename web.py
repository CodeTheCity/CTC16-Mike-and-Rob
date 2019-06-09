from flask import Flask, render_template, jsonify, request, json, redirect
import colorsys
from random import random

app = Flask(__name__)

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
