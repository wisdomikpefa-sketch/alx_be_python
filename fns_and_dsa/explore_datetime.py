# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print("Current date and time:", formatted_date)

def calculate_future_date():
    try:
        days_to_add = int(input("Enter number of days to add: "))
        current_date = datetime(input("Enter the number of days to add to the current date"))
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print("Future date after", days_to_add, "days:", formatted_future_date)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def main():
    print("\n--- DateTime Exploration ---")
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
