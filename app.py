import streamlit as st
import requests
from PIL import Image
import base64
import io

# Page setup
st.set_page_config(page_title="Dan Kaab AI Plant Doctor", page_icon="🌱")

# Branding
st.title("🌱 Dan Kaab AI Plant Doctor")
st.write("Professional Crop Diagnosis by **Dan Kaab Data Services**")
st.info("Developed by: Dahiru Ka'abu")

# API Configuration
API_KEY = "AIzaSyB__fefzf86ArcRLMyNsYKltVucdeSEi6I" 

def get_diagnosis(image_file):
    # Convert image to base64
    img_data = image_file.getvalue()
    base64_image = base64.b64encode(img_data).decode('utf-8')
    
    # Direct URL to bypass the 404 library issue
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"
    
    payload = {
        "contents": [{
            "parts": [
                {"text": "Identify this plant and its health status. If there is a disease, provide the name and a solution in English."},
                {"inline_data": {"mime_type": "image/jpeg", "data": base64_image}}
            ]
        }]
    }
    
    response = requests.post(url, json=payload)
    return response.json()

file = st.file_uploader("Upload a photo of a plant leaf", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    with st.spinner('Dan Kaab AI is analyzing...'):
        try:
            result = get_diagnosis(file)
            # Extract text from the API response
            diagnosis_text = result['candidates'][0]['content']['parts'][0]['text']
            st.success("Analysis Complete!")
            st.subheader("Diagnostic Results:")
            st.markdown(diagnosis_text)
        except Exception as e:
            st.error("Analysis Failed.")
            st.write("Detailed error information for debugging:")
            st.json(result) # This shows exactly what Google is saying

st.divider()
st.caption("© 2025 Dan Kaab Data Services | Bebeji, Kano State.")
