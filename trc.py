from datetime import datetime

prophetic_numbers = [888, 1260, 9999, 144000]

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def check_prophetic_intervals(days):
    return [number for number in prophetic_numbers if days == number]

def calculate_day_interval(date_str):
    try:
        parts = date_str.strip().split("-")
        if len(parts) != 3:
            return None, "Invalid format. Use YYYY-MM-DD."

        year, month, day = map(int, parts)

        if not (1 <= year <= 9999):
            return None, (
                f"⛔️ Year {year} is outside the exact calculable range (1–9999). "
                f"The Revelation Engine cannot calculate unverifiable prophetic intervals. "
                f"Please enter a valid date grounded in precise chronology."
            )

        input_date = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.now()
        delta_days = (today - input_date).days
        return abs(delta_days), None

    except Exception as e:
        return None, f"Error: {e}"
