try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280
from bmp280 import BMP280
import time, logging, pytz, serial, Adafruit_DHT
from datetime import datetime



DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


class sensors:

    def __init__(self):
        self.bus = SMBus(1)
        self.sensor = BMP280(i2c_dev=self.bus)
        self.logger = logging.getLogger("growlab")

    def get_readings(self):

        # DHT22
        humidityDHT22, temperatureDHT22 = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        tz_Paris = pytz.timezone('Europe/Paris')
        datetime_Paris = datetime.now(tz_Paris)
        time_tz_Paris = datetime_Paris.strftime("%Y-%m-%d %H:%M:%S")

        # Analogic sensor from arduino

        # Ouverture du port serie avec :
        # '/dev/ttyXXXX' : definition du port d ecoute (remplacer 'X' par le bon nom)
        # 9600 : vitesse de communication
        serialArduino = serial.Serial('/dev/ttyUSB0', 9600)
        serialOutput = serialArduino.readline()
        serialOutput = str(serialOutput, 'ascii')
        self.logger.info("Data from nano: {}".format(serialOutput))
        serialOutput = serialOutput.replace(' ', '')
        serialOutput = serialOutput.replace('\r\n', '')
        serialOutputArray = serialOutput.split("-")
        soilHumidityNano = serialOutputArray[0].replace('hum:', '')
        luxNano = serialOutputArray[1].replace('lux:', '')
        soilHumiditypercentNano = serialOutputArray[2].replace('humpercent:', '')

        # # BMP280
        # Ignore first result since it seems stale
        temperatureBMP280 = self.sensor.get_temperature()
        pressure = self.sensor.get_pressure()
        time.sleep(0.1)

        temperatureBMP280 = self.sensor.get_temperature()
        pressureBMP280 = self.sensor.get_pressure()
 
        return {
            "temperatureDHT22": temperatureDHT22,
            "humidityDHT22": humidityDHT22,
            "temperatureBMP280": temperatureBMP280,
            "pressureBMP280": pressureBMP280,
            "brightnessNano": luxNano,
            "soilHumidityNano": soilHumidityNano,
            "soilHumidityPerCentNano": soilHumiditypercentNano,
            "time_tz_Paris": time_tz_Paris
        }



