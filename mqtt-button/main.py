from sys import print_exception
import blink
import wifi
import sensor


def handleError(error):
    print(error)
    blink.slow()
    with open(file='error_logs.txt', mode='w') as f:
        print_exception(error, f)


try:
    wifi.connect()
except AssertionError as error:
    handleError(error)

try:
    sensor.connect()
except AssertionError as error:
    handleError(error)
else:
    blink.fast()
    sensor.wait()
