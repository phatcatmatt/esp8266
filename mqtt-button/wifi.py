import network
from machine import Pin
import time
import secrets

ssid = secrets.ssid
password = secrets.password


def connect():
    # make sure internal wifi access point is off
    network.WLAN(network.AP_IF).active(False)
    # connect to wifi
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)
    time.sleep(6)
    assert sta_if.isconnected(), sta_if.status()
