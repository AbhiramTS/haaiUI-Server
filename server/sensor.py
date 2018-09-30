import sensorData as sensor
import sensorFile as file

def moniter():
    file.init()
    sensor.moniter()


def getData(sensorKey):
    val = file.read(sensorKey)
    return val