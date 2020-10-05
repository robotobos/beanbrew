# beanbrew
espressif-based coffee pot controller with Android

# Intro

This will essentially be an IoT plug, but I will use it to replace the broken on/off switch for my coffee pot. 

We'll get the PoC working with MicroPython.

#Board Setup

Here's the commands I've been using to start running:

### This is to flash the micropython binary

Erase Flash:
```esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash```

Push firmware:
```esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 115200 write_flash -z 0x1000 esp32spiram-idf4-20191220-v1.12.bin```

Connect to board:
```sudo minicom -D /dev/ttyUSB0 -b 115200```
*the REPL is having trouble accepting keyboard input. Current workaround is try to open the port in another program, then come back to REPL. Will look into this. 

Push Python to board:
```ampy --port /dev/ttyUSB0 put main.py```

Run script on board:
```ampy --port /dev/ttyUSB0 run main.py```

Test client:
Change the parameter in the python testClient.py to on/off to activate the switch light


#TODO

#BOM

#Refs
Espressif Dev Kit: https://docs.espressif.com/projects/esp-idf/en/stable/hw-reference/get-started-devkitc.html

Micropython ESP32 Binaries: https://micropython.org/download/esp32/

ESP32 MicroPython dev: https://docs.micropython.org/en/latest/esp32/general.html

