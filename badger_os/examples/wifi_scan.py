import badger2040
import network
import time

Security = (
    'open',
    'WEP',
    'WPA-PSK',
    'WPA2-PSK',
    'WPA/WPA2-PSK',
    'WPA2/WPA3-PSK',
    'WPA3-PSK',
    'WPA2-Enterprise',
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

LINE_HEIGHT = 8

# Display Setup
display = badger2040.Badger2040()
display.led(128)

nic = network.WLAN(network.STA_IF)
nic.active(True)


def update_display():
    # Clear to white
    display.set_pen(15)
    display.clear()

    display.set_font("bitmap8")
    display.set_pen(0)

    y = int(LINE_HEIGHT / 2)
    nets = nic.scan()
    # sort by 4th item (RSSI) descending
    nets.sort(key=lambda x: x[3], reverse=True)
    for net in nets:
        ssid, bssid, channel, RSSI, security, hidden = net
        display.text("{} {} {} {} {}".format(str(RSSI), ssid.decode("utf-8"), Security[security], str(security), str(hidden)), 0, y, badger2040.WIDTH, fixed_width=True, scale=0.3)
        y += LINE_HEIGHT

    display.update()
    time.sleep(20)


# Call halt in a loop, on battery this switches off power.
# On USB, the app will exit when A+C is pressed because the launcher picks that up.
while True:
    update_display()
    display.keepalive()
    time.sleep(0.01)
