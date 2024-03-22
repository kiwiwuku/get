import RPi.GPIO as GPIO

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        snum = input("Type a number from 0 to 255: ")
        try:
            fnum = float(snum)
            if (not fnum.is_integer()):
                print("Number is float, not integer, Try again...")
                continue
            num = int(snum)
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))

                voltage = fnum / 256.0 * 3.3
                print(f"Output voltage is {voltage:.4} volt")
            else:
                if num < 0:
                    print("Number is <0, Try again...")
                elif num > 255:
                    print("Number is out of range [0,255], Try again...")  
        except Exception:
            if num == "q": break
            print("You have to type a number, not string, Try again...")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("END")
    