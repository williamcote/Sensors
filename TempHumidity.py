try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

import Adafruit_DHT

import paho.mqtt.subscribe as subscribe

DHT_TYPE = Adafruit_DHT.AM2302
DHT_PIN  = 21

class piTemp(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DHT_PIN, GPIO.IN)

    def read_temperature(self):
        """Read the temperature from the DHT sensor and return
        """
        self._humidity, self._celsius = Adafruit_DHT.read_retry(DHT_TYPE, DHT_PIN)

        if self._humidity is not None and self._celsius is not None:
            return self._celsius
        else:
            return 0

    def read_humidity(self):
        """Read the humidity from the DHT sensor and return
        """
        if self._humidity is not None and self._celsius is not None:
            return self._humidity
        else:
            return 0

    def read_temperature1(self):
        """Read the temperature from the MQTT server and return
        """
        self._sensor = subscribe.simple("Sensors/Room1/Temperature", hostname="192.168.145.127")
        return self._sensor.payload

    def read_humidity1(self):
        """Read the humidity from the MQTT server and return
        """
        self._sensor = subscribe.simple("Sensors/Room1/Humidity", hostname="192.168.145.127")
        return self._sensor.payload


    def read_temperature2(self):
        """Read the temperature from the MQTT server and return
        """
        self._sensor = subscribe.simple("Sensors/Room2/Temperature", hostname="192.168.145.127")
        return self._sensor.payload


    def read_humidity2(self):
        """Read the humidity from the MQTT server and return
        """
        self._sensor = subscribe.simple("Sensors/Room2/Humidity", hostname="192.168.145.127")
        return self._sensor.payload
