import streamlit as st
import google.generativeai as genai
from PIL import Image

# Set the page configuration
st.set_page_config(page_title="Dan Kaab AI Plant Doctor", page_icon="🌱")

# Header and Information
st.title("🌱 Dan Kaab AI Plant Doctor")
st.write("This application uses Artificial Intelligence (AI) to diagnose plant health issues from photos.")
st.info("Developed by: **Dan Kaab Data Services**")

# Configure the API Key
API_KEY = "AIzaSyB__fefzf86ArcRLMyNsYKltVucdeSEi6I" 
genai.configure(api_key=API_KEY)

# Image upload section
file = st.file_uploader("Upload a photo of a plant leaf", type=["jpg", "png", "jpeg"])

if file:
    # Display the uploaded image
    img = Image.open(file)
    st.image(img, caption="Uploaded Plant Photo", use_container_width=True)
    
    # AI Model Configuration
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Instructions for the AI
    prompt = """
    Analyze this plant image in detail.
    1. Identify the name of the plant.
    2. Determine if the plant is healthy or diseased.
    3. If diseased, identify the specific disease or deficiency.
    4. Provide a step-by-step treatment or solution.
    Write the entire response in clear English.
    """
    
    with st.spinner('Dan Kaab AI is analyzing the image... Please wait.'):
        try:
            # Generate the content using AI
            response = model.generate_content([prompt, img])
            
            # Show the results
            st.success("Analysis Complete!")
            st.subheader("Diagnostic Results:")
            st.markdown(response.text)
            
        except Exception as e:
            # Error handling
            st.error(f"An error occurred: {e}")
            st.info("Please ensure your requirements.txt includes: google-generativeai>=0.7.0")

# Footer
st.divider()
st.caption("© 2025 Dan Kaab Data Services | Bebeji, Kano State.")
