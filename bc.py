#!/usr/bin/env python3
import sys
import time
import unicornhat as uh
from message import send_message
from forecast import get_week_weather_status


WIDTH=8
HEIGHT=4
L=(255,255,255)
R=(0,0,255)
B=(0,0,0)


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
        t = time.strftime("%H%M%S")
        split_time = map(lambda x:list(bin(int(x))[2:]), t)
        
        for cidx, c in enumerate(split_time):
            set_column(cidx+1, c, colors[cidx])
        
        uh.show()
        time.sleep(1)

  
if __name__=='__main__':
    try:
        colors = get_colors()
    except Exception as e:
        print(f"Error in forecast.py:\n{e}")
        send_message('Unable to get colors.')
        colors = [L]*6
    try:
        run(colors)
    except KeyboardInterrupt:
        send_message('Bye')
        sys.exit()

