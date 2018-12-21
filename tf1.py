# TensorFlow and tf.keras
import tensorflow as tf
from pprint import pprint as print
from tensorflow import keras
import json

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from NumpyEncoder import NumpyEncoder

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(train_images.shape)

print(len(train_labels))

print(train_labels)

print(test_images.shape)

print(len(test_labels))


def save_train(images, name: str):
    fig = plt.figure(figsize=(20, 20))
    for i in range(100):
        plt.subplot(10, 10, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    file_name = 'tmp/%s.png' % (name)
    fig.savefig(file_name, dpi=100)
    plt.close(fig)


train_images = train_images / 255.0
test_images = test_images / 255.0

save_train(train_images, 'train_images')
save_train(test_images, 'test_images')

dense1 = keras.layers.Dense(128, activation=tf.nn.sigmoid)
dense2 = keras.layers.Dense(10, activation=tf.nn.softmax)
print(dense1.get_weights())
print(dense2.get_weights())

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    dense1,
    dense2
])
model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=1)
with open('tmp/dense1.json', 'w') as outfile:
    json.dump(dense1.get_weights(), outfile, cls=NumpyEncoder)

with open('tmp/dense2.json', 'w') as outfile:
    json.dump(dense2.get_weights(), outfile, cls=NumpyEncoder)

with open('tmp/model.json', 'w') as outfile:
    json.dump(model.get_weights(), outfile, cls=NumpyEncoder)


test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)


predictions = model.predict(test_images)
print(predictions[0])
