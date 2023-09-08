"""APP"""
import streamlit as st
import numpy as np
from PIL import Image

from src.segment import align_and_process_image


# Streamlit app
def main():
    """
    Streamlit app for Image Alignment Demo.
    Allows users to upload an image, process it, and display the original and rotated images
    along with length and width information.
    """
    st.title("Image Alignment Demo")

    # Sidebar for selecting input and output folders
    uploaded_image = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png", "bmp", "gif"])

    if st.button("Process Image"):
        pil_image = Image.open(uploaded_image)
        rotated_image, stats = align_and_process_image(np.array(pil_image))

        if (rotated_image is not None) and (stats is not None):

            # Display the original and rotated images
            st.image([pil_image, rotated_image], caption=["Original Image", "Rotated Image"], use_column_width=True)

            # Print the length and width information
            st.write("Length of the sample is", len(stats))
            st.write("Max width of the sample is", max(stats))
        else:
            st.write("No contours found in the image. Please try another image.")


if __name__ == "__main__":
    main()
