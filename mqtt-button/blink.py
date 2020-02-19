from time import sleep


def slow(led):
    for _ in range(4):
        led.value(not led.value())
        sleep(1)


def fast(led):
    for _ in range(6):
        led.value(not led.value())
        sleep(.1)
