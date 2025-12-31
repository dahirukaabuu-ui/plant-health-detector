
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Saita sunan manhajar
st.set_page_config(page_title="Dan Kaab AI Plant Doctor")
st.title("🌱 Dan Kaab AI Plant Doctor")
st.write("Specialist AI tool by **Dan Kaab Data Services**")

# Lambobin API dinka
API_KEY = "AIzaSyB__fefzf86ArcRLMyNsYKltVucdeSEi6I" 
genai.configure(api_key=API_KEY)

file = st.file_uploader("Upload a photo of a plant leaf", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    # Sashin AI
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "Analyze this plant image. 1. Identify the plant. 2. Diagnose any disease or health issue. 3. Provide a step-by-step solution. Answer in English clearly."
    
    with st.spinner('Dan Kaab AI is analyzing the leaf... Please wait'):
        try:
            response = model.generate_content([prompt, img])
            st.success("Analysis Complete!")
            st.subheader("Diagnostic Results:")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
