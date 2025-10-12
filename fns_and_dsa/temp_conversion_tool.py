# temp_conversion_tool.py
#fahrenheit_to_celsius_factor
#celsius_to_fahrenheit_factor

# Global conversion factors
FAHRENHEIT_OFFSET = 32
FAHRENHEIT_SCALE = 9 / 5
CELSIUS_SCALE = 5 / 9

def celsius_to_fahrenheit_factor(celsius):
    """Convert Celsius to Fahrenheit using global variables."""
    return (celsius * FAHRENHEIT_SCALE) + FAHRENHEIT_OFFSET

def fahrenheit_to_celsius_factor(fahrenheit):
    """Convert Fahrenheit to Celsius using global variables."""
    return (fahrenheit - FAHRENHEIT_OFFSET) * CELSIUS_SCALE

def main():
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit_factor(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif choice == "2":
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius_factor(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main() 
