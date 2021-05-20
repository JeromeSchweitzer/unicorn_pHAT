#!/usr/bin/env python3
import sys
import os
import subprocess
import time
import unicornhat as uh
import RPi.GPIO as GPIO
from message import send_message
from forecast import get_week_weather_status


WIDTH=8         # Width and height must be hardcoded, uh.get_shape() returns incorrect values
HEIGHT=4
L=(255,255,255) # Normal lit color
R=(0,0,255)     # Rain color
B=(0,0,0)       # 'Blank' color
E=(255,74,33)   # Error color
IP_PIN=15


def get_colors():
    """Return list of RGB values representing days of the week that have rain"""
    week_weather_status = get_week_weather_status()
    colors = [R if s=='Rain' else L for s in week_weather_status[:6]]

    return colors


def set_column(column_idx, values, color):
    """Set a specific column in the pHAT according to values and color"""
    column = [(0,0,0)]*(HEIGHT - len(values))
    column.extend([color if v=='1' else B for v in values])

    for ridx, pixel in enumerate(column):
        uh.set_pixel(column_idx, ridx, pixel)


def run(colors):
    """Continually update the pHAT to display the current time in six BCDs"""
    uh.set_layout(uh.AUTO)
    uh.rotation(r=180)
    uh.brightness(b=0.2)
    
    while True:
        if GPIO.input(IP_PIN) == GPIO.HIGH:
            send_message(str(subprocess.check_output('hostname -I', shell=True))[2:-4])
        if colors[0] != E and os.system('who | grep -i pts') == 0:
            colors = [E] * 6
        if colors[0] == E and os.system('who | grep -i pts') != 0:
            colors = get_colors()
        t = time.strftime("%H%M%S")
        split_time = map(lambda x:list(bin(int(x))[2:]), t)
        
        for cidx, c in enumerate(split_time):
            set_column(cidx+1, c, colors[cidx])
        
        uh.show()
        time.sleep(1)

  
if __name__=='__main__':
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    try:
        colors = get_colors()
    except Exception as e:
        print(f"Error in forecast.py:\n{e}")
        send_message(str(e))    # Very useful for debugging without internet
        colors = [L]*6
    try:
        run(colors)
    except Exception as e:
        print(f"Error in run():\n{e}")
        #send_message('bye')
        sys.exit()

