from pyzbar import pyzbar
import cv2
from glob import glob

def decode_barcode(image, cls):
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        print("detected barcode:", obj)
        image = draw_barcode(obj, image, cls)
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image


def draw_barcode(decoded, image, cls):
    image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    image = cv2.putText(image, cls, (int(12), int(12)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color=(0, 0, 0), thickness=1)
    image = cv2.putText(image, decoded.type, (int(12), int(25)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color=(0, 0, 0), thickness=1)
    image = cv2.putText(image, str(decoded.data), (int(12), int(35)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color=(0, 0, 0), thickness=1)
    return image


def decode_bar(file,cls):
    barcodes = glob(file)
    for barcode_file in barcodes:
        img = cv2.imread(barcode_file)
        img = decode_barcode(img,cls)
        cv2.imshow("img", img)
        cv2.waitKey(0)
