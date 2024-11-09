# step7.py
# Функция для шага 7: выбрасывает пользовательское исключение и содержит обработчик

from .custom_exceptions import NegativeNumberError

def check_positive_number(number):
    """Raises NegativeNumberError if number is negative, with an exception handler"""
    try:
        if number < 0:
            raise NegativeNumberError("Number cannot be negative")
    except NegativeNumberError as e:
        print(f"Caught a custom exception: {e}")
