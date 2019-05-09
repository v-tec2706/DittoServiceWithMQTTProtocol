import paho.mqtt.client as mqtt  # add paho-mqtt package
import time
import json
import random


def working_loop():
    client_name = "simple_mock"
    broker_address = "127.0.0.1"
    topic = "ditto-tutorial/my.test"

    message = {'thingID': 'octopus', 'temp': '0.0', 'alt': '0.0'}

    client = mqtt.Client(client_name)
    client.connect(broker_address)

    while True:
        message['temp'] = random.uniform(-10, 20)
        message['alt'] = random.uniform(0, 10000)

        json_message = json.dumps(message)

        client.publish(topic, json_message)
        time.sleep(3)


working_loop()
