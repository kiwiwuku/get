import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(num):
    return [int(elem) for elem in bin(num)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        dac_val = [int(elem) for elem in bin(k)[2:].zfill(8)]
        GPIO.output(dac, dac_val)
        sleep(0.006)
        comp_val = GPIO.input(comp)
        if comp_val == GPIO.LOW:
            k -= 2**i
    return k

def adc2():
    k = 2**7
    for i in range(6, 0, -1):
        temp = k + 2**i

        dac_val = [int(elem) for elem in bin(temp)[2:].zfill(8)]
        GPIO.output(dac, dac_val)
        sleep(0.006)
        comp_val = GPIO.input(comp)

        if comp_val == 0:
            k = temp
        else:
            k -= 2**i
    return k
try:
    while True:
        i = adc2()
        voltage = i * 3.3 / 256.0
        print("i = " + str(i) + "; voltage = " + str(voltage))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")