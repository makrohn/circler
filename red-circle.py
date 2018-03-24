#!/Users/mkrohn/.virtualenvs/npc_converter/bin/python

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
