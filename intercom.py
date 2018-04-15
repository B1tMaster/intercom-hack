#!/usr/bin/python3
import RPi.GPIO as GPIO
import subprocess
import shlex
from time import sleep

def greeting():
    command_line = 'aplay /home/pi/intercom/greeting.wav'
    args = shlex.split(command_line)
    subprocess.call(args)

def answer():
    command_line = 'sudo arecord -D plughw:1 --duration=3 -f cd /home/pi/intercom/answer.wav'
    args = shlex.split(command_line)
    subprocess.call(args)
   
def pulsador():
        if (GPIO.input(16)):
            GPIO.output(11, 1)
            GPIO.output(7, 1)
            sleep(2)
            greeting()
            answer()
            GPIO.output(11, 0)
            GPIO.output(7, 0)
            GPIO.output(13, 1)
            sleep(2)
            GPIO.output(13, 0)
        
        
if __name__ == '__main__':
    try: 
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.IN)
        GPIO.setwarnings(False)
        GPIO.setup(7, GPIO.OUT, initial=0)   
        GPIO.setup(11, GPIO.OUT, initial=0)
        GPIO.setup(13, GPIO.OUT, initial=0)
        while True:
            pulsador()
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit(0)
    except Exception as e:
        print("Error:")
        print(e)            
    finally:
        GPIO.cleanup()
        exit(1)
