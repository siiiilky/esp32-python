import config
import network

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

