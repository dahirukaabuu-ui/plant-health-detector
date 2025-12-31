import streamlit as st
import google.generativeai as genai
from PIL import Image

# Basic Setup
st.set_page_config(page_title="Dan Kaab AI Plant Doctor", page_icon="🌱")
st.title("🌱 Dan Kaab AI Plant Doctor")
st.write("Professional Diagnosis by **Dan Kaab Data Services**")

# Using your new API Key
API_KEY = "AIzaSyCF8IE1RrCcwzuVBLEDwFYdBckbU3TJ1zI" 
genai.configure(api_key=API_KEY)

file = st.file_uploader("Upload a plant leaf photo", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    # We use a broader model call to avoid the 404/Permission error
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = "Analyze this plant leaf. Identify the plant and any disease in English."
    
    with st.spinner('Analyzing...'):
        try:
            response = model.generate_content([prompt, img])
            st.success("Analysis Complete!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Permission Issue: {e}")
            st.info("Check if Gemini API is enabled in your Google Cloud Console.")

st.divider()
st.caption("© 2025 Dan Kaab Data Services | Bebeji, Kano State.")
