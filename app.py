import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup
st.set_page_config(page_title="Dan Kaab AI Plant Doctor", page_icon="🌱")
st.title("🌱 Dan Kaab AI Plant Doctor")
st.write("Expert Diagnosis by **Dan Kaab Data Services**")

# API Configuration
API_KEY = "AIzaSyB__fefzf86ArcRLMyNsYKltVucdeSEi6I" 

# WANNAN SHI NE GYARAN: Muna amfani da v1beta kai tsaye
genai.configure(api_key=API_KEY, transport='rest')

file = st.file_uploader("Upload plant photo", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    # Amfani da sunan model din da kake gani a AI Studio dinka
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    
    prompt = "Identify this plant and analyze its health in English."
    
    with st.spinner('Analyzing...'):
        try:
            # Tura hoton zuwa Google
            response = model.generate_content([prompt, img])
            st.success("Analysis Complete!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
