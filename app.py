import streamlit as st
import google.generativeai as genai
from PIL import Image

# Saita fasalin shafin manhajarka
st.set_page_config(page_title="Dan Kaab AI Plant Doctor", page_icon="🌱")

# Sunan manhaja da bayanan Dan Kaab Data Services
st.title("🌱 Dan Kaab AI Plant Doctor")
st.write("Wannan manhaja tana amfani da Artificial Intelligence (AI) domin gano matsalolin shuka.")
st.info("Developed by: **Dan Kaab Data Services**")

# Saka lambobin API Key ɗinka
API_KEY = "AIzaSyB__fefzf86ArcRLMyNsYKltVucdeSEi6I" 
genai.configure(api_key=API_KEY)

# Wurin ɗora hoto
file = st.file_uploader("Upload a photo of a plant leaf (Ɗora hoton ganyen shuka)", type=["jpg", "png", "jpeg"])

if file:
    # Nuna hoton da aka ɗora
    img = Image.open(file)
    st.image(img, caption="Hoton da ka ɗora", use_column_width=True)
    
    # Sashin AI (Mun gyara sunan model ɗin zuwa flash-latest)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    # Umarnin da za a ba AI
    prompt = """
    Look at this plant image carefully. 
    1. Identify the name of the plant.
    2. Check if the plant has any disease or nutritional deficiency.
    3. Provide a clear solution or treatment in English.
    Please be professional and concise.
    """
    
    with st.spinner('Dan Kaab AI yana binciken hoton... Dakata kaɗan'):
        try:
            # Karatun hoto daga AI
            response = model.generate_content([prompt, img])
            
            # Nuna sakamako
            st.success("An kammala bincike!")
            st.subheader("Diagnostic Results (Sakamakon Bincike):")
            st.write(response.text)
            
        except Exception as e:
            # Idan an samu matsala
            st.error(f"An samu matsala: {e}")
            st.warning("Tabbatar cewa API Key ɗinka yana aiki kuma intanet ɗinka tana da ƙarfi.")

# Bayani na ƙasa
st.divider()
st.caption("© 2025 Dan Kaab Data Services | Bebeji, Kano State.")
