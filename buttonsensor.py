from machine import Pin
from time import sleep

btn = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)


def button():
    while True:
        led.value(not btn.value())
        sleep(.2)
