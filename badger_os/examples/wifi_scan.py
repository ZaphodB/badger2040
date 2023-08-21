import badger2040
from badger2040 import WIDTH
import network
# from enum import Enum


# class Security(Enum):
#     open = 0
#     WEP = 1
#     WPA_PSK = 2
#     WPA2_PSK = 3
#     WPA_WPA2_PSK = 4
#
#
# class Visibility(Enum):
#     visible = 0
#     hidden = 1


TEXT_SIZE = 1
LINE_HEIGHT = 16

# Display Setup
display = badger2040.Badger2040()
display.led(128)

# Page Header
display.set_pen(15)
display.clear()
display.set_pen(0)
display.rectangle(0, 0, WIDTH, 20)
display.set_pen(0)
display.set_font('bitmap8')

y = 35 + int(LINE_HEIGHT / 2)

nic = network.WLAN(network.STA_IF)
nic.active(True)
nets = nic.scan()
# sort by 4th item (RSSI) descending
nets.sort(key=lambda x: x[3], reverse=True)
for net in nets:
    ssid, bssid, channel, RSSI, security, hidden = net
    # display.text("{} {} {} {}".format(Visibility(hidden).name, str(RSSI), ssid.decode("utf-8"), Security(security).name), 0, y, WIDTH)
    display.text("{} {} {} {}".format(str(hidden), str(RSSI), ssid.decode("utf-8"), str(security)), 0, y, WIDTH)
    y += LINE_HEIGHT

display.update()

# Call halt in a loop, on battery this switches off power.
# On USB, the app will exit when A+C is pressed because the launcher picks that up.
while True:
    display.keepalive()
    display.halt()
