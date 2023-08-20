from django.shortcuts import render

import tensorflow as tf
from PIL import Image
import numpy as np


def home(request):

    model_path = "saved_models\Brain_MRI_1.h5"

    model = tf.keras.models.load_model(model_path)



    class_names = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

    context = {'prediction': None}

    if request.method == 'POST' and request.FILES['image']:

        uploaded_image = request.FILES['image']

        img = Image.open(uploaded_image)
        height = 255
        width = 255

        img = img.resize((width, height))
        img_array = np.array(img)

        prediction = model.predict(tf.expand_dims(img_array, axis=0))

        f1 = "hello"

        prediction = np.argmax(prediction)
        print(prediction)
        prediction = class_names[prediction]
        print(prediction)

        context = {"prediction": prediction}

    return render(request, "home.html", context)