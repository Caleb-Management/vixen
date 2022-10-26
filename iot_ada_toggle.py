import pyfirmata
#importing library to communicate and translate Python code to Arduino Uno hardware
import time
#importing library to create delays
from Adafruit_IO import Client, Feed, RequestError
#importing certain modules from Adafruit library

ADAFRUIT_IO_USERNAME = "Krissmetic"
ADAFRUIT_IO_KEY = "aio_NiqU05m6k9GNvtLA41MBqAqfMVoe"
#connecting my username and key from my IoT dashboard

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
#creating a cliemt to communicate to my Adafruit account

board = pyfirmata.Arduino('COM5')
it = pyfirmata.util.Iterator(board)
it.start()
#initializing Arduino microcontroller by using the pyfirmata module

led = board.get_pin('d:11:o')
#defining pin numbers for LED

try:
    digital = aio.feeds('toggle')
    #telling the program to look for a feed called 'toggle'
except RequestError:
    feed = Feed(name='toggle')
    toggle = aio.create_feed
    #if unable to find the specified feed
    #a new feed must be created

while True:
    data = aio.receive(digital.key)
    print(data.value)
    #printing the currently toggled state, either ON or OFF
    if data.value == "ON":
        led.write(True)
        #if the push button is pressed, LED will be turned on
    else:
        led.write(False)
        #as long as the push button is not active, LED will be turned off
    time.sleep(1)