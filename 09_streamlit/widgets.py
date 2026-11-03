import streamlit as st
import pandas as pd

st.title("streamlit text input")

name = st.text_input("Enter your name:")


if name:
    st.write(f"Hello,{name}")

age = st.slider("select your age:",0,100,25)

if age:
    st.write(f"Your age is ,{age}")

options = ["python","java","cpp","javascript"]
choice = st.selectbox("choose your favourite language:",options)
st.write(f"You selected {choice}.")

data = {
    "Name":["nishu","nitish","manshi","aishwarya"],
    "Age":[21,90,87,35],
    "City" : ["Delhi","Lucknow","patna","banaras"]
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("choose a CSV file",type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)