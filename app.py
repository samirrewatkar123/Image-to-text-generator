from dotenv import load_dotenv
load_dotenv() # Loading all the enviorments

import streamlit as st
import os
import google.generativeai as genai
import pathlib
import textwrap
from PIL import Image



os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to load gemini_pro_model
model=genai.GenerativeModel('gemini-2.0-flash-exp')
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
        response=model.generate_content(image)

    return response.text

# Initialize streamlit app

st.set_page_config(page_title='Teleperformance Demo Application (Img2Text)')
st.header("Demo Content Creator Application")
input=st.text_input("Input Prompt : ",key='input')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.",  use_container_width =True)


submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
