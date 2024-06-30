import time
import json
import random
import paho.mqtt.client as mqtt

# AWS IoT details
broker = "YOUR_AWS_IOT_ENDPOINT"
port = 8883
topic = "iot/temperature"
client_id = "temperature_sensor"
ca_path = "path/to/AmazonRootCA1.pem"
cert_path = "path/to/certificate.pem.crt"
key_path = "path/to/private.pem.key"


# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    if rc == 0:
        print("Connection successful")
    else:
        print(f"Connection failed with code {rc}")

def on_publish(client, userdata, mid):
    print(f"Message {mid} published.")

def on_log(client, userdata, level, buf):
    print(f"Log: {buf}")

# MQTT Client
client = mqtt.Client(client_id, protocol=mqtt.MQTTv311)
client.tls_set(ca_path, certfile=cert_path, keyfile=key_path)
client.on_connect = on_connect
client.on_publish = on_publish
client.on_log = on_log
client.connect(broker, port)

# Function to simulate temperature data
def get_temperature():
    return round(random.uniform(20.0, 35.0), 2)

# Publish data to AWS IoT Core
client.loop_start()
while True:
    temperature = get_temperature()
    payload = json.dumps({"sensor_id": "sensor_1", "timestamp": int(time.time()), "temperature": temperature})
    result = client.publish(topic, payload)
    status = result.rc
    if status == 0:
        print(f"Published: {payload}")
    else:
        print(f"Failed to send message to topic {topic}")
    time.sleep(10)  # Publish data every 10 seconds