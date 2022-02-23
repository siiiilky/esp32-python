import config
import functions
from machine import Pin
try:
  import usocket as socket
except:
  import socket

wifi = functions.connect_to_wifi(config.ssid, config.password)
# Print out the network configuration received from DHCP
print('network config:', wifi.ifconfig())
# Create an output pin on GPIO 22
relay1 = Pin(22, Pin.OUT)
# Create an output pin on GPIO 23
relay2 = Pin(23, Pin.OUT)
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
    response = functions.web_page(relay1, relay2)
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()