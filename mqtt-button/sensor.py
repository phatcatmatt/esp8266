from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient
import esp
import secrets

btn = Pin(14, Pin.IN, Pin.PULL_UP)

state = ''
OPEN = 1
CLOSED = 0

client = MQTTClient(secrets.topic, secrets.ip)


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
            # esp.deepsleep()
        else:
            client.publish('ibs', 'CLOSED')
            state = CLOSED
            # esp.deepsleep(30e6)
        sleep(1)
