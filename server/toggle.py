import fileHandle as getCur
import mqttPinPub as mqtt

def toggle(pin):
    pinName = 'pin' + str(pin)
    currentState =getCur.read(pinName)
    if currentState == 1:
        nextState = 0
        mqtt.pub(pin,nextState)

    else:
        nextState = 1
        mqtt.pub(pin,nextState)