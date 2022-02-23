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


def web_page(relay1, relay2):
    # Set relay_state variable based on state returned from output pins
    if relay1.value() == 1:
        relay1_state = "ON"
    else:
        relay1_state = "OFF"
    if relay2.value() == 1:
        relay2_state = "ON"
    else:
        relay2_state = "OFF"

    # Create a variable containing the HTML to be sent, the state of the relays are contained in the variables we have just set
    html = """<html>
      <head> 
        <title>MicroPython Web Server</title> 
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="data:,">
        <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;} h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #006400; border: none; border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}.button2{background-color: #dc143c;}</style>
      </head>
      <body> 
        <h1>MicroPython Web Server</h1> 
        <p>Relay 1 state: <strong>""" + relay1_state + """</strong></p>
        <p>
          <a href="/?relay1=on"><button class="button">ON</button></a>
          <a href="/?relay1=off"><button class="button button2">OFF</button></a>
        </p>
        <p>Relay 2 state: <strong>""" + relay2_state + """</strong></p>
        <p>
          <a href="/?relay2=on"><button class="button">ON</button></a>
          <a href="/?relay2=off"><button class="button button2">OFF</button></a>
        </p>
      </body>
    </html>"""
    # Return the HTML
    return html