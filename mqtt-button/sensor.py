from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient
import secrets

btn = Pin(14, Pin.IN, Pin.PULL_UP)

state = ''
OPEN = 1
CLOSED = 0

client = MQTTClient(secrets.clientId, secrets.server)


def connect():
    client.connect()


def wait(led):
    global state

    while True:
        btnStatus = btn.value()
        # set LED opposite of button
        led.value(btnStatus)
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
