import network
from machine import Pin
import time
import blink
import secrets

ssid = secrets.ssid
password = secrets.password


def connect():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)
    time.sleep(5)
    assert sta_if.isconnected(), sta_if.status()
