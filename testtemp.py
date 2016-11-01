import sys
import time

import TempHumidity

pi_TempHumidity = TempHumidity.piTemp()

celsius = pi_TempHumidity.read_temperature()
humidity = pi_TempHumidity.read_humidity()
fahrenheit = 9.0/5.0 * celsius + 32

while True:
    print ('Temp: {0:0.1f}F Humidity: {1:0.1f}%'.format(fahrenheit, humidity))
    time.sleep(2)
