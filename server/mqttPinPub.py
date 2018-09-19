import paho.mqtt.client as mqtt #import the client1
import uuid


uniqeId = str(uuid.uuid4().hex)
broker_address="192.168.1.200"

def pub(pin,val):
    client = mqtt.Client(uniqeId) #create new instance
    client.connect(broker_address) #connect to broker
    top = "/device/PinD"
    topic = top + str(pin)
    value = str(val)
    client.publish(topic,value)#publish