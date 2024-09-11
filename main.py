import google.generativeai as genai
import streamlit as st
import pathlib
import textwrap
import PIL.Image
from dotenv import load_dotenv
import os
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')


def identify_ingredients(img):
    print(type(img))
    response = model.generate_content(["Write the list of food ingredients in the image and only names sepeated by comma(,)", img], stream=True)
    response.resolve()
    identified_ingredients = response.text
    return identified_ingredients
# Title
st.title("FlavorForge")
# Image uploader
uploaded_image = st.file_uploader("Upload an image of ingredients", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    # Display the uploaded image
    with open("uploaded_image.png", "wb") as f:
        f.write(uploaded_image.getvalue())
    uploaded_image = PIL.Image.open("uploaded_image.png")
    st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
    # Call your backend logic for ingredient identification
    identified_ingredients = identify_ingredients(uploaded_image)
    if identified_ingredients:
        st.write("Identified Ingredients:", identified_ingredients)

# User inputs
    meal_type = st.selectbox("Select meal type:", ["Lunch", "Dinner", "Snack", "Dessert"])
    kitchen_tools = st.multiselect("Select kitchen tools:", ["Stove top", "Oven", "Microwave", "Air Fryer", "Blender", "Food Processor", "BBQ", "Pressure Cooker"])
    time_available = st.slider("How much time do you have to cook?", min_value=0, max_value=120, step=5)
    expertise_level = st.selectbox("Are you a good Chef?", ["Novice", "Intermediate", "Expert"])
    model = genai.GenerativeModel('gemini-pro')
# Generate recipe suggestions
    if meal_type and kitchen_tools and time_available and expertise_level and identified_ingredients:
        prompt = f"""Write a Recipe with following things 
        How much time do you have to cook : {time_available} minutes, 
        How much good of a chef person is : {expertise_level}, 
        Which Ingredients did he possess: {identified_ingredients},
        Which Kitchen Tools does he has: {kitchen_tools}
        Given and The output must be the Name of Recipe and the Instructions(seperated by full stop(.))"""
        response = model.generate_content([prompt], stream=True)
        response.resolve()
        st.write(response.text)
# Display recipe suggestions


# Display more recipes if available

