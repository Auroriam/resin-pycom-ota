from network import WLAN
import socket
import time
from OTA import WiFiOTA
from time import sleep
import pycom
import binascii

from config import WIFI_SSID, WIFI_PASS, SERVER_IP, SERVER_PORT

# Turn on GREEN LED
pycom.heartbeat(False)
pycom.rgbled(0x550000)

# Setup OTA
ota = WiFiOTA(WIFI_SSID,
              WIFI_PASS,
              SERVER_IP,  # Update server address
              SERVER_PORT)  # Update server port

# Show blue LED for 1.0.0
pycom.rgbled(0x000055)

# Perform OTA
ota.connect()
ota.update()

sleep(5)
