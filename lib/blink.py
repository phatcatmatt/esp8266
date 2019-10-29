from machine import Pin
from time import sleep

# D8
led = Pin(15, Pin.OUT)


def slow():
    for _ in range(3):
        led.value(not led.value())
        sleep(1)
        led.value(not led.value())
        sleep(1)


def fast():
    for _ in range(10):
        led.value(not led.value())
        sleep(.1)
        led.value(not led.value())
        sleep(.1)
