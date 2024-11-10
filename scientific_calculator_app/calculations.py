# calculations.py
import math


# Define functions for basic calculations
def basic_calculation(operation: str, num1: float, num2: float) -> any:
    """
    Performs basic arithmetic operations.

    Params:
        operation (str): The operation to perform (Addition, Subtraction, Multiplication, Division, Percentage).
        num1 (float): The first number.
        num2 (float): The second number.

    Return Type:
        float: The result of the calculation, or a string indicating an error.
    """
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    elif operation == "Percentage":
        return (num1 / num2) * 100 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"


# Define functions for scientific calculations
def scientific_calculation(operation: str, num1: float, num2: float = None) -> any:
    """
    Performs scientific calculations.

    Params:
        operation (str): The scientific operation to perform (Square Root, Power, Logarithm, Exponential, Factorial,
                         Sin, Cos, Tan).
        num1 (float): The first number.
        num2 (float, optional): The second number (needed for Power operation).

    Return Type:
        float: The result of the calculation, or a string indicating an error.
    """
    if operation == "Square Root":
        return math.sqrt(num1)
    elif operation == "Power":
        return math.pow(num1, num2)
    elif operation == "Logarithm":
        return math.log(num1)
    elif operation == "Exponential":
        return math.exp(num1)
    elif operation == "Factorial":
        return math.factorial(int(num1))  # Factorial only works for integers
    elif operation == "Sin":
        return math.sin(num1)
    elif operation == "Cos":
        return math.cos(num1)
    elif operation == "Tan":
        return math.tan(num1)
    else:
        return "Invalid operation"
