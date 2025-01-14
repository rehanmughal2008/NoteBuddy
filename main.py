import streamlit as st
from pypdf import PdfReader
import google.generativeai as genai
import os
from dotenv import load_dotenv
from get_text import text_extractor

#Page config
st.set_page_config(
    page_title="NoteBuddy",
    page_icon="🎓")
load_dotenv()

#gemini configuration
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

#Project Configuration
st.title('🎓NoteBuddy')
st.html("<style> .main {overflow: hidden} </style>")

#file to upload into gemini
uploaded_file = st.file_uploader("Choose a file", type="pdf", accept_multiple_files=False)

#establish placeholder JSON
class response:
    text = ""

if st.button("Generate Notes", use_container_width=True):
    if uploaded_file is not None:
        # Display the uploaded file name
        #st.write(f"Uploaded file: {uploaded_file.name}")

        with st.spinner(text="Loading Your Notes..."):
                response = model.generate_content("Give me a detail set of notes based off of the following text and images(if any):" + text_extractor(uploaded_file))
    else:
        st.warning("Please upload a file first")

#Resulting AI text
st.markdown(response.text)