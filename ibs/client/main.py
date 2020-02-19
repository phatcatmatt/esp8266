from sys import print_exception
from machine import Pin
import blink
import wifi
import sensor

# built in led
LED = Pin(2, Pin.OUT)


def handleError(error):
    print(error)
    blink.slow(LED)
    with open(file='error_logs.txt', mode='w') as f:
        print_exception(error, f)


try:
    wifi.connect()
except AssertionError as error:
    handleError(error)

try:
    sensor.connect()
except AssertionError as error:
    handleError(error)
else:
    print('sensor online')
    blink.fast(LED)
    sensor.wait(LED)
