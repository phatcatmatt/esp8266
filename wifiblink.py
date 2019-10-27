import network
from machine import Pin
import time
import blink
import secrets

ssid = secrets.ssid
password = secrets.password

# D8
led = Pin(15, Pin.OUT)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
for _ in range(1):
    sta_if.connect(ssid, password)
    time.sleep(1)
    if sta_if.isconnected():
        blink.fast()
        print('Connected to {0}'.format(ssid))
        print(sta_if.status())
        break
    time.sleep(11)
else:
    blink.slow()
    print('Failed to connect to {0}'.format(ssid))
    print(sta_if.status())
