import cv2
import os
import numpy as np
from numpy.core.fromnumeric import reshape
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle
import training_data
import scanner


x = pickle.load(open("x.pickle", "rb")) 
y = pickle.load(open("y.pickle", "rb"))

x = x/255.0

model = Sequential()
model.add(Conv2D(64 , (3,3), input_shape = x.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64 , (3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

model.fit(x,y,batch_size=32, epochs=3, validation_split=0.2)


dir_path = "other/test"

for i in os.listdir(dir_path):
    img_path = dir_path +"//"+i
    img = image.load_img(img_path, target_size=(28,28))

    x_test = image.img_to_array(img)
    x_test = np.expand_dims(x_test, axis=0)
    x_test = np.array(x_test).reshape(-1, training_data.IMG_SIZE, training_data.IMG_SIZE, 1)
    images = np.vstack([x_test])
    val = model.predict(images)
    
    if val[2] < 0.5 :
        cls ="QR Code"
        scanner.decode_bar(img_path,cls)
        
    else:
        cls = "Barcode"
        scanner.decode_bar(img_path,cls)