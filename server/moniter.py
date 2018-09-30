import mqttPinSub
import sensor

moniter = mqttPinSub

if __name__ == '__main__':
    moniter.moniter()
    sensor.moniter()