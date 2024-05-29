def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5 / 9


def main():
    """
    Main function to run the temperature converter.
    """
    print("Welcome to the Temperature Converter!")
    print("Select the conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2): ")

        if choice in ('1', '2'):
            try:
                temperature = float(input("Enter the temperature to convert: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                converted = celsius_to_fahrenheit(temperature)
                print(f"{temperature}°C is equal to {converted:.2f}°F")
            elif choice == '2':
                converted = fahrenheit_to_celsius(temperature)
                print(f"{temperature}°F is equal to {converted:.2f}°C")

            # Ask if the user wants to perform another conversion
            next_conversion = input("Do you want to perform another conversion? (yes/no): ")
            if next_conversion.lower() != 'yes':
                break
        else:
            print("Invalid Input. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
