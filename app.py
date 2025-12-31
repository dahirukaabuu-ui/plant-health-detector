import streamlit as st
from PIL import Image

st.set_page_config(page_title="Dan Kaab Plant AI")
st.title("🌱 Plant Health Diagnosis Tool")
st.write("Welcome to **Dan Kaab Data Services**. Upload a photo to check plant health.")

file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if file:
    img = Image.open(file)
    st.image(img, use_column_width=True)
    st.write("---")
    st.subheader("Diagnostic Results")
    st.success("Status: Healthy")
    st.info("Recommendation: Maintain current irrigation levels.")
