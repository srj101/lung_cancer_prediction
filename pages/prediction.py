import gdown
import tensorflow as tf
from PIL import Image
import numpy as np
import streamlit as st

st.title("Prediction")

# Google Drive File ID for the model
# Replace with your actual ID
MODEL_URL = "https://drive.google.com/uc?id=1hM70fRdbtZ6GusaRPKRqfBYGdz73mY3c"


@st.cache(allow_output_mutation=True)
def load_model():
    model_path = "model.keras"
    # Download the model from Google Drive if it's not already present
    gdown.download(MODEL_URL, model_path, quiet=False)
    model = tf.keras.models.load_model(model_path)
    return model


model = load_model()

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Preprocess the image
    image = image.resize((256, 256))
    img_array = tf.keras.utils.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)
    img_array = tf.image.rgb_to_grayscale(img_array)
    img_array = img_array / 255
    predictions = model.predict(img_array)
    result = np.argmax(predictions)
    score = predictions[0][result]  # Confidence score for the predicted class
    CLASS_NAMES = ['Benign', 'Malignant', 'Normal']

    # Display the predicted class and score
    st.write(f"Predicted class: {CLASS_NAMES[result]}")
    st.write(f"Prediction score: {score*100:.2f}%")

    # Display additional details like image dimensions
    st.write(f"Resized image dimensions: 256 x 256")
else:
    st.write("Please upload an image file to proceed.")
