# Simple Streamlit Calculator 🔢

A simple and interactive calculator application built using *Streamlit*.  
This app allows users to perform basic arithmetic operations such as *Addition, Subtraction, Multiplication, and Division*.

---

## 🚀 Features
- Add two numbers  
- Subtract two numbers  
- Multiply two numbers  
- Divide two numbers (with zero-division safety)  
- Clean and user-friendly Streamlit interface  

---

## 📦 Requirements
Make sure you have Streamlit installed:

---

## ▶ How to Run the App

Open your terminal and run:

---

## 🧠 Code Overview

```python
import streamlit as st

def run():
    st.title("Simple Calculator 🔢")

    st.write("Perform basic arithmetic operations easily!")

    # Input fields
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    # Operation selection
    operation = st.selectbox(
        "Choose an operation",
        ("Add", "Subtract", "Multiply", "Divide")
    )

    # Calculate when user clicks button
    if st.button("Calculate"):
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Cannot divide by zero!")
                result = None

        if result is not None:
            st.success(f"Result: {result}")

