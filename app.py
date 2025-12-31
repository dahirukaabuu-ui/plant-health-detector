import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page setup
st.set_page_config(page_title="Dan Kaab AI Plant Doctor", page_icon="🌱")
st.title("🌱 Dan Kaab AI Plant Doctor")
st.write("Professional AI Diagnosis by **Dan Kaab Data Services**")

# API Configuration
API_KEY = "AIzaSyB__fefzf86ArcRLMyNsYKltVucdeSEi6I" 
genai.configure(api_key=API_KEY)

file = st.file_uploader("Upload plant photo", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_container_width=True)
    
    # MUN GYARA NAN: Muna kiran model din kai tsaye ba tare da 'models/' ba
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = "Identify this plant and its health status. If there is a disease, provide the name and a solution in English."
    
    with st.spinner('Dan Kaab AI is analyzing...'):
        try:
            # Generate content
            response = model.generate_content([prompt, img])
            st.success("Analysis Complete!")
            st.subheader("Diagnostic Results:")
            st.markdown(response.text)
        except Exception as e:
            # Idan flash bai yi ba, zai gwada amfani da pro
            try:
                model_alt = genai.GenerativeModel('gemini-1.5-pro')
                response = model_alt.generate_content([prompt, img])
                st.success("Analysis Complete (Pro)!")
                st.markdown(response.text)
            except Exception as e2:
                st.error(f"Error: {e2}")
                st.info("Please verify your API key permissions in Google AI Studio.")

st.divider()
st.caption("© 2025 Dan Kaab Data Services | Bebeji, Kano State.")
