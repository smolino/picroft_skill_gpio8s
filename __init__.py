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

    switches = {
        "LIGHT": {"gpio":"GPIO1", "dialog":"ledblink", "name":"light"},
        "SWITCH": {"gpio":"GPIO2", "dialog":"switchblink", "name":"switch"},
        "FAN": {"gpio":"GPIO3", "dialog":"fanblink", "name":"fan"},
        "BEDROOM": {"gpio":"GPIO4", "dialog":"bedroomblink", "name":"bedroom"},
        "LIVING": {"gpio":"GPIO5", "dialog":"livingroomblink", "name":"livingroom"},
        "BATHROOM": {"gpio":"GPIO6", "dialog":"bathroomblink", "name":"bathroom"},
        "KITCHEN": {"gpio":"GPIO7", "dialog":"kitchenblink", "name":"kitchen"},
        "LAMP": {"gpio":"GPIO8", "dialog":"lampblink", "name":"lamp"},
    }
    def getSwitchKey(self, values, gpio):
        for key, val in values.iteritems():
            if val['gpio'] == gpio:
                return key

    def on_change(self, gpio):
        """used to report the state of the led.

        This is attached to the on change event.  And will speak the
        status of the led.
        """
        key = self.getSwitchKey(self.switches, gpio)
        status = GPIO.get(gpio)
        name = self.switches[key]['name']
        self.speak("%s is %s" % (name, status))

    def __init__(self):
        """This is used to initize the GPIO kill

        This will set the default of blink_active and setup the function
        for listening to the io change.
        """
        self.blink_active = False
        for key in self.switches:
            GPIO.on(self.switches[key]['gpio'], self.on_change)
        super(GPIO_ControlSkill, self).__init__(name="GPIO_ControlSkill")

    def blink(self):
        """This Will Start the Led blink process

        This function will start the led blink process and continue
        until blink_active is false.
        """
        if self.blink_active:
            gpio = self.switches['LIGHT']["gpio"]
            GPIO.set(gpio, "Off" if GPIO.get(gpio)!="Off" else "On")
            threading.Timer(10, self.blink).start()

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
            key = message.data["ioobject"].upper()
            if key == 'LIGHT':
                self.speak_dialog(self.switches[key]['dialog'])
                self.blink_active = not self.blink_active
                if self.blink_active:
                    self.blink()
        elif message.data["command"].upper() == "STATUS":
            if message.data["ioobject"].upper() in self.switches:
                switch = self.switches[message.data["ioobject"].upper()]
                self.on_change(switch['gpio'])
        elif message.data["command"].upper() == "TURN":
            if "ioparam" in message.data:
                switch = self.switches[message.data["ioobject"].upper()]
                self.blink_active = False
                GPIO.set(switch['gpio'], "Off" if message.data["ioparam"].upper() == "OFF" else "ON")
            else:
                self.speak_dialog("ipparamrequired")

    def stop(self):
        """This function will clean up the Skill"""
        self.blink_active = False


def create_skill():
    """This function is to create the skill"""
    return GPIO_ControlSkill()
