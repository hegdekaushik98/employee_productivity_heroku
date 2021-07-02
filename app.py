import streamlit as st
import numpy as np
from PIL import Image
from detection.object_detection import detect_object
import cv2


def main():
    st.title("Employee Working or Not Working")

    img_array = upload_image_ui()
    # st.write(img_array.shape)
    # st.write(img_array.shape)

    # rgbImage = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
    # img_array = rgbImage


    if isinstance(img_array, np.ndarray):
        image = detect_object(img_array)
        st.image(image, width = 412)

def upload_image_ui():
    uploaded_image = st.file_uploader("Please upload an image file", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        try:
            image = Image.open(uploaded_image)

        except Exception:
            st.error("Error: Invalid image")
        else:
            img_array = np.array(image)
            img_array = cv2.cvtColor(img_array, cv2.COLOR_RGBA2RGB)
            return img_array

if __name__ == '__main__':
    main()
