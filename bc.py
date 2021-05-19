#!/usr/bin/env python3

import time
import unicornhat as uh
from message import send_message


WIDTH,HEIGHT=uh.get_shape()
HEIGHT=4
L=(255,255,255)
R=(0,0,255)
B=(0,0,0)


def get_colors():   # TODO: get colors
    pass


def set_column(column_idx, values, color):
    column = [(0,0,0)]*(HEIGHT - len(values))
    column.extend([color if v=='1' else B for v in values])

    for ridx, pixel in enumerate(column):
        uh.set_pixel(column_idx, ridx, pixel)


def run(colors):
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
    #colors = get_colors()
    colors = [L,L,R,L,R,L]
    run(colors)

