import paho.mqtt.client as mqtt
import blinky

CLOSED = 'CLOSED'
OPEN = 'OPEN'
PING = 'PING'

state = CLOSED


def parse_message(msg):
    global state
    # print(state)
    # todo this logic is horrible, clean it up
    if state == CLOSED:
        if msg == CLOSED:
            print('closed -> closed')
            blinky.rojo()
        else:
            print('closed -> open')
            state = OPEN
            blinky.verde()

    elif state == OPEN:
        if msg == CLOSED:
            print('open -> closed')
            state = CLOSED
            blinky.rojo()
        else:
            print('open ->  open')
            blinky.verde()


def on_connect(client, userdata, flags, rc):
    print('connected with code {0}'.format(rc))
    client.subscribe('ibs')
    blinky.pong()


def on_message(client, userdata, msg):
    parse_message(msg.payload.decode('utf-8'))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost')

client.loop_forever()
