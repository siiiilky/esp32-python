import config
import network

print("Connecting to wifi...")
# Activate the station interface
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
# Connect to your wifi network
sta_if.connect(config.ssid, config.password)
while not sta_if.isconnected():
    pass
# Do an ifconfig
print('network config:', sta_if.ifconfig())

