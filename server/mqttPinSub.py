import paho.mqtt.client as mqtt #import the client1
import time
import uuid
import fileHandle as fs

initMsg0 = str()
initMsg1 = str()
initMsg2 = str()
initMsg3 = str()
initMsg4 = str()
initMsg5 = str()
initMsg6 = str()
initMsg7 = str()
initMsg8 = str()

uniqeId = str(uuid.uuid4().hex)

val = [0,0,0,0,0,0,0,0,0]


############
def on_message_0(client, userdata, message):
    val[0] = int(str(message.payload.decode("utf-8")))
    fs.write('pin0',val[0])
    print(val)
########################################


############
def on_message_1(client, userdata, message):
    val[1] = int(str(message.payload.decode("utf-8")))
    fs.write('pin1',val[1])
    print(val)
########################################


############
def on_message_2(client, userdata, message):
    val[2] = int(str(message.payload.decode("utf-8")))
    fs.write('pin2',val[2])
    print(val)
########################################

############
def on_message_3(client, userdata, message):
    val[3] = int(str(message.payload.decode("utf-8")))
    fs.write('pin3',val[3])
    print(val)
########################################

############
def on_message_4(client, userdata, message):
    val[4] = int(str(message.payload.decode("utf-8")))
    fs.write('pin4',val[4])
    print(val)
########################################


############
def on_message_5(client, userdata, message):
    val[5] = int(str(message.payload.decode("utf-8")))
    fs.write('pin5',val[5])
    print(val)
########################################


############
def on_message_6(client, userdata, message):
    val[6] = int(str(message.payload.decode("utf-8")))
    fs.write('pin6',val[6])
    print(val)
########################################




############
def on_message_7(client, userdata, message):
    val[7] = int(str(message.payload.decode("utf-8")))
    fs.write('pin7',val[7])
    print(val)
########################################


############
def on_message_8(client, userdata, message):
    val[8] = int(str(message.payload.decode("utf-8")))
    fs.write('pin8',val[8])
    print(val)
########################################


############
def on_message(client, userdata, message):
    print("Subscription",str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################




def moniter():
    broker_address="192.168.1.200"
    #broker_address="iot.eclipse.org"
    #print("creating new instance")
    client = mqtt.Client(uniqeId) #create new instance
    client.on_message=on_message #attach function to callback
    client.message_callback_add("/device/PinD0", on_message_0)
    client.message_callback_add("/device/PinD1", on_message_1)
    client.message_callback_add("/device/PinD2", on_message_2)
    client.message_callback_add("/device/PinD3", on_message_3)
    client.message_callback_add("/device/PinD4", on_message_4)
    client.message_callback_add("/device/PinD5", on_message_5)
    client.message_callback_add("/device/PinD6", on_message_6)
    client.message_callback_add("/device/PinD7", on_message_7)
    client.message_callback_add("/device/PinD8", on_message_8)
    #print("connecting to broker")
    client.connect(broker_address) #connect to broker
    #start the loop
    #print("Subscribing to topic","/device/PinD#")

    client.subscribe("/device/#")
    client.loop_forever()