# Define functions for basic arithmetic operations

def add(x, y):
    """
    Add two numbers.

    Parameters:
    x (float): The first number.
    y (float): The second number.

    Returns:
    float: The sum of x and y.
    """
    return x + y


def subtract(x, y):
    """
    Subtract two numbers.

    Parameters:
    x (float): The first number.
    y (float): The second number.

    Returns:
    float: The difference between x and y.
    """
    return x - y


def multiply(x, y):
    """
    Multiply two numbers.

    Parameters:
    x (float): The first number.
    y (float): The second number.

    Returns:
    float: The product of x and y.
    """
    return x * y


def divide(x, y):
    """
    Divide two numbers.

    Parameters:
    x (float): The first number.
    y (float): The second number.

    Returns:
    float: The quotient of x divided by y.

    Raises:
    ValueError: If y is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


def main():
    """
    Main function to run the basic calculator.
    """
    print("Welcome to the Basic Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4): ")

        # Check if the choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                except ValueError as e:
                    print(e)

            # Ask if the user wants to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break
        else:
            print("Invalid Input. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

