#!/usr/bin/env python3
import sys
from time import sleep
import unicornhat as uh


WIDTH=8
HEIGHT=4
L=(255,100,255) # RGB values for lit character pixels
H=(0,0,0)       # RGB values character highlights
B=(0,0,0)       # RGB values for unlit (blank) pixels
CHAR_SPACING=2
CHARS={
    '0': ([
        [L,L,L],
        [L,H,L],
        [L,H,L],
        [L,L,L]
    ]), '1': ([
        [L,L,H],
        [H,L,H],
        [H,L,H],
        [L,L,L]
    ]), '2': ([
        [L,L,H],
        [H,H,L],
        [H,L,H],
        [L,L,L]
    ]), '3': ([
        [L,L,L],
        [H,L,L],
        [H,H,L],
        [L,L,L]
    ]), '4': ([
        [L,H,L],
        [L,L,L],
        [H,H,L],
        [H,H,L]
    ]), '5': ([
        [L,L,L],
        [L,H,H],
        [H,H,L],
        [L,L,L]
    ]), '6': ([
        [L,H,H],
        [L,L,L],
        [L,H,L],
        [L,L,L]
    ]), '7': ([
        [L,L,L],
        [H,H,L],
        [H,L,H],
        [H,L,H]
    ]), '8': ([
        [L,L,L],
        [L,H,L],
        [L,L,L],
        [L,L,L]
    ]), '9': ([
        [L,L,L],
        [L,H,L],
        [L,L,L],
        [H,H,L]
    ]), 'A': ([
        [H,L,H],
        [L,H,L],
        [L,L,L],
        [L,H,L]
    ]), 'B': ([
        [L,H,H],
        [L,L,L],
        [L,H,L],
        [L,L,L]
    ]), 'C': ([
        [H,L,L],
        [L,H,H],
        [L,H,H],
        [H,L,L]
    ]), 'D': ([
        [L,L,H],
        [L,H,L],
        [L,H,L],
        [L,L,H]
    ]), 'E': ([
        [L,L,L],
        [L,L,H],
        [L,H,H],
        [L,L,L]
    ]), 'F': ([
        [L,L,L],
        [L,L,H],
        [L,H,H],
        [L,H,H]
    ]), 'G': ([
        [H,L,L],
        [L,H,H],
        [L,H,L],
        [H,L,L]
    ]), 'H': ([
        [L,H,L],
        [L,L,L],
        [L,H,L],
        [L,H,L]
    ]), 'I': ([
        [L,L,L],
        [H,L,H],
        [H,L,H],
        [L,L,L]
    ]), 'J': ([
        [L,L,L],
        [H,L,H],
        [H,L,H],
        [L,H,H]
    ]), 'K': ([
        [L,H,L],
        [L,L,H],
        [L,H,L],
        [L,H,L]
    ]), 'L': ([
        [L,H,H],
        [L,H,H],
        [L,H,H],
        [L,L,L]
    ]), 'M': ([
        [L,L,L],
        [L,L,L],
        [L,H,L],
        [L,H,L]
    ]), 'N': ([
        [L,L,H],
        [L,H,L],
        [L,H,L],
        [L,H,L]
    ]), 'O': ([
        [H,L,H],
        [L,H,L],
        [L,H,L],
        [H,L,H]
    ]), 'P': ([
        [L,L,L],
        [L,H,L],
        [L,L,L],
        [L,H,H]
    ]), 'Q': ([
        [L,L,L],
        [L,H,L],
        [L,L,L],
        [H,H,L]
    ]), 'R': ([
        [L,L,L],
        [L,H,L],
        [L,L,H],
        [L,H,L]
    ]), 'S': ([
        [L,L,L],
        [L,L,H],
        [H,H,L],
        [L,L,L]
    ]), 'T': ([
        [L,L,L],
        [H,L,H],
        [H,L,H],
        [H,L,H]
    ]), 'U': ([
        [L,H,L],
        [L,H,L],
        [L,H,L],
        [L,L,L]
    ]), 'V': ([
        [L,H,L],
        [L,H,L],
        [L,H,L],
        [H,L,H]
    ]), 'W': ([
        [L,H,L],
        [L,H,L],
        [L,L,L],
        [L,L,L]
    ]), 'X': ([
        [L,H,L],
        [H,L,H],
        [L,H,L],
        [L,H,L]
    ]), 'Y': ([
        [L,H,L],
        [H,L,H],
        [H,L,H],
        [H,L,H]
    ]), 'Z': ([
        [L,L,L],
        [H,L,L],
        [L,H,H],
        [L,L,L]
    ]), '!': ([
        [L,H,H],
        [L,H,H],
        [H,H,H],
        [L,H,H]
    ]), '?': ([
        [L,L,L],
        [H,L,L],
        [H,H,H],
        [H,L,H]
    ]), '.': ([
        [H,H,H],
        [H,H,H],
        [H,H,H],
        [L,H,H]
    ]), ',': ([
        [H,H,H],
        [H,H,H],
        [H,L,H],
        [L,H,H]
    ]), '-': ([
        [B,B,B],
        [L,L,L],
        [B,B,B],
        [B,B,B]
    ]), '/': ([
        [B,B,L],
        [B,L,B],
        [B,L,B],
        [L,B,B]
    ]), ':': ([
        [B,B,B],
        [B,L,B],
        [B,B,B],
        [B,L,B]
    ]), '"': ([
        [L,B,L],
        [L,B,L],
        [B,B,B],
        [B,B,B]
    ]), '{': ([
        [B,B,L],
        [B,L,B],
        [B,L,B],
        [B,B,L]
    ]), '(': ([
        [B,B,L],
        [B,L,B],
        [B,L,B],
        [B,B,L]
    ]), '}': ([
        [L,B,B],
        [B,L,B],
        [B,L,B],
        [L,B,B]
    ]), ')': ([
        [L,B,B],
        [B,L,B],
        [B,L,B],
        [L,B,B]
    ]), ' ': ([
        [B,B],
        [B,B],
        [B,B],
        [B,B]
    ]), '#': ([     # The default character, used if a letter isn't in CHARS
        [L,L,L],
        [L,L,L],
        [L,L,L],
        [L,L,L]
    ]),
}


def str_to_pixels(string):
    """Return a mutlidimensional list of RGB values representing the message"""
    pixels = [[] for r in range(HEIGHT)]

    for ridx in range(HEIGHT):
        pixels[ridx].extend([B]*WIDTH)
    for char in string:
        for ridx, row in enumerate(CHARS['#'] if char not in CHARS else CHARS[char]):
            pixels[ridx].extend(row)
            pixels[ridx].extend([B]*CHAR_SPACING)
    for ridx in range(HEIGHT):
        pixels[ridx].extend([B]*WIDTH)

    return pixels


def send_message(string):
    """Roll the string param representation across the pHAT"""
    uh.set_layout(uh.AUTO)
    uh.rotation(r=180)
    uh.brightness(b=0.2)

    pixels = str_to_pixels(string.upper())
    for c in range(len(pixels[0]) - WIDTH):
        uh.set_pixels([r[c:c+WIDTH] for r in pixels])
        uh.show()
        sleep(0.1)

    uh.clear()
    uh.show()


if __name__=='__main__':
    message = ' '.join(sys.argv[1:])
    send_message(message)

