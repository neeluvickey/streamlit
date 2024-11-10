# Import statements
import streamlit as st
import time
from calculations import basic_calculation, scientific_calculation

# Home Page or Welcome Page
if 'page' not in st.session_state:
    st.session_state.page = 1

if st.session_state.page == 1:
    st.title("Welcome to the Scientific Calculator App!")
    st.image(r"C:\Neelu\vscode\streamlit\scientific_calculator_app\images\equation.jpg",
             caption="Scientific Calculator")
    st.write("Choose between Basic or Scientific Calculations.")

    # Button to choose between basic and scientific calculations
    calculation_type = st.radio("Select Calculator Type", ["Basic Calculation", "Scientific Calculation"])

    # Button to navigate to the next page based on the selected calculator type
    if st.button('Next'):
        if calculation_type == "Basic Calculation":
            st.session_state.page = 2
        else:
            st.session_state.page = 3

# Basic Calculator Page
elif st.session_state.page == 2:
    st.title("Basic Calculator")

    # User inputs for basic calculations
    operation = st.selectbox("Choose an operation",
                             ["Addition", "Subtraction", "Multiplication", "Division", "Percentage"])
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")

    # Spinner and calculation for basic operations
    if st.button('Calculate'):
        with st.spinner("Calculating..."):
            time.sleep(1)  # Simulate some delay
            result = basic_calculation(operation, num1, num2)
            st.success(f"The result is: {result}")

    # Back button to return to the home page
    if st.button('Back to Home'):
        st.session_state.page = 1

# Scientific Calculator Page
elif st.session_state.page == 3:
    st.title("Scientific Calculator")

    # User inputs for scientific calculations
    operation = st.selectbox("Choose an operation",
                             ["Square Root", "Power", "Logarithm", "Exponential", "Factorial", "Sin", "Cos", "Tan"])
    num1 = st.number_input("Enter the number:")

    num2 = None
    if operation == "Power":
        num2 = st.number_input("Enter the second number:")

    # Spinner and calculation for scientific operations
    if st.button('Calculate'):
        with st.spinner("Calculating..."):
            time.sleep(1)  # Simulate some delay
            result = scientific_calculation(operation, num1, num2)
            st.success(f"The result is: {result}")

    # Back button to return to the home page
    if st.button('Back to Home'):
        st.session_state.page = 1
