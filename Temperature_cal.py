def celsius_to_fahrenheit():
    celcius = float(input("Enter a temperature in celcius: "))
    fahrenheit = (celcius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit}")

def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"Temperature in Celsius: {celsius:.2f}\u00b0C")

def temp_cal():
    print("Welcome to the Temperature Calculator ")
    flag = 0
    while flag != 3:
        print("--------------------------------------------------")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        choice = input("Enter your choice (1, 2 or 3): ")
        if choice not in ['1', '2', '3']:
            print("Invalid choice. Please enter 1, 2, 3.")
            return
        if choice == '1':
            celsius_to_fahrenheit()
            print("--------------------------------------------------")
        if choice == '2':
            fahrenheit_to_celsius()
            print("--------------------------------------------------")
        if choice == '3':
            print("Thank you for using the Temperature Calculator. Goodbye!")
            flag = 3
temp_cal()
    