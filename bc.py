#!/usr/bin/env python
# Synergy.203.280.2095

from time import sleep
import unicornhat as uh
from message import send_message


WIDTH,HEIGHT=uh.get_shape()

  
if __name__=='__main__':
    send_message('The quick, brown fox - jumped. over! the lazy dog?'.upper())

