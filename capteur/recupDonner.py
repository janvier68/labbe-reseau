import board
import time

#!multi
import adafruit_tca9548a

#?CO2
import adafruit_ens160

#*temperateur
import adafruit_hts221

#?activation  GPIO
import RPi.GPIO as GPIO
    #  config
GPIO.setmode(GPIO.BCM)
    # ventilateur
broche_ventilateur=26
onoff_ventilateur=0
GPIO.setup(broche_ventilateur, GPIO.OUT)
    # brumisateur 
broche_brumisateur = 25
onoff_brumisateur=0
GPIO.setup(broche_brumisateur , GPIO.OUT)

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
tabSensor=[]
tabSensor.append(adafruit_hts221.HTS221(tca[1]))
tabSensor.append(adafruit_hts221.HTS221(tca[2]))
tabSensor.append(adafruit_hts221.HTS221(tca[3]))
tabSensor.append(adafruit_hts221.HTS221(tca[4]))

for i in range(len(tabSensor)):
    data_rate = adafruit_hts221.Rate.label[tabSensor[i].data_rate]
    print("Using data rate of: {:.1f} Hz".format(data_rate))

#init temps 
# Obtenir la date et l'heure actuelles
date_heure_actuelles = time.localtime()
format_date_heure = "%Y-%m-%d;%H:%M:%S"

temps_att_seconde_donner=10
att=0

#! condition valeur
def F_onoff_ventilateur():
    global onoff_ventilateur
    if onoff_ventilateur:
        GPIO.output(broche_ventilateur, GPIO.HIGH)
        onoff_ventilateur=0
    else:
        GPIO.output(broche_ventilateur, GPIO.LOW)
        onoff_ventilateur=1

def F_onoff_brumisateur():
    global onoff_brumisateur
    if onoff_brumisateur:
        GPIO.output(broche_brumisateur, GPIO.HIGH)
        onoff_brumisateur=0
    else:
        GPIO.output(broche_brumisateur, GPIO.LOW)
        onoff_brumisateur=1
    

while True:
    att+=10

    # ! condition action 
     

    # récupération des donner tout les x temps 
    if att==temps_att_seconde_donner:
        #*temperateur
        date_heure_actuelles = time.localtime()
        for i in range(4):
            ficher=open("Data/C_temperatureAndHumiditer_%u.txt"%(i),"+a")
            # time;température;humidity
            ficher.write("%s;%u;%u\n"%(time.strftime(format_date_heure, date_heure_actuelles),tabSensor[i].temperature,tabSensor[i].relative_humidity))
            ficher.close()
        
        #?CO2
        ficher=open("Data/C_co2.txt","+a")
        #AQI (1-5);TVOC (ppb);eCO2 (ppm
        ficher.write("%s;%u;%u;%u\n"%(time.strftime(format_date_heure, date_heure_actuelles),ensC0DE.AQI,ensC0DE.TVOC,ensC0DE.eCO2))
        ficher.close()
        #reset conteur
        att=0

    #att
    time.sleep(10)
