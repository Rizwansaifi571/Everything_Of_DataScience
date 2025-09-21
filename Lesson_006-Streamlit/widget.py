import streamlit as st
import pandas as pd 

name = st.text_input("Enter your name : ")
if name:
    st.write(f'Hello {name}!!')

age = st.slider('Select your age : ', 0, 100, 21)
st.write(f"Your age is {age}.")

options = ['Python', 'Java', 'C++', 'JavaScript']
choice = st.selectbox('Choose your favourate Language : ', options)
st.write(f'You select {choice}')

upload_file = st.file_uploader("Choose a CSV file", type = "csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)