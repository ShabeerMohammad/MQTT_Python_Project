import paho.mqtt.client as mqtt

# This is the publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("topic/test","Hello world!");
client.disconnect();


