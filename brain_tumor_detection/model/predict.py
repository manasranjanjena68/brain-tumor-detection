# model/predict.py

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load model once
MODEL_PATH = "model/Brain_Tumor.h5"
model = load_model(MODEL_PATH)

# Define your class labels
class_labels = ['pituitary', 'glioma', 'notumor', 'meningioma']

def predict_tumor(img_path, image_size=128):
    try:
        # Load and preprocess the image
        img = load_img(img_path, target_size=(image_size, image_size))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Prediction
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        confidence = np.max(predictions)

        # Interpret result
        if class_labels[predicted_class] == 'notumor':
            return ("No Tumor", confidence * 100)
        else:
            return (class_labels[predicted_class], confidence * 100)

    except Exception as e:
        return ("Error", str(e))
