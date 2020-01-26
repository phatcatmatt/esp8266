from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient

btn = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

state = ''
OPEN = 1
CLOSED = 0

client = MQTTClient('inner-sanctum', '192.168.1.248')


def connect():
    client.connect()
    # assert client.connect()


def wait():
    global state

    while True:
        btnStatus = btn.value()
        # set LED opposite of button
        led.value(not btnStatus)
        print(btnStatus)
        if btnStatus == state:
            pass
        elif btnStatus == OPEN:
            client.publish('ibs', 'OPEN')
            state = OPEN
        else:
            client.publish('ibs', 'CLOSED')
            state = CLOSED
        sleep(1)
