import json

fileName = 'pinStat.json'

def init():
    fileObject = open(fileName,"w") # w->rewrite content in file
    initData ={
                "pin0": 0,
                "pin1": 0,
                "pin2": 0,
                "pin3": 0,
                "pin4": 0,
                "pin5": 0,
                "pin6": 0,
                "pin7": 0,
                "pin8": 0
                }

    json.dump(initData, fileObject)


def read(pin):
    fileObject = open(fileName,"r") # w->rewrite content in file
    data = json.load(fileObject)
    val = data[pin]
    return val


def write(pin,val):
    fileObject = open(fileName,"r") # w->rewrite content in file
    data = json.load(fileObject)

    data[pin] = val

    fileObject = open(fileName,"w")
    json.dump(data, fileObject)

# init()
# print(read('pin3'))
# write('pin3',1)
# print(read('pin3'))
# write('pin3',2)
# print(read('pin3'))
# write('pin3',3)
# print(read('pin3'))