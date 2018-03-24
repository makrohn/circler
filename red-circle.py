#Copyright 2016 Matthew Krohn
#
#This file is part of Circler.
#
#Circler is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from PIL import Image
from math import floor
import sys

def red_circle(token):

    image = token
    image.convert("RGBA")

    width,height = image.size

    if width > height:
        square = width

    if height > width:
        square = height

    new = Image.new("RGBA",(square,square),"white")

    left=floor((square-width)/2)
    top=floor((square-height)/2)

    print(left)
    print(top)

    new.paste(image,(left,top))

    datas = new.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    new.putdata(newData)

    circle = Image.open("Red - Medium.png")
    circle = circle.resize((square,square))

    circle.paste(new,(0,0), new)
    return circle

if __name__=="__main__":
    image_file = Image.open(sys.argv[1])
    circled_token = red_circle(image_file)
    circled_token.save(sys.argv[2])
