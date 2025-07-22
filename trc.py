# trc.py — Temporal Resonance Core
from datetime import datetime

# Define known prophetic numbers
prophetic_numbers = [888, 1260, 9999, 144000]

def is_palindrome(n):
    """Check if a number is a palindrome (same forward/backward)."""
    return str(n) == str(n)[::-1]

def check_prophetic_intervals(days):
    """Check which prophetic numbers match the given day count."""
    return [number for number in prophetic_numbers if days == number]

def calculate_day_interval(date_str):
    """Calculate how many days since the input date."""
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None, "Invalid date format. Use YYYY-MM-DD."
    
    today = datetime.now()
    delta_days = (today - input_date).days
    return delta_days, None
