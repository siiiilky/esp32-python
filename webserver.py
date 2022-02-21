import config
import functions
from machine import Pin
try:
  import usocket as socket
except:
  import socket
from time import sleep

wifi = functions.connect_to_wifi(config.ssid, config.password)
# Print out the network configuration received from DHCP
print('network config:', wifi.ifconfig())

# ESP32 GPIO 22
relay1 = Pin(22, Pin.OUT)
# ESP32 GPIO 23
relay2 = Pin(23, Pin.OUT)

def web_page():
    if relay1.value() == 1:
        relay1_state = "ON"
    else:
        relay1_state = "OFF"
    if relay2.value() == 1:
        relay2_state = "ON"
    else:
        relay2_state = "OFF"

    html = """<html><head> <title>MicroPython Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #006400; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #dc143c;}</style></head><body> <h1>MicroPython Web Server</h1> 
  <p>Relay 1 state: <strong>""" + relay1_state + """</strong></p><p><a href="/?relay1=on"><button class="button">ON</button></a><a href="/?relay1=off"><button class="button button2">OFF</button></a></p>
  <p>Relay 2 state: <strong>""" + relay2_state + """</strong></p><p><a href="/?relay2=on"><button class="button">ON</button></a><a href="/?relay2=off"><button class="button button2">OFF</button></a></p></body></html>"""
    return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    relay1_on = request.find('/?relay1=on')
    relay1_off = request.find('/?relay1=off')
    if relay1_on == 6:
        print('Relay 1 ON')
        relay1.value(1)
    if relay1_off == 6:
        print('Relay 1 OFF')
        relay1.value(0)
    relay2_on = request.find('/?relay2=on')
    relay2_off = request.find('/?relay2=off')
    if relay2_on == 6:
        print('Relay 2 ON')
        relay2.value(1)
    if relay2_off == 6:
        print('Relay 2 OFF')
        relay2.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()