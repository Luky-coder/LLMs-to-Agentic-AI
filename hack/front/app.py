import streamlit as st
import requests

# App title
st.title("Upload App - Text + Image")

# Text input field
text_input = st.text_input("Enter a message:")

# Image file uploader
image_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if st.button("Submit"):
    """Handles the submission of the text and image to the backend API."""

    if not text_input or not image_file:
        st.warning("Please provide both text and an image.")
    else:
        files = {
            "image": (image_file.name, image_file, image_file.type),
        }
        data = {
            "text": text_input,
        }

        try:
            response = requests.post("http://localhost:8080/upload", data=data, files=files)

            if response.status_code == 200:
                st.success("Success: " + response.text)
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Request error: {e}")

if st.button("Test"):
    """Tests the connection with the backend API."""
    try:
        response = requests.get("http://localhost:8000/")

        if response.status_code == 200:
            st.success("Success: " + response.text)
        else:
            st.error(f"Error {response.status_code}: {response.text}")
    except Exception as e:
        st.error(f"Request error: {e}")
