import streamlit as st

st.title("wlcm to basic streamlit app")

age=st.slider("select age", 1,100)
city=st.selectbox("select your city", ["delhi","mumbai","pune","nsk"])

if st.button("show details"):
    st.write("age",age)
    st.write("city",city)










