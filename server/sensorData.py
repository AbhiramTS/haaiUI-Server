import paho.mqtt.client as mqtt #import the client1
import time
import uuid
import sensorFile as fs

initMsg0 = str()
initMsg1 = str()
initMsg2 = str()
initMsg3 = str()


uniqeId = str(uuid.uuid4().hex)

val = [0.0, 0.0, 0.0, 0.0]


############
def on_message_0(client, userdata, message):
    val[0] = float(str(message.payload.decode("utf-8")))
    fs.write('h',val[0])
    print(val)
########################################


############
def on_message_1(client, userdata, message):
    val[1] = float(str(message.payload.decode("utf-8")))
    fs.write('t',val[1])
    print(val)
########################################


############
def on_message_2(client, userdata, message):
    val[2] = float(str(message.payload.decode("utf-8")))
    fs.write('l',val[2])
    print(val)
########################################

############
def on_message_3(client, userdata, message):
    val[3] = float(str(message.payload.decode("utf-8")))
    fs.write('m',val[3])
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
    print("creating new instance")
    client = mqtt.Client(uniqeId) #create new instance
    client.on_message=on_message #attach function to callback
    client.message_callback_add("/sensor/humidity", on_message_0)
    client.message_callback_add("/sensor/temperature", on_message_1)
    client.message_callback_add("/sensor/ldr", on_message_2)
    client.message_callback_add("/sensor/motion", on_message_3)
    print("connecting to broker")
    client.connect(broker_address) #connect to broker
    #start the loop
    #print("Subscribing to topic","/device/PinD#")

    client.subscribe("/sensor/#")
    client.loop_forever()

# if __name__ == '__main__':
#     fs.init()
#     moniter()