# Scientific Calculator Steamlit App

## Overview
This project is a **Scientific Calculator** web application built using **Streamlit** and **Python**. The app allows users to perform both basic arithmetic operations and advanced scientific calculations in an interactive and user-friendly interface. 

The project is structured to separate the logic (Python functions) from the user interface (Streamlit app), making the code easier to maintain and extend.

## Features

### 1. Basic Calculations:
- **Addition**
- **Subtraction**
- **Multiplication**
- **Division**
- **Percentage**

### 2. Scientific Calculations:
- **Square Root**
- **Power**
- **Logarithm**
- **Exponential**
- **Factorial**
- **Trigonometric Functions:** `Sin`, `Cos`, `Tan`

### 3. Interactive User Interface:
- The home page greets users with a welcome message and image.
- Users can select between "Basic Calculation" and "Scientific Calculation" modes.
- Real-time input with a result displayed immediately after calculation.
- Includes a **spinner** to show a waiting time when performing calculations.

### 4. Navigation:
- A **Back to Home** button is available on both calculation pages to navigate back to the home screen.

## Folder Structure

streamlit_calculator/ │ 
├── app.py # Streamlit code for the user interface ├── calculations.py # Python functions for basic and scientific calculations ├── images/ │ └── welcome_image.png # Image used on the welcome page └── README.md # Project description and setup instructions


## Installation and Setup

### Prerequisites
- **Python 3.7+** installed on your machine.
- Install required Python libraries:
  - `streamlit`
  - `math` (part of Python Standard Library)
- You can install the required packages using pip:
    ```bash
    pip install streamlit

## How to Run the App

1. Clone or download the repository.
    ```bash
   git clone https://github.com/neeluvickey/streamlit.git
2. Navigate to the project folder:
    ```bash
   cd scientific_calculator_app
3. Run the app with Streamlit:
   ```bash
   streamlit run app.py
4. The app will launch in your default web browser. If it doesn't, open your browser and go to:
    ```bash
   http://localhost:8501

## Usage

- When the app starts, you will be greeted with a welcome page that allows you to choose between Basic Calculation or Scientific Calculation.
- After selecting the calculator type, you can perform the desired operations:
  - Basic Calculation: Enter two numbers and select from addition, subtraction, multiplication, division, or percentage.
  - Scientific Calculation: Choose operations like square root, power, trigonometric functions, and logarithm, and provide the required input(s).
- You can navigate back to the home page at any time by clicking the Back to Home button on the calculator pages.

## File Breakdown

- `app.py`: Handles the Streamlit user interface and navigation logic.
- `calculations.py`: Contains the Python logic for performing basic and scientific calculations.
- `images/`: Contains the image assets used in the app (e.g., welcome page image).

## Dependencies
- `Streamlit`: The framework used to build the user interface.
- `math`: Python's built-in math module for scientific functions.
- To install the required dependencies, make sure to run:
    ```bash
    pip install streamlit

## Future Enhancements
- Add more scientific operations like inverse trigonometric functions.
- Implement a more advanced UI design.
- Support for history of calculations.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


## Conclusion:
This format ensures clarity and ease of use for anyone looking at your project. Let me know if you need any adjustments or additional sections!

