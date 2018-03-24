"""Module to remove whitespace from an image, square it, and add a circle"""

# Copyright 2016 Matthew Krohn
#
# This file is part of Circler.
#
# Circler is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from math import floor
import sys

from PIL import Image


def red_circle(token):
    """Honestly, this is pretty much the entire program"""
    image = token
    image.convert("RGBA")

    width, height = image.size

    if width > height:
        square = width

    if height > width:
        square = height

    new = Image.new("RGBA", (square, square), "white")

    left = floor((square-width)/2)
    top = floor((square-height)/2)

    print(left)
    print(top)

    new.paste(image, (left, top))

    datas = new.getdata()

    new_data = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    new.putdata(new_data)

    circle = Image.open("Red - Medium.png")
    circle = circle.resize((square, square))

    circle.paste(new, (0, 0), new)
    return circle

if __name__ == "__main__":
    IMAGE_FILE = Image.open(sys.argv[1])
    CIRCLED_TOKEN = red_circle(IMAGE_FILE)
    CIRCLED_TOKEN.save(sys.argv[2])
