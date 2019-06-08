from machine import Pin, PWM

import urequests
import ujson
import time

sensor_url = "http://foo.bodaegl.com/air.json"

red = PWM(Pin(2), freq=500, duty=0)
green = PWM(Pin(0), freq=500, duty=0)
blue = PWM(Pin(4), freq=500, duty=0)
white = PWM(Pin(5), freq=500, duty=0)

def pick_col(lvl):
    colours = {'red': (255, 0, 0),
               'green': (0, 255, 0),
               'blue': (0, 0, 255),
               'orange': (255, 165, 0),
               'yellow': (255, 255, 0),
               'yel_grn': (255, 255, 0),
               'off': (0,0,0) }
    if lvl < 20: return colours['green']
    if lvl < 30: return colours['yellow']
    if lvl < 40: return colours['orange']
    return colours['red']

def build_pix(col, lvl, mxm=100):
    return [col for _ in range(NUM_PIXELS)]

def disp(pm2, pm10):
    c = pick_col(pm2)
    print("Pixel val: ", c)
    red.duty(4*c[0])
    green.duty(4*c[1])
    blue.duty(4*c[2])


def get_current(url):
    resp = urequests.get(url)
    vals = ujson.loads(resp.text)
    return vals[-1]

def update():
    pm10 = 0
    pm2 = 0
    cur = get_current(sensor_url)
    for reading in cur['sensordatavalues']:
        if reading['value_type'] == "P2":
            pm2 = float(reading['value'])
            print("PM2.5 value:", pm2)
        if reading['value_type'] == "P1":
            pm10 = float(reading['value'])
            print("PM10 value:", pm10)
    disp(pm2, pm10)


def run():
    while True:
        try:
            update()
        except Exception as e:
            print(e)
        time.sleep(2)

run()
