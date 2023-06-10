import streamlit as st
#https://realpython.com/image-processing-with-the-python-pillow-library/#:~:text=PIL%20stands%20for%20Python%20Imaging,includes%20support%20for%20Python%203.
from PIL import Image
import numpy as np
from keras.models import load_model

model = load_model('model.h5')

st.title('Hot Dog or Not Hot Dog?')

#https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader 
uploaded_image = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    # Display uploaded image
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess image
    image = image.resize((28, 28))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    # Make prediction
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)

    class_names = ['hot dog', 'not hot dog']
    result = class_names[predicted_class]

    st.write('Prediction:', result)

