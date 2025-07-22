# revelation_engine.py
from trc import calculate_day_interval, is_palindrome, check_prophetic_intervals

def main():
    print("🧭 Revelation Engine v0.1")
    date_str = input("Enter a date (YYYY-MM-DD): ").strip()

    days, error = calculate_day_interval(date_str)
    if error:
        print(error)
        return

    print(f"\n📅 Days since {date_str}: {days}")

    if is_palindrome(days):
        print(f"🔁 {days} is a palindrome!")

    matches = check_prophetic_intervals(days)
    for match in matches:
        print(f"✨ MATCH: {days} matches prophetic number {match}!")

    print("\nDone.")

if __name__ == "__main__":
    main()
