from machine import Pin, PWM

import urequests
import ujson
import time

sensor_url = "http://air.bodaegl.com/test"

red = PWM(Pin(14), freq=500, duty=0)
green = PWM(Pin(12), freq=500, duty=0)
blue = PWM(Pin(4), freq=500, duty=0)
white = PWM(Pin(5), freq=500, duty=0)

def get_current(url):
    resp = urequests.get(url)
    vals = ujson.loads(resp.text)
    return vals

def update():
    cur = get_current(sensor_url)
    print(cur)
    red.duty(int(cur["r"]))
    green.duty(int(cur["g"]))
    blue.duty(int(cur["b"]))
    white.duty(int(cur["w"]))
             

def run():
    while True:
        try:
            update()
        except Exception as e:
            print(e)
        time.sleep(10)

run()
