"""
! il faut importer les libréri suivant pour installer sur arduino (pas oublier de crée python)
sudo apt install rpi.gpio
#python + librery
sudo apt install python3
python3 get-pip.py
#BLINKA
sudo pip3 install adafruit-circuitpython-ens160
sudo pip3 install adafruit-circuitpython-adafruit_hts221.HTS221
sudo pip3 install adafruit-circuitpython-tca9548a 
sudo pip3 install RPi.GPIO
#activer i2c 
https://www.raspberryme.com/activer-linterface-i2c-sur-le-raspberry-pi/
"""


import board
import time

#!multi
import adafruit_tca9548a

#?CO2
import adafruit_ens160

#*temperateur
import adafruit_hts221


# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA


#!Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)
#différance les diff I2C

#?CO2
ensC0DE = adafruit_ens160.ENS160(tca[0])
# Set the temperature compensation variable to the ambient temp
# for best sensor calibration
ensC0DE.temperature_compensation = 25
# Same for ambient relative humidity
ensC0DE.humidity_compensation = 50


#*temperateur
sensor1 = adafruit_hts221.HTS221(tca[1])
sensor2 = adafruit_hts221.HTS221(tca[2])
sensor3 = adafruit_hts221.HTS221(tca[3])
sensor4 = adafruit_hts221.HTS221(tca[4])

#pour température mais jsp si sa marche 
data_rate = adafruit_hts221.Rate.label[sensor1.data_rate]
print("Using data rate of: {:.1f} Hz".format(data_rate))
data_rate = adafruit_hts221.Rate.label[sensor2.data_rate]
print("Using data rate of: {:.1f} Hz".format(data_rate))
data_rate = adafruit_hts221.Rate.label[sensor3.data_rate]
print("Using data rate of: {:.1f} Hz".format(data_rate))
data_rate = adafruit_hts221.Rate.label[sensor4.data_rate]
print("Using data rate of: {:.1f} Hz".format(data_rate))


while True:
    
    #*temperateur
    print("\nCapteur temperateur && humiditer")

    print("Relative Humidity: {:.2f} % rH".format(sensor1.relative_humidity))
    print("Temperature: {:.2f} C".format(sensor1.temperature))
    print("")
    print("Relative Humidity: {:.2f} % rH".format(sensor2.relative_humidity))
    print("Temperature: {:.2f} C".format(sensor2.temperature))
    print("")
    print("Relative Humidity: {:.2f} % rH".format(sensor3.relative_humidity))
    print("Temperature: {:.2f} C".format(sensor3.temperature))
    print("")
    print("Relative Humidity: {:.2f} % rH".format(sensor4.relative_humidity))
    print("Temperature: {:.2f} C".format(sensor4.temperature))
    print("")
    
    #?CO2
    print("\nCapteur C02")
    print("AQI (1-5):", ensC0DE.AQI)
    print("TVOC (ppb):", ensC0DE.TVOC)
    print("eCO2 (ppm):", ensC0DE.eCO2)

    # att 2 seconde
    time.sleep(2)
