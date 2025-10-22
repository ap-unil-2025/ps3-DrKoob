"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
   
def temperature_converter():
    temperature = input("Enter the temperature value: ")
    try:
        temperature = float(temperature)
    except ValueError:
            print("Invalid input. Please enter a valid number")
    unit = input('Enter C for Celsius or F for Fahrenheit:')
    if unit == 'C':
        result = celsius_to_fahrenheit(temperature)
    elif unit == 'F':
        result = fahrenheit_to_celsius(temperature)
    else:
        print("Invalid unit. Please enter C or F")
        return
    print(f"The temperature is {result:.2f} {unit}")



    # Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    print("All tests passed!")

    # Run interactive converter
    temperature_converter()
    