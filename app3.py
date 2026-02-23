import streamlit as st

st.title("Basic Calculator")


num1 = st.number_input("Enter your 1st number", step=1, format="%d")
num2 = st.number_input("Enter your 2nd number", step=1, format="%d")

op = st.selectbox("Choose operation", ["add", "sub", "mult", "div"])

if st.button("Calculate"):

    num1 = int(num1)
    num2 = int(num2)

    if op == "add":
        st.write("Result:", num1 + num2)

    elif op == "sub":
        st.write("Result:", num1 - num2)

    elif op == "mult":
        st.write("Result:", num1 * num2)

    elif op == "div":
        if num2 != 0:
            st.write("Result:", num1 // num2)   # integer division
        else:
            st.write("Cannot divide by zero")