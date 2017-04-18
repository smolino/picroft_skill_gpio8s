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

GPIO_STATE = {}
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
    if GPIO.input(channel) == GPIO.HIGH:
        set("Button","Pressed")
    else:
        set("Button","Released")

"""This is the setup for the RPi GPIO"""
if pi_interface:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27,GPIO.OUT)
    GPIO.setup(17,GPIO.IN)
    GPIO.add_event_detect(17,GPIO.BOTH,ButtonHandeler)

def set(key,value):
    """This is used to set values for GPIO

    This function is used to set values for each of GPIO's Will also call
    the GPIO's function if it exisits.

    Args:
        key(int or str): Used to identify the gpio to interface
        value(int or str): The value to set the gpio to.
    """
    GPIO_STATE[key] = value
    if (key=="GPIO1") and pi_interface:
        if value.upper()=="ON":
            GPIO.output(27,GPIO.HIGH)
        else:
            GPIO.output(27,GPIO.LOW)
    if key in GPIO_ON:
        GPIO_ON[key]()

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
    def printgpio():
        print(GPIO_STATE)

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
    if pi_interface:
        print("GPIO is valid")

