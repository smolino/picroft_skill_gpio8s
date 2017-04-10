# -*- coding: utf-8 -*-
"""Skill F-Type controlls.

This allows for control of the Jaguar F-Type demo car only.  You will
require the api key and install as a skill to mycroft.

Notes
-----
    Notes that the responce by the car is somewhat flaky and therefor
    it is important to listen to the responses from mycroft.

"""

from os.path import dirname
import requests
import json
import threading

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import logging.handlers

import GPIO

__author__ = 'amcgee7'

LOGGER = logging.getLogger(__name__)
handler = logging.FileHandler(__name__+'.log');
handler.setLevel(logging.DEBUG)
LOGGER.addHandler(handler)

LOGGER.info("File %s Started",__name__)


class GPIO_ControlSkill(MycroftSkill):

    def __init__(self):
        self.blink_active = False
        super(GPIO_ControlSkill, self).__init__(name="GPIO_ControlSkill")

    def initialize(self):
        LOGGER.info("initialize FTypeControlSkill dir=%s",dirname(__file__))
        self.load_data_files(dirname(__file__))

        command_intent = IntentBuilder("IoCommandIntent").require("command").require("ioobject").optional("ioparam").build()
        self.register_intent(command_intent, self.handle_command_intent)

    def blink_led(self):
        if self.blink_active:
            threading.Timer(0.5, blink_led).start()
        if GPIO.get("GPIO1")!="On":
            GPIO.set("GPIO1","On")
        else:
            GPIO.set("GPIO1","Off")


    def handle_command_intent(self, message):
        global vehicle_command_flag
        if message.data["command"] == "Blink":
            self.speak_dialog("ledblink")
            if self.blink_active:
                self.blink_active = False
            else:
                self.blink_active = True
                self.blink_led()
        elif message.data["command"] == "Turn":
            if message.data["ioobject"] == "LED":
                if "ioparam" in message.data:
                    if mesage.data["ioobject"] == "On":
                        GPIO.set("GPIO1","On")
                    elif message.data["ioobject"] == "Off":
                        GPIO.set("GPIO1","Off")
                else:
                    self.speak_dialog("ipparamrequired")

    def stop(self):
        self.blink_active = False
        pass


def create_skill():
    return GPIO_ControlSkill()
