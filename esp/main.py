import machine
import time

p22_green = machine.Pin(22, machine.Pin.OUT)
p23_red = machine.Pin(23, machine.Pin.OUT)

while True:
    p23_red.value(1)
    p22_green.value(1)

    time.sleep(1)

    p23_red.value(0)
    p22_green.value(0)

    time.sleep(1)
