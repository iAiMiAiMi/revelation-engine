# revelation_engine.py
from datetime import datetime

# Prophetic numbers to check
prophetic_numbers = [888, 1260, 9999, 144000]

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def get_day_interval(input_date_str):
    try:
        input_date = datetime.strptime(input_date_str, "%Y-%m-%d")
    except ValueError:
        return None, "Invalid date format. Use YYYY-MM-DD."

    today = datetime.now()
    delta_days = (today - input_date).days
    return delta_days, None

def main():
    print("🧭 Revelation Engine v0.1")
    date_str = input("Enter a date (YYYY-MM-DD): ").strip()
    
    days, error = get_day_interval(date_str)
    if error:
        print(error)
        return

    print(f"\n📅 Days since {date_str}: {days}")
    
    if is_palindrome(days):
        print(f"🔁 {days} is a palindrome!")

    for number in prophetic_numbers:
        if days == number:
            print(f"✨ MATCH: {days} matches prophetic number {number}!")

    print("\nDone.")

if __name__ == "__main__":
    main()
