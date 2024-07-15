import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name=st.text_input("Enter your name:")

age=st.slider("select your age:" , 0,100,25)

st.write(f"your age is {age}.")

options = ["Python","Java","C++","Javascript"]
choice = st.selectbox("choose your favorite language:",options)
st.write(f" your selected {choice}.")

if name:
    st.write(f"Hello, {name}")

data= {
    "Name": ["john", "jane","jake","jill"],
    "Age":[28,24,35,40],
    "city":["new york ","los angeles","chicago","houston"]

}
df=pd.DataFrame(data)
st.write(df)   

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)

