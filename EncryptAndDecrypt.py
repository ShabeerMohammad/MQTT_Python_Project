import time
import paho.mqtt.client as paho
from cryptography.fernet import Fernet

#local address is 192.168.225.54
#External Brokers #'broker.hivemq.com' #test.mosquitto.org #iot.eclipse.org #mqtt.eclipse.org

#define the broker
broker = 'test.mosquitto.org'   #external broker

#define callback to connect and decrypt the message

def on_connect(client,userdata,flags,rc):
    print("Connected with result code : "+str(rc))

def on_message(client,userdata,message):
    time.sleep(1)
    print('receive payload',message.payload)

    if message.payload == encrypted_message:
     print("\n published and received messages are the same")

    decrypted_message = code.decrypt(message.payload)
    print("\nreceived message=",str(decrypted_message.decode("utf-8")))     #print the encrypted data

    print("message topic=",message.topic)   #print the topic
    print("message qos=",message.qos)       #print the quality of service level to use
    print("message retain flag=",message.retain)    #print the last known good / retained message for the topic

    client.disconnect()     #disconnecting from the client
    client.loop_stop()      #stopping from the loop

#for log purose
#def on_log(client,userdata,level,buf):
#    print("log: ",buf)

#create a client instance
client = paho.Client("Data_Cipher-01")

client.on_connect = on_connect
client.on_message = on_message
#client.on_log = on_log

#Encryption with the key

key = Fernet.generate_key()
print("key :",key)
code = Fernet(key)
print("code :",code)
message = b'The message is successfully encrypted and decrypted'
encrypted_message = code.encrypt(message)
out_message = encrypted_message.decode()    #create a UTF-8 encoded string to pass as the message payload to MQTT publish method

print("connecting to the broker",broker)
client.connect(broker)
client.loop_start()     #start loop to process received messages

print('subscribing to the topic')
client.subscribe("Encrypt/Data")
time.sleep(2)

print("publishing encrypted message",encrypted_message)
client.publish("Encrypt/Data",out_message)      #publishing the topic
time.sleep(4)






