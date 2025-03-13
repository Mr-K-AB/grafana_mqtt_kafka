import random
import time
import json
import paho.mqtt.client as mqtt
from datetime import datetime

# MQTT Configuration
MQTT_BROKER = "mosquitto"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/sensor"

def simulate_sensor_data():
    client = mqtt.Client()
    client.connect(MQTT_BROKER, MQTT_PORT, 60)

    while True:
        payload = {
            "device_id": f"sensor_{random.randint(1, 10)}",
            "timestamp": datetime.utcnow().isoformat(),
            "temperature": round(random.uniform(20, 35), 2),
            "humidity": random.randint(30, 80)
        }
        client.publish(MQTT_TOPIC, json.dumps(payload))
        print(f"Published: {payload}")
        time.sleep(2)

if __name__ == "__main__":
    simulate_sensor_data()
