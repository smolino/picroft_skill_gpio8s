"""This is test code for interacting with GPIO

This is intented to mock up an interface into the RPi GPIO until hardware
is accquired
"""

import json
import threading
import time

blink_active = False
"""bool: to controll weather blink continues to be active

This will not start the blinking it will only be important once blinking
has started.  This is currently only used in testing.
"""

GPIO = {}
""" This is an object of tracking GPIO"""

GPIO_ON = {}
""" This maps functions to gpio activit

These functions will be called when the GPIO is changed in any way.
"""


is_imported = True
"""Used as a flag to show that GPIO was imported"""

def set(key,value):
    """This is used to set values for GPIO

    This function is used to set values for each of GPIO's Will also call
    the GPIO's function if it exisits.

    Args:
        key(int or str): Used to identify the gpio to interface
        value(int or str): The value to set the gpio to.
    """
    GPIO[key] = value
    if key in GPIO_ON:
        GPIO_ON[key]()

def get(key):
    """ Returns the value of the givien GPIO

    Args:
        key(int or str): Used to identify the gpio to interface
    """
    return GPIO[key]

def on(key,function):
    """Used to set the function for the GPIO interface

    Args:
        key(int or str): Used to identify the gpio to interface
        function(function): The function for the gpio
    """
    GPIO_ON[key]= function

def json():
    """Returns a json object of the GPIO info"""
    return json.dumps(GPIO)


if __name__=="__main__":
    """This is console testing of the GPIO.  Not ment for automated testing

    This should show that everything is working to the developer and allow
    for changes going forward
    """
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

