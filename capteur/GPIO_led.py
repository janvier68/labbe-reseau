import RPi.GPIO as GPIO
import time

# Définir le numéro de la broche de la LED
broche_led = 18
broche_led2 = 15

# Configuration de la broche GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(broche_led, GPIO.OUT)
GPIO.setup(broche_led2, GPIO.OUT)

# Fonction pour allumer la LED
def allumer_led():
    GPIO.output(broche_led, GPIO.HIGH)
    GPIO.output(broche_led2, GPIO.HIGH)

# Fonction pour éteindre la LED
def eteindre_led():
    GPIO.output(broche_led, GPIO.LOW)
    GPIO.output(broche_led2, GPIO.LOW)

# Clignotement de la LED
while True:
    allumer_led()  # Allumer la LED
    time.sleep(1)  # Attendre 1 seconde
    eteindre_led()  # Éteindre la LED
    time.sleep(1)  # Attendre 1 seconde

# faut faire comment pour les brumi