import streamlit as st
from utils import (
    is_valid_number,
    is_valid_email,
    validate_positive_number,
    format_currency,
    format_percentage,
    calculate_sum,
    calculate_average,
    check_file_exists,
    get_file_size
)


st.set_page_config(
    page_title="Python Utility Module",
    page_icon="🛠️",
    layout="wide"
)


st.title("🛠️ Python Utility Module")
st.write(
    "An interactive Streamlit application demonstrating "
    "reusable Python utility functions."
)

st.divider()


# --------------------------------------------------
# NUMBER VALIDATION
# --------------------------------------------------

st.header("🔢 Number Validation")

number_input = st.text_input(
    "Enter a number",
    placeholder="Example: 2500"
)

if st.button("Validate Number"):
    if is_valid_number(number_input):
        st.success("✅ Valid number")
    else:
        st.error("❌ Invalid number")


# --------------------------------------------------
# POSITIVE NUMBER VALIDATION
# --------------------------------------------------

st.header("➕ Positive Number Validation")

positive_number = st.number_input(
    "Enter a value",
    value=100.0
)

if validate_positive_number(positive_number):
    st.success("✅ The number is positive.")
else:
    st.warning("⚠️ The number must be greater than zero.")


# --------------------------------------------------
# EMAIL VALIDATION
# --------------------------------------------------

st.header("📧 Email Validation")

email = st.text_input(
    "Enter email address",
    placeholder="example@gmail.com"
)

if st.button("Validate Email"):
    if is_valid_email(email):
        st.success("✅ Valid email address")
    else:
        st.error("❌ Invalid email address")


# --------------------------------------------------
# CURRENCY FORMATTER
# --------------------------------------------------

st.header("💰 Currency Formatter")

amount = st.number_input(
    "Enter amount",
    min_value=0.0,
    value=5000.0
)

st.info(f"Formatted Amount: **{format_currency(amount)}**")


# --------------------------------------------------
# PERCENTAGE FORMATTER
# --------------------------------------------------

st.header("📊 Percentage Formatter")

percentage = st.number_input(
    "Enter percentage",
    min_value=0.0,
    max_value=100.0,
    value=75.5
)

st.info(f"Formatted Percentage: **{format_percentage(percentage)}**")


# --------------------------------------------------
# CALCULATIONS
# --------------------------------------------------

st.header("🧮 Calculation Utilities")

col1, col2 = st.columns(2)

with col1:
    first_number = st.number_input(
        "First Number",
        value=10.0
    )

with col2:
    second_number = st.number_input(
        "Second Number",
        value=20.0
    )

if st.button("Calculate Sum"):
    result = calculate_sum(first_number, second_number)
    st.success(f"Result: {result}")


# --------------------------------------------------
# AVERAGE CALCULATOR
# --------------------------------------------------

st.header("📈 Average Calculator")

numbers_text = st.text_input(
    "Enter numbers separated by commas",
    placeholder="10, 20, 30, 40, 50"
)

if st.button("Calculate Average"):

    try:
        numbers = [
            float(value.strip())
            for value in numbers_text.split(",")
            if value.strip()
        ]

        if numbers:
            average = calculate_average(numbers)
            st.success(f"Average: {average:.2f}")
        else:
            st.warning("Please enter at least one number.")

    except ValueError:
        st.error("Please enter valid numeric values.")


# --------------------------------------------------
# FILE UTILITIES
# --------------------------------------------------

st.header("📁 File Utilities")

file_path = st.text_input(
    "Enter file path",
    placeholder="Example: C:/Users/YourName/Desktop/test.txt"
)

if st.button("Check File"):

    if not file_path:
        st.warning("Please enter a file path.")

    elif check_file_exists(file_path):

        size = get_file_size(file_path)

        st.success("✅ File exists.")
        st.write(f"File size: **{size} bytes**")

    else:
        st.error("❌ File does not exist.")


# --------------------------------------------------
# FUNCTION DOCUMENTATION
# --------------------------------------------------

st.divider()

st.header("📚 Available Utility Functions")

functions = {
    "is_valid_number()": "Validates numeric input.",
    "is_valid_email()": "Performs basic email validation.",
    "validate_positive_number()": "Checks whether a number is positive.",
    "format_currency()": "Formats values as Indian currency.",
    "format_percentage()": "Formats values as percentages.",
    "calculate_sum()": "Adds two numbers.",
    "calculate_average()": "Calculates the average of numbers.",
    "check_file_exists()": "Checks whether a file exists.",
    "get_file_size()": "Returns the file size in bytes."
}

for function_name, description in functions.items():
    st.write(f"**{function_name}** — {description}")


st.divider()

st.caption("VEDA Internship | Python Programming Track | Day 25")