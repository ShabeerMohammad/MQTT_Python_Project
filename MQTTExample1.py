import paho.mqtt.client as mqtt
import time

###########################

def on_message(client,userdata,message):
    print("message received",str(message.payload.decode('utf-8')))
    print("message topic=",message.topic)
    print('message qos=',message.qos)
    print("message retain flag=",message.retain)

########################################

broker_address='192.168.225.54'
#broker_address = 'iot.eclipse.org'

print("Creating a new instance")
client=mqtt.Client("P1")

#client.on_message = on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address)

#client.loop_start() #start the loop

print('Subscribe to topic',"house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")

print('Publishing message to topic',"house/bulbs/bulb1")
client.publish("house/bulbs/bulb1",'OFF')

time.sleep(4) #wait
#client.loop_stop()  #stop the loop

