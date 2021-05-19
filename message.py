#!/usr/bin/env python

from time import sleep
import unicornhat as uh


L=(255,100,255) # RGB values for a lit pixel
O=(0,0,0)       # RGB values for an off pixel in a char
B=(0,0,0)       # RGB values for unlit pixels
WIDTH,HEIGHT=uh.get_shape()
CHAR_SPACING=2

CHARS={
    '0': ([
        [L,L,L],
        [L,O,L],
        [L,O,L],
        [L,L,L]
    ]),
    '1': ([
        [L,L,O],
        [O,L,O],
        [O,L,O],
        [L,L,L]
    ]),
    '2': ([
        [L,L,O],
        [O,O,L],
        [O,L,O],
        [L,L,L]
    ]),
    '3': ([
        [L,L,L],
        [O,O,L],
        [O,L,O],
        [L,L,O]
    ]),
    '4': ([
        [L,O,L],
        [L,L,L],
        [O,O,L],
        [O,O,L]
    ]),
    '5': ([
        [L,L,L],
        [L,O,O],
        [O,O,L],
        [L,L,L]
    ]),
    '6': ([
        [L,O,O],
        [L,L,L],
        [L,O,L],
        [L,L,L]
    ]),
    '7': ([
        [L,L,L],
        [O,O,L],
        [O,L,O],
        [O,L,O]
    ]),
    '8': ([
        [L,L,L],
        [L,O,L],
        [L,L,L],
        [L,L,L]
    ]),
    '9': ([
        [L,L,L],
        [L,O,L],
        [L,L,L],
        [O,O,L]
    ]),
    'A': ([
        [O,L,O],
        [L,O,L],
        [L,L,L],
        [L,O,L]
    ]),
    'B': ([
        [L,O,O],
        [L,L,L],
        [L,O,L],
        [L,L,L]
    ]),
    'C': ([
        [O,L,L],
        [L,O,O],
        [L,O,O],
        [O,L,L]
    ]),
    'D': ([
        [L,L,O],
        [L,O,L],
        [L,O,L],
        [L,L,O]
    ]),
    'E': ([
        [L,L,L],
        [L,L,O],
        [L,O,O],
        [L,L,L]
    ]),
    'F': ([
        [L,L,L],
        [L,L,O],
        [L,O,O],
        [L,O,O]
    ]),
    'G': ([
        [O,L,L],
        [L,O,O],
        [L,O,L],
        [O,L,L]
    ]),
    'H': ([
        [L,O,L],
        [L,L,L],
        [L,O,L],
        [L,O,L]
    ]),
    'I': ([
        [L,L,L],
        [O,L,O],
        [O,L,O],
        [L,L,L]
    ]),
    'J': ([
        [L,L,L],
        [O,L,O],
        [O,L,O],
        [L,O,O]
    ]),
    'K': ([
        [L,O,L],
        [L,L,O],
        [L,O,L],
        [L,O,L]
    ]),
    'L': ([
        [L,O,O],
        [L,O,O],
        [L,O,O],
        [L,L,L]
    ]),
    'M': ([
        [L,L,L],
        [L,L,L],
        [L,O,L],
        [L,O,L]
    ]),
    'N': ([
        [L,L,O],
        [L,O,L],
        [L,O,L],
        [L,O,L]
    ]),
    'O': ([
        [O,L,O],
        [L,O,L],
        [L,O,L],
        [O,L,O]
    ]),
    'P': ([
        [L,L,L],
        [L,O,L],
        [L,L,L],
        [L,O,O]
    ]),
    'Q': ([
        [L,L,L],
        [L,O,L],
        [L,L,L],
        [O,O,L]
    ]),
    'R': ([
        [L,L,L],
        [L,O,L],
        [L,L,O],
        [L,O,L]
    ]),
    'S': ([
        [L,L,L],
        [L,L,O],
        [O,O,L],
        [L,L,L]
    ]),
    'T': ([
        [L,L,L],
        [O,L,O],
        [O,L,O],
        [O,L,O]
    ]),
    'U': ([
        [L,O,L],
        [L,O,L],
        [L,O,L],
        [L,L,L]
    ]),
    'V': ([
        [L,O,L],
        [L,O,L],
        [L,O,L],
        [O,L,O]
    ]),
    'W': ([
        [L,O,L],
        [L,O,L],
        [L,L,L],
        [L,L,L]
    ]),
    'X': ([
        [L,O,L],
        [O,L,L],
        [L,O,L],
        [L,O,L]
    ]),
    'Y': ([
        [L,O,L],
        [O,L,O],
        [O,L,O],
        [O,L,O]
    ]),
    'Z': ([
        [L,L,L],
        [O,L,L],
        [L,O,O],
        [L,L,L]
    ]),
    '!': ([
        [L,O,O],
        [L,O,O],
        [O,O,O],
        [L,O,O]
    ]),
    '?': ([
        [L,L,L],
        [O,L,L],
        [O,O,O],
        [O,L,O]
    ]),
    '.': ([
        [O,O,O],
        [O,O,O],
        [O,O,O],
        [L,O,O]
    ]),
    ',': ([
        [O,O,O],
        [O,O,O],
        [O,L,O],
        [L,O,O]
    ]),
    '-': ([
        [B,B,B],
        [L,L,L],
        [B,B,B],
        [B,B,B]
    ]),
    ' ': ([
        [B,B],
        [B,B],
        [B,B],
        [B,B]
    ]),
}


def str_to_pixels(string):
    pixels = [[] for r in range(HEIGHT)]

    for ridx in range(HEIGHT):
        pixels[ridx].extend([B]*WIDTH)
    for char in string:
        for ridx, row in enumerate(CHARS[char]):
            pixels[ridx].extend(row)
            pixels[ridx].extend([B]*CHAR_SPACING)
    for ridx in range(HEIGHT):
        pixels[ridx].extend([B]*WIDTH)

    return pixels


def send_message(string):
    uh.set_layout(uh.AUTO)
    uh.rotation(r=180)
    uh.brightness(b=0.2)

    pixels = str_to_pixels(string)
    pixels_width = len(pixels[0])
    for c in range(len(pixels[0]) - WIDTH):
        uh.set_pixels([r[c:c+WIDTH] for r in pixels])
        uh.show()
        sleep(0.1)

    uh.clear()
    uh.show()


