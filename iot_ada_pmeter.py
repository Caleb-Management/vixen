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
#initializing communication with Arduino

p_meter = board.get_pin('a:0:i')
#defining pin number and function for potentiometer


try:
    digital = aio.feeds('p-meter')
    #telling the program to check for a feed named 'p-meter' on the dashboard
except RequestError:
    feed = Feed(name='p-meter')
    p_meter = aio.create_feed(feed)
    #if unable to find the specified feed (there has been an error in the request)
    #a new feed must be created


while True:
    analog_value = p_meter.read()
    #declaring that the analog input from potentiometer is the value
    if analog_value is not None:
        aio.send_data('p-meter', analog_value)
        #sending value data to Adafruit dashboard
    time.sleep(1)

    print(digital)

    data = aio.receive(digital.key)
    print(data.value)