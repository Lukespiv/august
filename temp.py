def celsius_to_fahrenheit(celsius):
    """given a celsius value returne the conversation"""
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} celsius to fahrenhiet is {fahrenheit}")