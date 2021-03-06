import tensorflow as tf
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import img_to_array


def ImageClassf():
    model = Sequential()
    model.add(
        Conv2D(120,
               60,
               3,
               padding="same",
               activation="relu",
               input_shape=(640, 360, 3)))
    model.add(MaxPooling2D(pool_size=(65, 25), padding="same"))
    model.add(Dropout(0.5))

    model.add(Conv2D(60, 30, 3, padding="same"))
    model.add(MaxPooling2D(pool_size=(60, 25), padding="same"))
    model.add(Dropout(0.5))

    model.add(Conv2D(60, 25, 3, padding="same"))
    model.add(MaxPooling2D(pool_size=(60, 25), padding="same"))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.5))

    model.add(Dense(2, activation="softmax"))
    model.compile(loss="categorical_crossentropy",
                  optimizer="Nadam",
                  metrics=["accuracy"])
    return model
