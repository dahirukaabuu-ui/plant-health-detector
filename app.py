import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page setup
st.set_page_config(page_title="Dan Kaab AI Plant Doctor", page_icon="🌱")

# Branding
st.title("🌱 Dan Kaab AI Plant Doctor")
st.write("Expert Plant Health Diagnosis by **Dan Kaab Data Services**")
st.info("Developed by: Dahiru Ka'abu")

# API Configuration - Using your latest key
API_KEY = "AIzaSyBc9gtcvzMa8MAkNF49YKzBIgQ8cBxIfS0" 
genai.configure(api_key=API_KEY)

# Image Uploader
file = st.file_uploader("Upload a photo of a plant leaf", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    # We use the stable Gemini 1.5 Flash model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = "Identify this plant and analyze its health status. If there is a disease, provide the name and a step-by-step solution. Write everything in clear English."
    
    with st.spinner('Dan Kaab AI is analyzing the leaf... Please wait.'):
        try:
            # AI analysis
            response = model.generate_content([prompt, img])
            st.success("Analysis Complete!")
            st.subheader("Diagnostic Results:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Analysis Error: {e}")
            st.warning("If the error persists, please ensure your API Key has all permissions enabled in Google Cloud.")

st.divider()
st.caption("© 2025 Dan Kaab Data Services | Bebeji, Kano State.")
