#KY040 Python Class
#base file from Martin O'Hanlon
#stuffaboutcode.com

"""Seriously, Martin's site is one of the best resources for RPi, python, coding help
Thank you Martin for providing the base of this file. My project wouldn't have
worked, and I would be lost without this gem."""

#Increase Volume, Decrease Volume, Play, Pause, and Skip Track 
# functionality as well as doc strings by Jakob Vendegna

"""This file is intended to run as a service on a Raspberry Pi using an mcp player like
runeaudio (http://www.runeaudio.com/). The functionality of this file will allow a headless
player, as should be with a RPi."""

import RPi.GPIO as GPIO
from time import sleep
import subprocess

#start playing on boot
subprocess.call(['mpc','play'])


class KY040:
    """in martin's file the clockwise and anti clockwise variables are opposite with CLOCKWISE = 0, etc...
    however this gave my ky040 the opposite functionality that I wanted. I am sure the variables are arbitrary,
    but I thought I would change it for the sake of sanity."""
    CLOCKWISE = 1
    ANTICLOCKWISE = 0
    #button_counter tracks the number of times the switch on the ky040 has been pressed
    button_counter = 0
    
    def __init__(self, clockPin, dataPin, switchPin, rotaryCallback, switchCallback):
        #persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback


        #setup pins
        GPIO.setup(clockPin, GPIO.IN)
        GPIO.setup(dataPin, GPIO.IN)
        GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
       

    def start(self):
        GPIO.add_event_detect(self.clockPin, GPIO.FALLING, callback=self._clockCallback, bouncetime=250)
        GPIO.add_event_detect(self.switchPin, GPIO.FALLING, callback=self._switchCallback, bouncetime=300)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)
        GPIO.remove_event_detect(self.switchPin)
    # when knob turned:
    def _clockCallback(self, pin):
        if GPIO.input(self.clockPin) == 0:
            data = GPIO.input(self.dataPin)
            if data == 1:
                self.rotaryCallback(self.ANTICLOCKWISE)
                subprocess.call(['mpc', 'volume', '-2'])
            else:
                self.rotaryCallback(self.CLOCKWISE)
                subprocess.call(['mpc', 'volume', '+2'])

    #  when buttton pressed
    def _switchCallback(self, pin):
        if GPIO.input(self.switchPin) == 0:
            self.switchCallback()
            subprocess.call(['mpc','toggle'])
            track_Counter += 1
            print str(track_Counter)

            if track_Counter == 3:
                subprocess.call(['mpc','next'])
                track_Counter = 0



#test
if __name__ == "__main__":
    
    #set your pins here
    CLOCKPIN = 5
    DATAPIN = 6
    SWITCHPIN = 13

    def rotaryChange(direction):
        print "turned - " + str(direction)


    def switchPressed():
        print "button pressed"


    GPIO.setmode(GPIO.BCM)
    
    ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN, rotaryChange, switchPressed)

    ky040.start()

    try:
        while True:
            sleep(0.1)
    finally:
        ky040.stop()
        GPIO.cleanup()