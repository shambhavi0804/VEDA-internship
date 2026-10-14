import os
from pathlib import Path


def is_valid_number(value):
    """Check whether a value can be converted to a number."""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def is_valid_email(email):
    """Perform a simple email validation."""
    if not isinstance(email, str):
        return False

    return "@" in email and "." in email.split("@")[-1]


def validate_positive_number(value):
    """Check whether a number is greater than zero."""
    try:
        return float(value) > 0
    except (ValueError, TypeError):
        return False


def format_currency(amount):
    """Format a number as Indian Rupees."""
    try:
        return f"₹{float(amount):,.2f}"
    except (ValueError, TypeError):
        return "Invalid amount"


def format_percentage(value):
    """Format a value as a percentage."""
    try:
        return f"{float(value):.2f}%"
    except (ValueError, TypeError):
        return "Invalid percentage"


def calculate_sum(a, b):
    """Return the sum of two numbers."""
    return float(a) + float(b)


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def check_file_exists(file_path):
    """Check whether a file exists."""
    return Path(file_path).is_file()


def get_file_size(file_path):
    """Return file size in bytes."""
    if not check_file_exists(file_path):
        return None

    return os.path.getsize(file_path)