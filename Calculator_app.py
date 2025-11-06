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

if __name__ == "__main__":
    run()
