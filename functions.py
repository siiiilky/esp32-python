import config
import network

def connect_to_wifi():
    print("Connecting to wifi...")
    # Activate the station interface
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    # Connect to your wifi network
    sta_if.connect(config.ssid, config.password)
    # Wait until the wireless is connected
    while not sta_if.isconnected():
        pass
    return sta_if
