def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
choice = input("Enter 'C' for Celsius to Fahrenheit or 'F' for Fahrenheit to Celsius: ").upper()

if choice == 'C':
    celsius_temp = float(input("Enter temperature in Celsius: "))
    fahrenheit_result = celsius_to_fahrenheit(celsius_temp)
    print(f"{celsius_temp:.2f}°C is equivalent to {fahrenheit_result:.2f}°F")
elif choice == 'F':
    fahrenheit_temp = float(input("Enter temperature in Fahrenheit: "))
    celsius_result = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"{fahrenheit_temp:.2f}°F is equivalent to {celsius_result:.2f}°C")
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
