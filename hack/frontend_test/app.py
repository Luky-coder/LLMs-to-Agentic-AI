import streamlit as st
import requests

st.title("App Upload Text + Image")

# Input texte
text_input = st.text_input("Entrez un message :")

# Input image
image_file = st.file_uploader("Choisissez une image", type=["png", "jpg", "jpeg"])

# Soumettre
if st.button("Envoyer"):

    if not text_input or not image_file:
        st.warning("Veuillez remplir le texte et choisir une image.")
    else:
        # Préparer les données
        files = {
            "image": (image_file.name, image_file, image_file.type),
        }
        data = {
            "text": text_input,
        }

        try:
            # ⚠️ Remplace l'URL par ton adresse réelle FastAPI
            response = requests.post("http://localhost:8080/upload", data=data, files=files)

            if response.status_code == 200:
                st.success("Succès : " + response.text)
            else:
                st.error(f"Erreur {response.status_code} : {response.text}")
        except Exception as e:
            st.error(f"Erreur de requête : {e}")

# Soumettre pour test GET
if st.button("Test"):
    try:
        # ⚠️ Remplace l'URL par ton adresse réelle FastAPI
        response = requests.get("http://localhost:8000/")

        if response.status_code == 200:
            st.success("Succès : " + response.text)
        else:
            st.error(f"Erreur {response.status_code} : {response.text}")
    except Exception as e:
        st.error(f"Erreur de requête : {e}")