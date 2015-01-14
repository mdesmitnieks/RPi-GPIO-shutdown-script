from subprocess import call
import RPi.GPIO as gpio


def loop():
    while(1):
        pass


def shutdown(pin):
    call('halt', shell=False)

#Set pin numbering to board numbering
gpio.setmode(gpio.BOARD)

gpio.setup(7, gpio.IN) 

gpio.add_event_detect(7, gpio.FALLING, callback=shutdown, bouncetime=60000) 

loop() 
