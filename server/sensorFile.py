import json

fileName = 'sensorStat.json'

def init():
    fileObject = open(fileName,"w") # w->rewrite content in file
    initData ={
                "h": 0.0,
                "t": 0.0,
                "l": 0.0,
                "m": 0.0
                }

    json.dump(initData, fileObject)


def read(sensor):
    fileObject = open(fileName,"r") # w->rewrite content in file
    data = json.load(fileObject)
    val = data[sensor]
    return val


def write(sensor,val):
    fileObject = open(fileName,"r") # w->rewrite content in file
    data = json.load(fileObject)

    data[sensor] = val

    fileObject = open(fileName,"w")
    json.dump(data, fileObject)
