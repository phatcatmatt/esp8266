from sys import print_exception
from machine import Pin, deepsleep
import blink
import wifi
from umqtt.simple import MQTTClient
import secrets
from time import sleep

# built in led
LED = Pin(2, Pin.OUT)


def handleError(error):
    print(error)
    blink.slow(LED)
    with open(file='error_logs.txt', mode='w') as f:
        print_exception(error, f)


client = MQTTClient(secrets.clientId, secrets.server)

try:
    wifi.connect()
except AssertionError as error:
    handleError(error)

try:
    client.connect()
except AssertionError as error:
    handleError(error)
else:
    print('sensor online')
    blink.fast(LED)
   # todo: send the message immediately, sleep 1 min
    client.publish('ibs', 'CLOSED')
    sleep(5)
    print('going to sleepsies')
    deepsleep(5 * 1000)
