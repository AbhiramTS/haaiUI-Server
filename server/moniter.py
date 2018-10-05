from multiprocessing import Process as process
import mqttPinSub
import sensor

moniter = mqttPinSub

def pro1():
    print("process 1")
    moniter.moniter()

def pro2():
    print("process 2")
    sensor.moniter()

if __name__ == '__main__':
    p1 = process(target = pro1)
    p2 = process(target = pro2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()