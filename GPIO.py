"""This is test code for interacting with GPIO

This is intented to mock up an interface into the RPi GPIO until hardware
is accquired
"""

import json
import threading
import time

try:
    import RPi.GPIO as GPIO
    """This is trapped so you can still run without RPi.GPIO

    GPIO will be checked before use
    """
    pi_interface = True
except:
    pi_interface = False
    pass


blink_active = False
"""bool: to controll weather blink continues to be active

This will not start the blinking it will only be important once blinking
has started.  This is currently only used in testing.
"""
GPIOS = { "GPIO1":27,
          "GPIO2":17,
          "GPIO3":22,
          "GPIO4":05,
          "GPIO5":06,
          "GPIO6":13,
          "GPIO7":19,
          "GPIO8":26 }

GPIO_STATE = { "GPIO1":"Off",
               "GPIO2":"Off",
               "GPIO3":"Off",
               "GPIO4":"Off",
               "GPIO5":"Off",
               "GPIO6":"Off",
               "GPIO7":"Off",
               "GPIO8":"Off" }
""" This is an object of tracking GPIO"""

GPIO_ON = {}
""" This maps functions to gpio activit

These functions will be called when the GPIO is changed in any way.
"""


is_imported = True
"""Used as a flag to show that GPIO was imported"""

def ButtonHandeler(channel):
    """This handels the button press and sets the state

    Args:
        channel(int):  The RPi GPIO channel used for monitoring the button
    """
"""    if GPIO.input(channel) == GPIO.HIGH:
        set("Button","Pressed")
    else:
        set("Button","Released")"""

"""This is the setup for the RPi GPIO"""
if pi_interface:
    GPIO.setmode(GPIO.BCM)
    for gpio in GPIOS:
        GPIO.setup(GPIOS[gpio],GPIO.OUT)
""" GPIO.add_event_detect(17,GPIO.BOTH,ButtonHandeler)"""

def set(key,value):
    """This is used to set values for GPIO

    This function is used to set values for each of GPIO's Will also call
    the GPIO's function if it exisits.

    Args:
        key(int or str): Used to identify the gpio to interface
        value(int or str): The value to set the gpio to.
    """
    GPIO_STATE[key] = value
    if pi_interface:
        for gpio in GPIOS:
            if (key == gpio):
                if value.upper() == "ON":
                    GPIO.output(GPIOS[gpio], GPIO.LOW)
                else:
                    GPIO.output(GPIOS[gpio],GPIO.HIGH)
    if key in GPIO_ON:
        GPIO_ON[key](key)


def get(key):
    """ Returns the value of the givien GPIO

    Args:
        key(int or str): Used to identify the gpio to interface
    """
    return GPIO_STATE[key]

def on(key,function):
    """Used to set the function for the GPIO interface

    Args:
        key(int or str): Used to identify the gpio to interface
        function(function): The function for the gpio
    """
    GPIO_ON[key]= function

def json():
    """Returns a json object of the GPIO info"""
    return json.dumps(GPIO_STATE)


if __name__=="__main__":
    """This is console testing of the GPIO.  Not ment for automated testing

    This should show that everything is working to the developer and allow
    for changes going forward
    """
    def printgpio(key):
        print(GPIO_STATE)

    def blink_led():
        if blink_active:
            threading.Timer(0.5, blink_led).start()
        if get("GPIO1")!="Off":
            set("GPIO1","Off")
        else:
            set("GPIO1","On")

    on("GPIO1",printgpio)

    set("GPIO1","On")
    blink_active = True
    blink_led()
    time.sleep(10)
    blink_active = False
    if pi_interface:
        print("GPIO is valid")

    def blink_switch():
        if blink_active:
            threading.Timer(0.5, blink_switch).start()
        if get("GPIO2")!="Off":
            set("GPIO2","Off")
        else:
            set("GPIO2","On")

    on("GPIO2",printgpio)

    set("GPIO2","On")
    blink_active = True
    blink_switch()
    time.sleep(10)
    blink_active = False
    if pi_interface:
        print("GPIO is valid")


    def blink_fan():
        if blink_active:
            threading.Timer(0.5, blink_fan).start()
        if get("GPIO3")!="Off":
            set("GPIO3","Off")
        else:
            set("GPIO3","On")

    on("GPIO3",printgpio)

    set("GPIO3","On")
    blink_active = True
    blink_fan()
    time.sleep(10)
    blink_active = False
    if pi_interface:
        print("GPIO is valid")

    def blink_bedroom():
        if blink_active:
            threading.Timer(0.5, blink_bedroom).start()
        if get("GPIO4")!="Off":
            set("GPIO4","Off")
        else:
            set("GPIO4","On")

    on("GPIO4",printgpio)

    set("GPIO4","On")
    blink_active = True
    blink_bedroom()
    time.sleep(10)
    blink_active = False
    if pi_interface:
        print("GPIO is valid")

    def blink_livingroom():
        if blink_active:
            threading.Timer(0.5, blink_livingroom).start()
        if get("GPIO5")!="Off":
            set("GPIO5","Off")
        else:
            set("GPIO5","On")

    on("GPIO5",printgpio)

    set("GPIO5","On")
    blink_active = True
    blink_livingroom()
    time.sleep(10)
    blink_active = False
    if pi_interface:
        print("GPIO is valid")

    def blink_bathroom():
        if blink_active:
            threading.Timer(0.5, blink_bathroom).start()
        if get("GPIO6")!="Off":
            set("GPIO6","Off")
        else:
            set("GPIO6","On")

    on("GPIO6",printgpio)

    set("GPIO6","On")
    blink_active = True
    blink_bathroom()
    time.sleep(10)
    blink_active = False
    if pi_interface:
        print("GPIO is valid")

    def blink_kitchen():
        if blink_active:
            threading.Timer(0.5, blink_kitchen).start()
        if get("GPIO7")!="Off":
            set("GPIO7","Off")
        else:
            set("GPIO7","On")

    on("GPIO7",printgpio)

    set("GPIO7","On")
    blink_active = True
    blink_kitchen()
    time.sleep(10)
    blink_active = False
    if pi_interface:
        print("GPIO is valid")

    def blink_lamp():
        if blink_active:
            threading.Timer(0.5, blink_lamp).start()
        if get("GPIO8")!="Off":
            set("GPIO8","Off")
        else:
            set("GPIO8","On")

    on("GPIO8",printgpio)

    set("GPIO8","On")
    blink_active = True
    blink_lamp()
    time.sleep(10)
    blink_active = False
    if pi_interface:
        print("GPIO is valid")
