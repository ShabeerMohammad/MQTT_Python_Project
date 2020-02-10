import paho.mqtt.client as mqtt
#This is the subscriber

def on_connect(client,userdata,flags,rc):
    print("Connected with result code"+str(rc))
    client.subscribe("topic/test")

def on_message(client,userdata,msg):
    if msg.payload.decode()=="Hello World!":
        print('Yes')
        client.disconnect()

client = mqtt.Client()
client.connect("THE_IP_ADDRESS_OF_OUT_BROKER",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

