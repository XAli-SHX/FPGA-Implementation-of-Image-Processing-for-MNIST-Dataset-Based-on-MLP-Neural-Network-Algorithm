from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np

"""
model = keras.Sequential(
        [
            keras.Input(shape=input_shape),
            layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D(pool_size=(2, 2)),
            layers.Flatten(),
            layers.Dropout(0.5),
            layers.Dense(num_classes, activation="softmax"),
        ]
    )
"""

if __name__ == "__main__":
    model = keras.models.load_model("./trained_model.h5", compile=True)
    layer0_conv2d = model.layers[0]
    layer0_file = open("./coeffs/layer0_conv2d.txt", "w")
    layer0_file.write(str(layer0_conv2d.weights))
    layer0_file.close()
    print("hi")