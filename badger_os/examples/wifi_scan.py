import badger2040
import network
import time

Security = (
    'open',
    'WEP',
    'WPA-PSK',
    'WPA2-PSK',
    'WPA/WPA2-PSK',
    'WPA2-Enterprise',
    'WPA3-PSK',
    'WPA2/WPA3-PSK',
    'WAPI-PSK',
    'OWE',
    'MAX'
)


Visibility = (
    'visible',
    'hidden',
    '?',
    '?',
    '?',
    '?',
    '?',
    '?',
    '?'
)

button_a = badger2040.BUTTONS[badger2040.BUTTON_A]
button_b = badger2040.BUTTONS[badger2040.BUTTON_B]
button_c = badger2040.BUTTONS[badger2040.BUTTON_C]

button_up = badger2040.BUTTONS[badger2040.BUTTON_UP]
button_down = badger2040.BUTTONS[badger2040.BUTTON_DOWN]

LINE_HEIGHT = 16

# Display Setup
display = badger2040.Badger2040()
display.led(128)

nic = network.WLAN(network.STA_IF)
nic.active(True)


def update_display():
    # Page Header
    display.clear()
    display.set_pen(0)
    display.rectangle(0, 0, badger2040.WIDTH, 20)
    display.set_pen(0)
    display.set_font('bitmap8')
    display.set_pen(0)

    y = 35 + int(LINE_HEIGHT / 2)
    nets = nic.scan()
    # sort by 4th item (RSSI) descending
    nets.sort(key=lambda x: x[3], reverse=True)
    for net in nets:
        ssid, bssid, channel, RSSI, security, hidden = net
        display.text("{} {} {} {}".format(str(RSSI), ssid.decode("utf-8"), Security[security], Visibility[hidden]), 0, y, badger2040.WIDTH, scale=3)
        y += LINE_HEIGHT

    display.update()
    time.sleep(30)


# Call halt in a loop, on battery this switches off power.
# On USB, the app will exit when A+C is pressed because the launcher picks that up.
while True:
    update_display()
    display.keepalive()
    display.halt()
    time.sleep(0.01)
