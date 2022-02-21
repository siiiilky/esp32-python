import functions
from machine import Pin
from time import sleep

wifi = functions.connect_to_wifi()
# Print out the network configuration received from DHCP
print('network config:', wifi.ifconfig())

# ESP32 GPIO 22
relay1 = Pin(22, Pin.OUT)
# ESP32 GPIO 23
relay2 = Pin(23, Pin.OUT)
while True:
  # RELAY ON
  relay1.value(0)
  relay2.value(1)
  sleep(10)
  # RELAY OFF
  relay1.value(1)
  relay2.value(0)
  sleep(10)