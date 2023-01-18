from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
import glob, os

class Definity():
    def join():

        path = "example.jpg"
        PIL_image = Image.open(path)

        shape = [(40, 60), (130, 120)]
        img1 = ImageDraw.Draw(PIL_image)
        img1.rectangle(shape, fill="#800080", outline="green")

        font = ImageFont.truetype("Rasfferd.otf", 50)

        string = "C {NUMB}"
        string = string.replace("{NUMB}",str(datetime.today().day))

        # draw.text((x, y),"Sample Text",(r,g,b))
        img1.text([50,60], string, (255, 255, 255), font=font)


        PIL_image = PIL_image.save("one_day\\"+str(datetime.today().day)+".jpg")

Definity.join()