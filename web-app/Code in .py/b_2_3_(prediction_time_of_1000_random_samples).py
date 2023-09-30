# -*- coding: utf-8 -*-
"""B.2.3 (Prediction Time of 1000 random samples).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_uklQY0KucZeJyDbp6dHcPG42HMmGULI
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, Activation
from keras.optimizers import Adam
from keras.callbacks import TensorBoard
from matplotlib import pyplot as plt
from keras.utils.np_utils import to_categorical 
from keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import BatchNormalization
import time
from sklearn.metrics import classification_report

# In this section, we chose to train the best models and retrieve the time it takes to train a model so that it can predict 1000 images.
# We chose to keep 1 model per CNN type, 1 for a 1-Layer CNN, 1 for a 2-Layer CNN, 1 for a 3-Layer CNN, 1 for a 4-Layer CNN

# Define the 1st Convolutional Neural Network, the best of our 1-Layer CNN tested so far.
name1 = '1_NN_256'
cnn_model_1 = Sequential([], name = name1)
# 1st Convolutional Layer
cnn_model_1.add(Conv2D(256, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
cnn_model_1.add(MaxPooling2D(pool_size=(2, 2)))
cnn_model_1.add(BatchNormalization())
cnn_model_1.add(Flatten())
cnn_model_1.add(Dense(128, activation='relu'))
cnn_model_1.add(Dense(10, activation='softmax'))

# Define the 2nd Convolutional Neural Network, the best of our 2-Layer CNN tested so far.
name2 = '2_NN_128_128'
cnn_model_2 = Sequential([], name = name2)
# 1st Convolutional Layer
cnn_model_2.add(Conv2D(128, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
cnn_model_2.add(MaxPooling2D(pool_size=(2, 2)))
cnn_model_2.add(BatchNormalization())
# 2nd Convolutional Layer
cnn_model_2.add(Conv2D(128, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
cnn_model_2.add(BatchNormalization())
cnn_model_2.add(Flatten())
cnn_model_2.add(Dense(128, activation='relu'))
cnn_model_2.add(Dense(10, activation='softmax'))

# Define the 3rd Convolutional Neural Network, the best of our 3-Layer CNN tested so far.
name3 = '3_NN_128_256_256'
cnn_model_3 = Sequential([], name = name3)
# 1st Convolutional Layer
cnn_model_3.add(Conv2D(128, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
cnn_model_3.add(MaxPooling2D(pool_size=(2, 2)))
cnn_model_3.add(BatchNormalization())
# 2nd Convolutional Layer
cnn_model_3.add(Conv2D(256, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
cnn_model_3.add(BatchNormalization())
# 3rd Convolutional Layer
cnn_model_3.add(Conv2D(256, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
cnn_model_3.add(Dense(256, activation='relu'))
cnn_model_3.add(Flatten())
cnn_model_3.add(Dense(128, activation='relu'))
cnn_model_3.add(Dense(10, activation='softmax'))

# Define the 4th Convolutional Neural Network, the best of our 4-Layer CNN tested so far.
name4 = '4_NN_128_128_128_128'
cnn_model_4 = Sequential([],name = name4)
# 1st Convolutional Layer
cnn_model_4.add(Conv2D(128, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
cnn_model_4.add(BatchNormalization())
# 2nd Convolutional Layer
cnn_model_4.add(Conv2D(128, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
cnn_model_4.add(MaxPooling2D(pool_size=(2, 2)))
cnn_model_4.add(BatchNormalization())
# 3rd Convolutional Layer
cnn_model_4.add(Conv2D(128, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
cnn_model_4.add(Dense(128, activation='relu'))
# 4th Convolutional Layer
cnn_model_4.add(Conv2D(128, kernel_size=(3, 3), activation='relu', input_shape=(28,28,1)))
cnn_model_4.add(MaxPooling2D(pool_size=(2, 2)))
cnn_model_4.add(BatchNormalization())
cnn_model_4.add(Flatten())
cnn_model_4.add(Dense(128, activation='relu'))
cnn_model_4.add(Dense(10, activation='softmax'))

# Edit the following 2 lines if you want to get the classification report for every model.
# cnn_models = [cnn_model_1,cnn_model_2,cnn_model_3,cnn_model_4]
cnn_models=[cnn_model_4]
names=[name1, name2, name3, name4]

# ~ Data preprocessing section ~
# Save the training data from fashion-mnist_test.csv to the "train" DataFrame
train = pd.read_csv("drive/MyDrive/Colab Notebooks/fashion-mnist_train.csv")
# Save the testing data from fashion-mnist_test.csv to the "test" DataFrame
test = pd.read_csv("drive/MyDrive/Colab Notebooks/fashion-mnist_test.csv")

def bullet_1v2(model,fig_num):
    # ~ Data Preprocessing
    Y_train = train['label'].values
    X_train = train.drop(labels = ['label'], axis = 1)
    X_train = X_train / 255.0
    X_train = X_train.values.reshape(-1,28,28,1)
    Y_train = to_categorical(Y_train, num_classes = 10)
    # test0 refers to the 1000 random images, that will test our models
    test0=test.sample(n=1000)
    X_test = test0.drop(labels = ['label'], axis = 1)
    X_test = X_test / 255.0
    X_test = X_test.values.reshape(-1,28,28,1)
    
    optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)
    datagen = ImageDataGenerator(
            featurewise_center=False,  # set input mean to 0 over the dataset
            samplewise_center=False,  # set each sample mean to 0
            featurewise_std_normalization=False,  # divide inputs by std of the dataset
            samplewise_std_normalization=False,  # divide each input by its std
            zca_whitening=False,  # dimesion reduction
            rotation_range=0.1,  # randomly rotate images in the range
            zoom_range = 0.1, # Randomly zoom image
            width_shift_range=0.1,  # randomly shift images horizontally
            height_shift_range=0.1,  # randomly shift images vertically
            horizontal_flip=False,  # randomly flip images
            vertical_flip=False)  # randomly flip images
    model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    datagen.fit(X_train)
    X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size = 0.1, random_state = 2)
    history = model.fit_generator(datagen.flow(X_train, Y_train, batch_size=128),
                                  shuffle=True, epochs=2, 
                                  validation_data = (X_val, Y_val),verbose = 1, 
                                  steps_per_epoch=X_train.shape[0] // 128)
    
    ## Make predictions of classes
    start=time.time()
    predicted_classes = model.predict_classes(X_test)
    end=time.time()
    
    # Get true labels of test data 
    y_true = test0.iloc[:, 0]
    # Convert to np array
    y_true=np.array(y_true)
    predicted_classes=np.array(predicted_classes)
    # Set name of classes 
    target_names = ["Class{}".format(i) for i in range(10)]
    # Classification report to get precision recall f1 score support
    print(classification_report(y_true, predicted_classes, target_names=target_names))
    # Print the time the model needs to predict 1000 images
    print("Prediction of 1000 images time:",end-start)
    """
    Precision= Accuacy of positive predictions - What percent of your predictions were correct?
    Recall = Fraction of positives that were correctly indetified -What percent of the positive cases did you catch?
    F1 Score -What percent of positive predictions were correct?
    Support = the number of actual occurrences of the class in the specified dataset.
    """

fig_num=0
# By calling the function, the training begins for every model 
for model in cnn_models:
    bullet_1v2(model,fig_num)
    fig_num+=1