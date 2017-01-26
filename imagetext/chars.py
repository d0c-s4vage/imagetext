#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Utility functions for working with individual characters
"""

X = 1

CHAR_WIDTH = 3
CHAR_HEIGHT = 5
SPACE_WIDTH = 2

charmap = {
    "0": [
        [X,X,X],
        [X,0,X],
        [X,0,X],
        [X,0,X],
        [X,X,X],
    ],
    "1": [
        [0,X,0],
        [0,X,0],
        [0,X,0],
        [0,X,0],
        [0,X,0],
    ],
    "2": [
        [0,X,X],
        [X,0,X],
        [0,0,X],
        [0,X,0],
        [X,X,X],
    ],
    "3": [
        [0,X,X],
        [X,0,X],
        [0,X,X],
        [0,0,X],
        [X,X,X],
    ],
    "4": [
        [X,0,X],
        [X,0,X],
        [X,X,X],
        [0,0,X],
        [0,0,X],
    ],
    "5": [
        [X,X,X],
        [X,0,0],
        [X,X,X],
        [0,0,X],
        [X,X,X],
    ],
    "6": [
        [X,0,0],
        [X,0,0],
        [X,X,X],
        [X,0,X],
        [X,X,X],
    ],
    "7": [
        [X,X,X],
        [0,0,X],
        [0,0,X],
        [0,X,0],
        [X,0,0],
    ],
    "8": [
        [X,X,X],
        [X,0,X],
        [X,X,X],
        [X,0,X],
        [X,X,X],
    ],
    "9": [
        [X,X,X],
        [X,0,X],
        [X,X,X],
        [0,0,X],
        [0,0,X],
    ],
    "a": [
        [X,X,X],
        [X,0,X],
        [X,X,X],
        [X,0,X],
        [X,0,X],
    ],
    "b": [
        [X,X,X],
        [X,0,X],
        [X,X,0],
        [X,0,X],
        [X,X,X],
    ],
    "c": [
        [X,X,X],
        [X,0,0],
        [X,0,0],
        [X,0,0],
        [X,X,X],
    ],
    "d": [
        [X,X,0],
        [X,0,X],
        [X,0,X],
        [X,0,X],
        [X,X,0],
    ],
    "e": [
        [X,X,X],
        [X,0,0],
        [X,X,0],
        [X,0,0],
        [X,X,X],
    ],
    "f": [
        [X,X,X],
        [X,0,0],
        [X,X,0],
        [X,0,0],
        [X,0,0],
    ],
}


def get_char(pixels, x, y):
    """Attempt to identify the character visually represented by
    the char at coords ``x``, ``y`` in the provided 2d pixel array
    (where ``1`` is a pixel present and ``0`` is a pixel absent).

    :param list pixels: A nested 3x5 list of ones and zeroes
    :returns: The character visually represented by the pixels, else ""
    """
    char_pixels = []
    for y_off in xrange(CHAR_HEIGHT):
        char_pixels.append(pixels[y+y_off][x:x+CHAR_WIDTH])

    for k,v in charmap.iteritems():
        if v == char_pixels:
            return k

    return ""


def get_bitmap(char):
    """Return the simple bitmap of the provided char

    :param str char: The bitmap char to return. char should be one of ``0-9A-F``
    :returns: Bitmap list if a bitmap is defined for char, else ``None``
    """
    return charmap.get(char, None)


def write_char_to_pixels(char, pixels, x, y):
    """Write the provided ``char`` into the 2d pixels array
    at location ``x`` and ``y``

    :param str char: A one-byte string
    :param list pixels: A 2-d array of ones and zeroes ("pixels")
    :param int x: The x coord to begin writing the bitmap into
    :param int y: The y coord to begin writing the bitmap into
    """
    if len(char) != 1:
        raise Exception("Char must be a 1-byte string, not {} bytes".format(
            len(char)
        ))

    bitmap = get_bitmap(char)
    if bitmap is None:
        raise Exception("No bitmap defined for character {!r}".format(char))

    y_off = 0
    for row in bitmap:
        x_off = 0
        for pixel in row:
            pixels[y + y_off][x + x_off] = pixel
            x_off += 1

        y_off += 1
