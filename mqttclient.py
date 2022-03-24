import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import esp
esp.osdebug(None)
import gc
gc.collect()
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
client_id = ubinascii.hexlify(machine.unique_id())
last_message = 0
message_interval = 5
counter = 0

def sub_cb(topic, msg):
  print((topic, msg))
  if topic == config.mqtt_topic_sub and msg == b'up-on':
    print('Garage Door Up Activated')
    relay1.value(1)
  elif topic == config.mqtt_topic_sub and msg == b'up-off':
    print('Garage Door Up Dectivated')
    relay1.value(0)
  elif topic == config.mqtt_topic_sub and msg == b'down-on':
    print('Garage Door Down Activated')
    relay2.value(1)
  elif topic == config.mqtt_topic_sub and msg == b'down-off':
    print('Garage Door Down Dectivated')
    relay2.value(0)

def connect_and_subscribe():
  global client_id
  client = MQTTClient(client_id, config.mqtt_server, config.mqtt_port, config.mqtt_user, config.mqtt_password)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(config.mqtt_topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (config.mqtt_server, config.mqtt_topic_sub))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
  except OSError as e:
    restart_and_reconnect()