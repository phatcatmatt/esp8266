from sys import print_exception
import blink
import wifitest
import buttonsensor

try:
    wifitest.connect()
except AssertionError as error:
    print(error)
    blink.slow()
    with open(file='error_logs.txt', mode='w') as f:
        print_exception(error, f)
# connection successful
else:
    blink.fast()
    buttonsensor.button()
