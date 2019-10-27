import network
import time
import secrets

ssid = secrets.ssid
password = secrets.password

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
for _ in range(10):
    sta_if.connect(ssid, password)
    time.sleep(1)
    if sta_if.isconnected():
        print('Connected to {0}'.format(ssid))
        break
    time.sleep(11)
else:
    print('Failed to connect to {0}'.format(ssid))
    print(sta_if.status())
