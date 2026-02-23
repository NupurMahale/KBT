import streamlit as st
st.title("helloo ,  gn")

name=st.text_input("enter name")

if st.button("submit"):
    st.write("hello ", name)