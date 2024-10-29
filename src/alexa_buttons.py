#!/usr/bin/env python3

import argparse
from time import sleep
import RPi.GPIO as GPIO
import requests
from config import button_config

def setup_pins(pin_out, pin_in):
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(pin_out, GPIO.OUT)
    GPIO.setup(pin_in, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.output(pin_out, True)


def trigger_routine(url):
    response = requests.get(url)

    print(response.json())


def main():
    
    for button in button_config:
        setup_pins(button["pin_out"], button["pin_in"])

    while True:
        for button in button_config:
            if GPIO.input(button["pin_in"]):
                print("Button pressed")
                trigger_routine(button["trigger_url"])
                sleep(0.5)

if __name__ == "__main__":
    main()
