import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pandas as pd
import pickle


df = pd.read_csv("other/Database.csv")
data_dir = "Data"
cat = ["qrImg","barImg"]

IMG_SIZE = 28
training_data = []
df.reset_index()
def create_training_data():
    for category in cat:
        path = os.path.join(data_dir,category)
        class_num = cat.index(category)
        for img in os.listdir(path):
            try:
                img_arr = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_arr = cv2.resize(img_arr, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_arr, class_num])
            except Exception as e:
                pass

create_training_data()

random.shuffle(training_data)
x = []
y = []

for features, label in training_data:
    x.append(features)
    y.append(label)


x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y = np.array(y)

pickle_out = open("x.pickle","wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()