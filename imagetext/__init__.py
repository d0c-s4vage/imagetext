#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
imagetext is a module that provides two functions: write and read.

The ``write`` function will visually write input data as hex characters
into a PNG image.

The ``read`` function will read visual hex characters from images created
by imagetext and return the raw data.
"""


import binascii
import math
import PIL.Image


import imagetext.chars as chars


CHARS_PER_ROW = 64
"""The number of characters per row. Intended to be
used as reference only.
"""


def write(data, outfile):
    """Write the provided ``data`` into the filepath/stream-like object
    specified by ``outfile``.

    :param str data: The data to write
    :param outfile: A stream-like object OR a file-path string.
    :returns: None
    """
    # times two b/c one byte needs two characters in hex. E.g. FF
    char_rows = int(math.ceil(len(data)*2 / float(CHARS_PER_ROW)))

    width = (chars.CHAR_WIDTH * CHARS_PER_ROW) + (chars.SPACE_WIDTH * (CHARS_PER_ROW))
    height = (chars.CHAR_HEIGHT * char_rows) + (chars.SPACE_WIDTH * (char_rows))

    pixels = []
    for x in xrange(height):
        pixels.append([0] * width)

    _insert_chars_into_pixels(data, pixels)

    image_data = _pixels_to_rgb(pixels)
    img = PIL.Image.frombytes("RGB", (width,height), image_data)
    img.save(outfile, format="PNG")


def read(infile):
    """Extract the data visually contained in the image specified by the ``infile``
    filepath/stream-like object.

    :params infile: A stream-like object OR a file-path string.
    :returns: The data extracted from the image
    """
    img = PIL.Image.open(infile)
    raw_data = img.tobytes()

    pixels = _rgb_to_pixels(raw_data)

    read_data = ""

    num_char_rows = len(pixels) / (chars.CHAR_HEIGHT + chars.SPACE_WIDTH)
    for char_row in xrange(num_char_rows):
        y = char_row * (chars.CHAR_HEIGHT + chars.SPACE_WIDTH)

        for char_x in xrange(CHARS_PER_ROW):
            x = char_x * (chars.CHAR_WIDTH + chars.SPACE_WIDTH)

            read_data += chars.get_char(pixels, x, y)

    return binascii.unhexlify(read_data)


# -------------------------------
## UTILITY FUNCTIONS
# -------------------------------


def _insert_chars_into_pixels(data, pixels):
    hex_data = binascii.hexlify(data)

    rows = []
    while len(hex_data) > 0:
        next_row = hex_data[:CHARS_PER_ROW]
        hex_data = hex_data[CHARS_PER_ROW:]
        rows.append(next_row)

    y = 0
    for row in rows:
        x = 0
        for char in row:
            chars.write_char_to_pixels(char, pixels, x, y)
            x += chars.CHAR_WIDTH + chars.SPACE_WIDTH
        y += chars.CHAR_HEIGHT + chars.SPACE_WIDTH


def _rgb_to_pixels(data):
    pixels = []

    bytes_per_row = (CHARS_PER_ROW * (chars.CHAR_WIDTH + chars.SPACE_WIDTH)) * 3
    rows = []
    while len(data) > 0:
        row = data[:bytes_per_row]
        data = data[bytes_per_row:]
        rows.append(row)

    for row in rows:
        pixel_row = []
        for idx in xrange(0, len(row), 3):
            if row[idx:idx+3] == "\xff\xff\xff":
                pixel_row.append(0)
            else:
                pixel_row.append(1)
        pixels.append(pixel_row)

    return pixels


def _pixels_to_rgb(pixels):
    res = ""
    for row in pixels:
        for pixel in row:
            if pixel == 0:
                res += "\xff\xff\xff"
            else:
                res += "\x00\x00\x00"
    return res
