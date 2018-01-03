# -*- coding: utf-8 -*-
"""Skill controlls GPIO on Raspberry Pi.

This allows users to control Relay Switch The Relay Switch is Attached to GPIO1

Example:
    literal blocks::

        Turn Light on
	Turn Light off
        Turn Switch on
        Turn switch off
	Turn fan on
	Turn fan off
	Turn bedroom on
	Turn bedroom off
	Turn living on
	Turn living off
	Turn bathroom on
	Turn bathroom off
	Turn kitchen on
	Turn kitchen off
	Turn lamp on
	Turn lamp off



"""

from os.path import dirname, abspath
import sys
import requests
import json
import threading
import time

sys.path.append(abspath(dirname(__file__)))

from adapt.intent import IntentBuilder
try:
    from mycroft.skills.core import MycroftSkill
except:
    class MycroftSkill:
        pass

import GPIO

""" Includes the GPIO interface"""

__author__ = 'smolino'


class GPIO_ControlSkill(MycroftSkill):
    """This is the skill for controlling GPIO of the Raspberry Pi"""

    def on_led_change(self):
        """used to report the state of the led.

        This is attached to the on change event.  And will speak the
        status of the led.
        """
        """status = GPIO.get("GPIO1")
	self.speak("Light is %s" % status)"""

    def __init__(self):
        """This is used to initize the GPIO kill

        This will set the default of blink_active and setup the function
        for listening to the io change.
        """
        self.blink_active = False
        GPIO.on("GPIO1",self.on_led_change)
        GPIO.on("GPIO2",self.on_led_change)
        GPIO.on("GPIO3",self.on_led_change)
        GPIO.on("GPIO4",self.on_led_change)
        GPIO.on("GPIO5",self.on_led_change)
        GPIO.on("GPIO6",self.on_led_change)
        GPIO.on("GPIO7",self.on_led_change)
        GPIO.on("GPIO8",self.on_led_change)
        super(GPIO_ControlSkill, self).__init__(name="GPIO_ControlSkill")

    def blink_led(self):
        """This Will Start the Led blink process

        This function will start the led blink process and continue
        until blink_active is false.
        """
        if self.blink_active:
            threading.Timer(10, self.blink_led).start()
        if self.blink_active:
            if GPIO.get("GPIO1")!="Off":
                GPIO.set("GPIO1","Off")
            else:
                GPIO.set("GPIO1","On")

    def blink_switch(self):
        """This Will Start the Switch blink process

        This function will start the switch blink process and continue
        until blink_active is false.
        """
        if self.blink_active:
            threading.Timer(10, self.blink_switch).start()
        if self.blink_active:
            if GPIO.get("GPIO2")!="On":
                GPIO.set("GPIO2","On")
            else:
                GPIO.set("GPIO2","Off")

    def blink_fan(self):
        """This Will Start the Switch blink process

        This function will start the switch blink process and continue
        until blink_active is false.
        """
        if self.blink_active:
            threading.Timer(10, self.blink_fan).start()
        if self.blink_active:
            if GPIO.get("GPIO3")!="On":
                GPIO.set("GPIO3","On")
            else:
                GPIO.set("GPIO3","Off")

    def blink_bedroom(self):
        """This Will Start the Switch blink process

        This function will start the switch blink process and continue
        until blink_active is false.
        """
        if self.blink_active:
            threading.Timer(10, self.blink_bedroom).start()
        if self.blink_active:
            if GPIO.get("GPIO4")!="On":
                GPIO.set("GPIO4","On")
            else:
                GPIO.set("GPIO4","Off")

    def blink_livingroom(self):
        """This Will Start the Switch blink process

        This function will start the switch blink process and continue
        until blink_active is false.
        """
        if self.blink_active:
            threading.Timer(10, self.blink_livingroom).start()
        if self.blink_active:
            if GPIO.get("GPIO5")!="On":
                GPIO.set("GPIO5","On")
            else:
                GPIO.set("GPIO5","Off")

    def blink_bathroom(self):
        """This Will Start the Switch blink process

        This function will start the switch blink process and continue
        until blink_active is false.
        """
        if self.blink_active:
            threading.Timer(10, self.blink_bathroom).start()
        if self.blink_active:
            if GPIO.get("GPIO6")!="On":
                GPIO.set("GPIO6","On")
            else:
                GPIO.set("GPIO6","Off")

    def blink_kitchen(self):
        """This Will Start the Switch blink process

        This function will start the switch blink process and continue
        until blink_active is false.
        """
        if self.blink_active:
            threading.Timer(10, self.blink_kitchen).start()
        if self.blink_active:
            if GPIO.get("GPIO7")!="On":
                GPIO.set("GPIO7","On")
            else:
                GPIO.set("GPIO7","Off")

    def blink_lamp(self):
        """This Will Start the Switch blink process

        This function will start the switch blink process and continue
        until blink_active is false.
        """
        if self.blink_active:
            threading.Timer(10, self.blink_lamp).start()
        if self.blink_active:
            if GPIO.get("GPIO8")!="On":
                GPIO.set("GPIO8","On")
            else:
                GPIO.set("GPIO8","Off")


    def initialize(self):
        """This function will initialize the Skill for Blinking an LED

        This creates two intents
            * IoCommandIntent - Will fire for any command that controlls the LED
            * SystemQueryIntent - Will fire for any system command

        The SystemQueryIntent was desinged for debug info while testing
        and is not required going forward.

        """
        self.load_data_files(dirname(__file__))

        command_intent = IntentBuilder("IoCommandIntent").require("command").require("ioobject").optionally("ioparam").build()
        system_intent = IntentBuilder("SystemQueryIntent").require("question").require("systemobject").build()

        self.register_intent(command_intent, self.handle_command_intent)
        self.register_intent(system_intent, self.handle_system_intent)

    def handle_system_intent(self, message):
        """This is the handeler for system intent.

        This will handle all questions of the system for debug info.

        Args:
            message(obj):
                This is the object containing the message that fired the
                intent.  This is used to discover what to do within the
                intent.
        """
        if message.data["systemobject"] == "Name":
            self.speak_dialog("name")
            self.speak(__name__)
        elif message.data["systemobject"] == "GPIO":
            self.speak_dialog("check")
            if GPIO.is_imported:
                self.speak("GPIO is Imported")
            else:
                self.speak("GPIO is not Imported")
        elif message.data["systemobject"] == "Modules":
            self.speak_dialog("modules")
            for module in sys.modules:
                self.speak(module)
        elif message.data["systemobject"] == "Path":
            self.speak_dialog("path")
            for path in sys.path:
                self.speak(path)

    def handle_command_intent(self, message):
        """This will handle all command intents for controlling GPIO

        This handles all commands to controll the LEDS including checking
        the status.

        Args:
            message(obj):
                This is the object containing the message that fired the
                intent.  This is used to discover what to do within the
                intent.
        """
        if message.data["command"].upper() == "BLINK":
            self.speak_dialog("ledblink")
            if self.blink_active:
                self.blink_active = False
            else:
                self.blink_active = True
                self.blink_led()
        elif message.data["command"].upper() == "STATUS":
            if message.data["ioobject"].upper() == "LIGHT":
                self.on_led_change()
        elif message.data["command"].upper() == "TURN":
            if message.data["ioobject"].upper() == "LIGHT":
                if "ioparam" in message.data:
                    if message.data["ioparam"].upper() == "OFF":
                        self.blink_active = False
                        GPIO.set("GPIO1","Off")
                    elif message.data["ioparam"].upper() == "ON":
                        self.blink_active = False
                        GPIO.set("GPIO1","On")
        if message.data["command"].upper() == "BLINK":
            self.speak_dialog("switchblink")
            if self.blink_active:
                self.blink_active = False
            else:
                self.blink_active = True
                self.blink_switch()
        elif message.data["command"].upper() == "TURN":
            if message.data["ioobject"].upper() == "SWITCH":
                if "ioparam" in message.data:
                    if message.data["ioparam"].upper() == "OFF":
                        self.blink_active = False
                        GPIO.set("GPIO2","Off")
                    elif message.data["ioparam"].upper() == "ON":
                        self.blink_active = False
                        GPIO.set("GPIO2","On")
        if message.data["command"].upper() == "BLINK":
            self.speak_dialog("fanblink")
            if self.blink_active:
                self.blink_active = False
            else:
                self.blink_active = True
                self.blink_fan()
        elif message.data["command"].upper() == "TURN":
            if message.data["ioobject"].upper() == "FAN":
                if "ioparam" in message.data:
                    if message.data["ioparam"].upper() == "OFF":
                        self.blink_active = False
                        GPIO.set("GPIO3","Off")
                    elif message.data["ioparam"].upper() == "ON":
                        self.blink_active = False
                        GPIO.set("GPIO3","On")
        if message.data["command"].upper() == "BLINK":
            self.speak_dialog("bedroomblink")
            if self.blink_active:
                self.blink_active = False
            else:
                self.blink_active = True
                self.blink_bedroom()
        elif message.data["command"].upper() == "TURN":
            if message.data["ioobject"].upper() == "BEDROOM":
                if "ioparam" in message.data:
                    if message.data["ioparam"].upper() == "OFF":
                        self.blink_active = False
                        GPIO.set("GPIO4","Off")
                    elif message.data["ioparam"].upper() == "ON":
                        self.blink_active = False
                        GPIO.set("GPIO4","On")
        if message.data["command"].upper() == "BLINK":
            self.speak_dialog("livingroomblink")
            if self.blink_active:
                self.blink_active = False
            else:
                self.blink_active = True
                self.blink_livingroom()
        elif message.data["command"].upper() == "TURN":
            if message.data["ioobject"].upper() == "LIVING":
                if "ioparam" in message.data:
                    if message.data["ioparam"].upper() == "OFF":
                        self.blink_active = False
                        GPIO.set("GPIO5","Off")
                    elif message.data["ioparam"].upper() == "ON":
                        self.blink_active = False
                        GPIO.set("GPIO5","On")
        if message.data["command"].upper() == "BLINK":
            self.speak_dialog("bathroomblink")
            if self.blink_active:
                self.blink_active = False
            else:
                self.blink_active = True
                self.blink_bathroom()
        elif message.data["command"].upper() == "TURN":
            if message.data["ioobject"].upper() == "BATHROOM":
                if "ioparam" in message.data:
                    if message.data["ioparam"].upper() == "OFF":
                        self.blink_active = False
                        GPIO.set("GPIO6","Off")
                    elif message.data["ioparam"].upper() == "ON":
                        self.blink_active = False
                        GPIO.set("GPIO6","On")
        if message.data["command"].upper() == "BLINK":
            self.speak_dialog("kitchenblink")
            if self.blink_active:
                self.blink_active = False
            else:
                self.blink_active = True
                self.blink_kitchen()
        elif message.data["command"].upper() == "TURN":
            if message.data["ioobject"].upper() == "KITCHEN":
                if "ioparam" in message.data:
                    if message.data["ioparam"].upper() == "OFF":
                        self.blink_active = False
                        GPIO.set("GPIO7","Off")
                    elif message.data["ioparam"].upper() == "ON":
                        self.blink_active = False
                        GPIO.set("GPIO7","On")
        if message.data["command"].upper() == "BLINK":
            self.speak_dialog("lampblink")
            if self.blink_active:
                self.blink_active = False
            else:
                self.blink_active = True
                self.blink_lamp()
        elif message.data["command"].upper() == "TURN":
            if message.data["ioobject"].upper() == "LAMP":
                if "ioparam" in message.data:
                    if message.data["ioparam"].upper() == "OFF":
                        self.blink_active = False
                        GPIO.set("GPIO8","Off")
                    elif message.data["ioparam"].upper() == "ON":
                        self.blink_active = False
                        GPIO.set("GPIO8","On")
                else:
                    self.speak_dialog("ipparamrequired")

    def stop(self):
        """This function will clean up the Skill"""
        self.blink_active = False


def create_skill():
    """This function is to create the skill"""
    return GPIO_ControlSkill()

