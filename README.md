# ML-clothing-predictions-web-app
A web application based on the Streamlit framework, that is capable of categorizing images provided by a user with different methods.

This web application allows us to classify clothing images into 10 categories that are referred to the Fashion Mnist Dataset. In the navigation menu on the left of the main page, we can see all the options given to the user as well as the option “About us”, where the details about the creators  with contact information are listed. A preview of the home menu of the application is given below:

![Screenshot_1](https://user-images.githubusercontent.com/64161512/147825150-8a05bdc3-9407-49d4-8622-4f9cc18eee4b.jpg)

A clothing image can be classified into 10 categories by our trained model with three diffrent ways:

**1. Random Image Classification**, in which the user can randomly pull an image from the test dataset, and let the classification model predict its category.

**2. Upload & Classify**, in which the user can upload an image (type png or jpg) of their interest and let the classifier predict its label.

**3. Classify the URL**, in which the user can provide a URL of an image, and the classification model will predict its category.


After every prediction, emojis are being displayed to the user depending on the probability of categorizing correctly the image. Also, 2 random facts about the category of the predicted image are beign shown.

The 10 clothing categories that the model can predict are the following:

• Class 0: T-shirt/top

• Class 1: Trouser

• Class 2: Pullover

• Class 3: Dress

• Class 4: Coat

• Class 5: Sandal

• Class 6: Shirt

• Class 7: Sneaker

• Class 8: Bag

• Class 9: Ankle boot

For more information about the dataset, checkout https://www.kaggle.com/zalando-research/fashionmnist.
