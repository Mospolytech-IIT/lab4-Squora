# step8.py
# Три функции, демонстрирующие работу исключений

def square_root(number):
    """Calculates the square root, raises ValueError if number is negative"""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return number ** 0.5

def open_file(filename):
    """Attempts to open a file, raises FileNotFoundError if file doesn't exist"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        print(f"File error: {e}")
        return None

def multiply_strings(string, times):
    """Multiplies a string, raises TypeError if times is not an integer"""
    if not isinstance(times, int):
        raise TypeError("Times must be an integer")
    return string * times
