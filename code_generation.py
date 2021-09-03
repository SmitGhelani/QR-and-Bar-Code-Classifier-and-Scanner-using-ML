from barcode.writer import ImageWriter
from barcode import EAN13
from os import name
import pandas as pd
import barcode
import random
import string
import qrcode


def random_string(letter_count, digit_count):
    str1 = ''.join((random.choice(string.ascii_letters) for x in range(letter_count)))
    str1 += ''.join((random.choice(string.digits) for x in range(digit_count)))
    sam_list = list(str1)
    random.shuffle(sam_list)
    final_string = ''.join(sam_list)
    return final_string


def random_number():
    str1 =[]
    while len(str1) != 12:
        for i in range(1, 13):
            str1.append(str(random.randint(0, 9)))
    
    random.shuffle(str1)
    final_num = ''.join(str1)
    return final_num


def create_bar():
    img_arr = []
    text_arr = []
    type_arr = []
    for i in range(500):
        text = random_number()
        file = "Data/barImg/bar_img_"+str(i)
        ean = barcode.get('ean13', text, writer=ImageWriter())
        filename = ean.save(file)
        img_arr.append(file)
        text_arr.append(text)
        type_arr.append("Barcode")

    return img_arr, text_arr, type_arr


def create_qrcode():
    img_arr = []
    str_arr = []
    type_arr = []
    for count in range(500):
        i, j = random.randint(0,10), random.randint(0,10)
        rndm_str = random_string(i,j)
        img = qrcode.make(rndm_str)
        img_name = "Data/qrImg/qr_img_"+str(count)+".png"
        img_arr.append(img_name)
        str_arr.append(rndm_str)
        type_arr.append("QRcode")
        img.save(img_name)
    
    return img_arr, str_arr, type_arr


img_arr, text_arr, type_arr = create_bar()
df = pd.DataFrame()

img_arr1, text_arr1, type_arr1 = create_qrcode()
img_arr.append(img_arr1)
text_arr.append(text_arr1)
type_arr.append(type_arr1)

df["IMG Name"] = pd.DataFrame(img_arr)
df["Text"] = pd.DataFrame(text_arr)
df["Type"] = pd.DataFrame(type_arr)

db_name = "other/Database.csv"
df.to_csv(db_name)