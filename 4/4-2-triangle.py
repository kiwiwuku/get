import RPi.GPIO as GPIO
from time import sleep
import numpy as np

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

flag = 1
x = 0

try:
    period = float(input("Type a period for sygnal: "))

    while True:
        GPIO.output(dac, dec2bin(x))

        if x == 0: flag = 1
        elif x == 255: flag = 0

        x = x + 1 if flag == 1 else x - 1

        sleep(period/512)

except ValueError:
    print("Inapropriate period")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("END")
    