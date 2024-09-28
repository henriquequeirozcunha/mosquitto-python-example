#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Publish some messages to queue
"""
import paho.mqtt.publish as publish
import json
import random as rand
import time

host = "localhost"
start_time = time.time()
reset_interval = 5 * 60  # 5 minutos em segundos
received_request = False

if __name__ == '__main__':

    while True:
        elapsed_time = time.time() - start_time
        y = {
            'Wind Speed': rand.random(),
            'Wind Power Density (Watts/m2)': rand.random(),
            'Wind Power (Watts)': rand.random(),
            'Air Density (kg/m^3)': rand.random(),
            'Temperature (F)': rand.randint(32, 122),
            'Pressure (mmHg)': rand.uniform(20.0, 100.0),
        }

        if elapsed_time >= reset_interval:
            if not received_request:
                raise Exception('Simulando 5 minutos sem response da API')
            else:
                received_request = False
                elapsed_time = 0

        publish.single(topic="test", payload=json.dumps(y), hostname=host, port=1883)
        received_request = True
        time.sleep(1)