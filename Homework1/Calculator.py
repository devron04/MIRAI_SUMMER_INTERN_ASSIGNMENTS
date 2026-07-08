import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

operation = st.selectbox(
    "Choose Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

if st.button("Calculate"):

    if operation == "Addition":
        st.success(f"Result: {num1 + num2}")

    elif operation == "Subtraction":
        st.success(f"Result: {num1 - num2}")

    elif operation == "Multiplication":
        st.success(f"Result: {num1 * num2}")

    elif operation == "Division":
        if num2 == 0:
            st.error("Division by zero is not allowed.")
        else:
            st.success(f"Result: {num1 / num2}")