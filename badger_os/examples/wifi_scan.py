import badger2040
from badger2040 import WIDTH
import network

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

y = 35 + int(LINE_HEIGHT / 2)

nic = network.WLAN(network.STA_IF)
nic.active(True)
for net in nic.scan():
    ssid, bssid, channel, RSSI, security, hidden = net
    display.text("> {}".format(ssid), 0, y, WIDTH)
    y += LINE_HEIGHT

display.update()

# Call halt in a loop, on battery this switches off power.
# On USB, the app will exit when A+C is pressed because the launcher picks that up.
while True:
    display.keepalive()
    display.halt()
