import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Hello, {name}")

age = st.slider("Select your age:", 0, 100, 25)

st.write(f"Your age is {age}.")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favorite language", options=options)
st.write(f"You selected {choice}.")



data = {
    "Name": ["Jhon", "Jane", "Jake", "Jill"],
    "Age":  [28, 34, 64, 26],
    "City": ["New Your", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("Sampledata.csv")
st.write(df)

upload_file = st.file_uploader("Choose a CSV file", type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)