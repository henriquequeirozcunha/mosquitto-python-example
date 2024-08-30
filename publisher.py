#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Publish some messages to queue
"""
import paho.mqtt.publish as publish


msgs = [{'topic': "kids/yolo", 'payload': "jump"},
        {'topic': "adult/pics", 'payload': "some photo"},
        {'topic': "adult/news", 'payload': "extra extra"},
        {'topic': "adult/news", 'payload': "super extra"}]

host = "localhost"


if __name__ == '__main__':
    # publish a single message
    while True:
        import random as rand
        import json
        payload1 = rand.randint(1, 10)
        payload2 = rand.randint(11, 20)
        # encoded = json.dumps(, indent=2).encode('utf-8')
        # print(type(encoded))
        publish.single(topic="test", payload=json.dumps({'Vel. Média': payload1, 'Pot.': payload2}), hostname=host, port=3001)

        # publish.single(topic="fernando", payload=payload2, hostname=host, port=3001)


    # publish multiple messages
    # publish.multiple(msgs, hostname=host)


# vi: set fileencoding=utf-8 :
