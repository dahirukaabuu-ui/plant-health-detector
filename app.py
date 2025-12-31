import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page setup
st.set_page_config(page_title="Dan Kaab AI Plant Doctor", page_icon="🌱")
st.title("🌱 Dan Kaab AI Plant Doctor")
st.write("Professional Diagnosis by **Dan Kaab Data Services**")

# Your latest API Key
API_KEY = "AIzaSyBc9gtcvzMa8MAkNF49YKzBIgQ8cBxIfS0" 
genai.configure(api_key=API_KEY)

file = st.file_uploader("Upload a plant leaf photo", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    # GYARA: Mun saka 'models/' a gaban sunan
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    
    prompt = "Identify this plant and its health status. If there is a disease, provide the name and a solution in English."
    
    with st.spinner('Dan Kaab AI is analyzing...'):
        try:
            # Generate response
            response = model.generate_content([prompt, img])
            st.success("Analysis Complete!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Check if your API Key supports this model in Google AI Studio.")

st.divider()
st.caption("© 2025 Dan Kaab Data Services | Bebeji, Kano State.")
