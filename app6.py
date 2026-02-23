
import streamlit as st

st.title(" Form")

with st.form("form"):

    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", step=1, format="%d")
    gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])
    
    submit = st.form_submit_button("Submit")


if submit:
    st.write("Form Submitted Successfully!")
    st.write("Name:", name)
    st.write("Age:", int(age))
    st.write("Gender:", gender)