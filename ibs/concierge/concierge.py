# this is technically neither a server nor a broker
# the MQTT broker runs as a daemon when the pi boots
# this is just a client that subscribes to the topic and listens

import paho.mqtt.client as mqtt
# import blinky
import asyncio

CLOSED = 'CLOSED'
OPEN = 'OPEN'

state = OPEN


async def timer():
    global state;
    print('timer go');
    try:
        await asyncio.sleep(10)
        print('door open?')
        state = OPEN
    except asyncio.CancelledError:
        print('timer cancelled')
        raise
    # finally:
    #     print('finally')
    # if it's been 1 min
    # set state as open
    # send slack message


def handle_message(msg):
    global state
    if state == CLOSED:
        if msg == CLOSED:
            # asyncio.canc
            # reset timer
            # reset state?
            pass
    elif state == OPEN:
        if msg == CLOSED:
            state = CLOSED
            # blinky.rojo()
            # set timer
            print('door now closed')
            # asyncio.create_task(timer())
            asyncio.run(timer())
            # send closed slack message


def on_connect(client, userdata, flags, rc):
    print('connected with code {0}'.format(rc))
    client.subscribe('ibs')
    # blinky.pong()


def on_message(client, userdata, msg):
    handle_message(msg.payload.decode('utf-8'))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# client.connect('localhost')
client.connect('192.168.1.248')

client.loop_forever()
