# -*- coding: utf-8 -*-
"""resnet-50.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_2pAxKLFqcqfkuxbUXcKdj61WUpvbmes
"""

from keras.applications import ResNet50
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.regularizers import l2

from google.colab import drive
drive.mount('/content/drive')

train_path = '/content/drive/MyDrive/AYZEK-Kanarya/dataset/train'
test_path = '/content/drive/MyDrive/AYZEK-Kanarya/dataset/test'
val_path = '/content/drive/MyDrive/AYZEK-Kanarya/dataset/val'

train_data_gen = ImageDataGenerator(rescale=1/255) # Ölçeklendirme
test_data_gen = ImageDataGenerator(rescale=1/255)
val_data_gen = ImageDataGenerator(rescale=1/255)

train_generator = train_data_gen.flow_from_directory(
        train_path,
        target_size=(224, 224), # Görüntü boyutları
        batch_size=32,
        class_mode='categorical')  # Sınıf modu, çok sınıflı bir sınıflandırma olduğu için 'categorical'

test_generator = test_data_gen.flow_from_directory(
    test_path,
    target_size=(224, 224),  # Görüntü boyutları
    batch_size=32,
    class_mode='categorical'  # Sınıf modu, çok sınıflı bir sınıflandırma olduğu için 'categorical'
)

val_generator = val_data_gen.flow_from_directory(
    val_path,
    target_size=(224, 224),  # Görüntü boyutları
    batch_size=32,
    class_mode='categorical'  # Sınıf modu, çok sınıflı bir sınıflandırma olduğu için 'categorical'
)

checkpoint = ModelCheckpoint(
    f'/content/drive/MyDrive/AYZEK-Kanarya/models/resnet-50/resnet-50_model1.h5',
     monitor='val_accuracy',
     verbose=1,
     save_best_only=True,
     mode = 'max'
)

earlystop = EarlyStopping(monitor='val_accuracy',
                          patience=5,
                          verbose=1,
                          mode = 'max')

model = Sequential()
resnet = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
model.add(resnet)

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(4, activation='softmax'))

model.compile(optimizer='Adadelta', loss='categorical_crossentropy', metrics=['accuracy'])

# Modeli eğitme
results = model.fit(train_generator, epochs=20, verbose=1, callbacks=[checkpoint,earlystop], validation_data= val_generator)

import matplotlib.pyplot as plt
train_loss = results.history['loss']
train_accuracy = results.history['accuracy']

# train loss ve train accuracy görselleştirilmesi
epochs = range(1, len(train_loss) + 1)

plt.plot(epochs, train_loss, 'b', label='Training loss')
plt.plot(epochs, train_accuracy, 'r', label='Training accuracy')
plt.title('Training Loss and Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss / Accuracy')
plt.legend()

plt.show()

test_loss, test_accuracy = model.evaluate(test_generator, steps=len(test_generator))
print(f"Test Loss: {test_loss}")
print(f"Test Accuracy: {test_accuracy}")

#model ile tahmin (test verileriyle)
predictions = model.predict(test_generator)

# test verileri ve tahmin edilen değerler arasındaki karşılaştırma
num_samples_to_visualize = 20
test_labels = []  # Gerçek değerleri tutan boş liste
predicted_labels = []  # Tahmin edilen değerleri tutan boş liste

# Test verilerinden örnekleri al
for i, (_, labels) in enumerate(test_generator):
    test_labels.extend(labels.argmax(axis=1))  # Gerçek etiketleri al
    predicted_labels.extend(predictions.argmax(axis=1))  # Tahmin edilen etiketleri al
    if i == num_samples_to_visualize - 1:
        break

# Sonuçları görselleştir
plt.figure(figsize=(12, 8))
for i in range(num_samples_to_visualize):
    plt.subplot(5, 4, i + 1)
    plt.imshow(test_generator[i][0][0])  # Test resmini göster
    plt.title(f'Real: {test_labels[i]}, Predicted: {predicted_labels[i]}')
    plt.axis('off')

plt.tight_layout()
plt.show()