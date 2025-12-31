import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page setup
st.set_page_config(page_title="Dan Kaab AI Plant Doctor", page_icon="🌱")

# Header
st.title("🌱 Dan Kaab AI Plant Doctor")
st.write("Professional AI Diagnosis by **Dan Kaab Data Services**")
st.info("Powered by Gemini 3 Flash")

# API Configuration
API_KEY = "AIzaSyB__fefzf86ArcRLMyNsYKltVucdeSEi6I" 
genai.configure(api_key=API_KEY)

# File uploader
file = st.file_uploader("Upload a photo of a plant leaf", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    # GYARA: Mun canza sunan model zuwa gemini-1.5-flash-8b
    # Wannan shi ne mafi sauri kuma mafi dacewa da Preview versions
    model = genai.GenerativeModel('gemini-1.5-flash-8b')
    
    prompt = "Identify this plant and its health status. If there is a disease, provide the name and a solution in English."
    
    with st.spinner('Dan Kaab AI is analyzing using Gemini 3...'):
        try:
            response = model.generate_content([prompt, img])
            st.success("Analysis Complete!")
            st.subheader("Diagnostic Results:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Check if your API Key supports Gemini 1.5/3 models in AI Studio.")

st.divider()
st.caption("© 2025 Dan Kaab Data Services | Bebeji, Kano State.")
