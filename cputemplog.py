from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt

cpu = CPUTemperature()

plt.ion()
x = []
y = []

def write_temp(temp):
    with open("/home/toddp/PythonProjects/cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()


while True:
    temp = cpu.temperature
    write_temp(temp)
    # convert cpu temp to fahrenheit
    ftemp = (temp * 1.8) + 32
    # round down to 2 decimal places
    cputemp = round(ftemp, 2)
#    print(str(cputemp))

    graph(temp)
    plt.pause(1)
    sleep(30)