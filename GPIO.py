import json
import threading
import time

blink_active = False

GPIO = {}
GPIO_ON = {}


INPUT = 0
OUTPUT = 1

OUTPUT_HIGH = 1
OUTPUT_LOW  = 2


def set(key,value):
    GPIO[key] = value
    if key in GPIO_ON:
        GPIO_ON[key]()

def get(key):
    return GPIO[key]

def on(key,function):
    GPIO_ON[key]= function

def json():
    return json.dumps(GPIO)


if __name__=="__main__":
    def printgpio():
        print GPIO

    def blink_led():
        if blink_active:
            threading.Timer(0.5, blink_led).start()
        if get("GPIO1")!="On":
            set("GPIO1","On")
        else:
            set("GPIO1","Off")

    on("GPIO1",printgpio)

    set("GPIO1","On")
    blink_active = True
    blink_led()
    time.sleep(10)
    blink_active = False

