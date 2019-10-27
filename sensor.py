from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient

btn = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

client = MQTTClient('inner-sanctum', '192.168.1.248')
client.connect()

status = ''
available = 1
occupied = 0

while True:
    led.value(btn.value())
    if btn.value() == available:
        client.publish('ibs', 'OPEN')
    else:
        client.publish('ibs', 'CLOSED')
    sleep(2)
