def celsius_to_fahrenheit(celsius):
    """given a celsius value returne the conversation"""
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """given a fahrenheit value returne the converted value"""
    fahrenheit = 82
    celsius = (fahrenheit - 32) * 5/9
    return celsius

celsius = 25

fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} celsius to fahrenhiet is {fahrenheit}")

celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} fahrenhiet to celsius is {celsius}")