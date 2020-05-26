#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO | Relay
#--------------
# 26     01
# 19     02
# 13     03
# 06     04
# 12     05
# 16     06
# 20     07
# 21     08

# initiate list with pin gpio pin numbers

gpioList = [26, 19, 13, 06, 12, 16, 20, 21]

for i in gpioList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# Sleep time variables

sleepTimeShort = 2
sleepTimeLong = 1

# MAIN LOOP =====
# ===============

try:
    while True:
        guess = int(input('Enter 1 through 8: '))
        if int==i in gpioList:
            GPIO.output(i, GPIO.LOW)
        else:
            GPIO.output(i, GPIO.HIGH)

# End program cleanly with keyboard
except KeyboardInterrupt:
    print " Quit"

    # Reset GPIO settings

    GPIO.cleanup()