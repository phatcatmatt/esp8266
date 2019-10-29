from sys import print_exception
import blink
import wifi
import sensor

try:
    wifi.connect()
except AssertionError as error:
    print(error)
    blink.slow()
    with open(file='error_logs.txt', mode='w') as f:
        print_exception(error, f)
# connection successful
else:
    blink.fast()
    sensor.sense()
