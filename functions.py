import network

def connect_to_wifi(ssid, password):
    print("Connecting to wifi...")
    # Activate the station interface
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    # Connect to your wifi network
    sta_if.connect(ssid, password)
    # Wait until the wireless is connected
    while not sta_if.isconnected():
        pass
    return sta_if
