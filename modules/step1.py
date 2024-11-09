# step1.py
# Функции для шага 1: две функции, которые выбрасывают исключения, без обработки

def validate_positive(number):
    """Raises ValueError if the number is non-positive"""
    if number <= 0:
        raise ValueError("Number must be positive")

def check_length(value, min_length):
    """Raises ValueError if the length of value is less than min_length"""
    if len(value) < min_length:
        raise ValueError("Value length is too short")
