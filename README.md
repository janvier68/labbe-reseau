# labbe-reseau
Le projet l’abbé réseau a pour objectif le surcyclage d’une ancienne baie de brasse réseau en cave d’affinage pour fromage et saucisson 
Le guide de secours  

# Installation rasbery + composant 
## Installation des librairies minimales et de python 
```Code
sudo apt-get update 

sudo apt-get upgrade 

sudo apt-get install python3-pip 

sudo pip3 install --upgrade setuptools 
```
 
## Installation de Blinka  
Il faudra valider en “O” afin de continuer et valider l’opération 
Il faudra également attendre un petit peu, le téléchargement et l’installation de Blinka étant l’une des plus longues de tout le setup.  
Le terminal va ensuite pour vous demander de reboot, faites-le 
```Code
cd ~ 

sudo pip3 install --upgrade adafruit-python-shell 

wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py 

sudo python3 raspi-blinka.py 
```

 

##Activation des I2C et des SPI 
ls /dev/i2c* /dev/spi* 

Enfin, pour vérifier que tout a été correctement installé on lance le code suivant que l’on nommera “blinkatest.py” 

```Python
import board 

import digitalio 

import busio 

  

print("Hello blinka!") 

  

# Try to great a Digital input 

pin = digitalio.DigitalInOut(board.D4) 

print("Digital IO ok!") 

  

# Try to create an I2C device 

i2c = busio.I2C(board.SCL, board.SDA) 

print("I2C ok!") 

  

# Try to create an SPI device 

spi = busio.SPI(board.SCLK, board.MOSI, board.MISO) 

print("SPI ok!") 

  

print("done!") 
```
 

## Librairie hts221
On installe ensuite les librairies qui sont nécessaires au bon fonctionnement des capteurs d’humidité/température, de qualité d’air ainsi que le multiplexer. 

```Code 
sudo pip3 install adafruit-circuitpython-hts221 
```

Le test final pour le capteur de température/humidité se fera avec ce code :  
```Python
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries 
# SPDX-License-Identifier: MIT 

import time 
import board 
import adafruit_hts221 


i2c = board.I2C()  # uses board.SCL and board.SDA 

# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller 

hts = adafruit_hts221.HTS221(i2c) 


data_rate = adafruit_hts221.Rate.label[hts.data_rate] 

print("Using data rate of: {:.1f} Hz".format(data_rate)) 

print("") 

  

while True: 

    print("Relative Humidity: {:.2f} % rH".format(hts.relative_humidity)) 

    print("Temperature: {:.2f} C".format(hts.temperature)) 

    print("") 

    time.sleep(1) 
```




## Installation de la librairie TCA9548A 
Pour le capteur de qualité d’air, référez-vous à ce site :  
https://wiki.dfrobot.com/SKU_SEN0515_Fermion_ENS160_Air_Quality_Sensor#target_8 

On y trouve les diverses commandes à utiliser ainsi que les informations liées aux indices qu’affiche le capteur 
 
```Code
sudo pip3 install adafruit-circuitpython-tca9548a 
```
 

On exécutera ensuite ce code que l’on nommera humblement main.py : 
```Python
# SPDX-FileCopyrightText: 2021 Carter Nelson for Adafruit Industries 
# SPDX-License-Identifier: MIT 

 
# This example shows using TCA9548A to perform a simple scan for connected devices 
import board 
import adafruit_tca9548a 

  

# Create I2C bus as normal 

i2c = board.I2C()  # uses board.SCL and board.SDA 

# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller 

  

# Create the TCA9548A object and give it the I2C bus 

tca = adafruit_tca9548a.TCA9548A(i2c) 

  

for channel in range(8): 

    if tca[channel].try_lock(): 

        print("Channel {}:".format(channel), end="") 

        addresses = tca[channel].scan() 

        print([hex(address) for address in addresses if address != 0x70]) 

        tca[channel].unlock() 
```

On devra voir ce résultat : 
(ajouter img)

On à terminer pour l'installation.
