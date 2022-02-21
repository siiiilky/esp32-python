import config
import network
from machine import Pin
from time import sleep

print("Connecting to wifi...")
# Activate the station interface
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# Connect to your wifi network
sta_if.connect(config.ssid, config.password)
# Wait until the wireless is connected
while not sta_if.isconnected():
    pass
# Print out the network configuration received from DHCP
print('network config:', sta_if.ifconfig())

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