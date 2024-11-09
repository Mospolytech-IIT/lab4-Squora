# custom_exceptions.py
# Шаг 6: три пользовательских исключения

class NegativeNumberError(Exception):
    """Exception for negative number input"""
    pass

class InvalidNameError(Exception):
    """Exception for invalid name input"""
    pass

class OutOfRangeError(Exception):
    """Exception for input out of allowed range"""
    pass
