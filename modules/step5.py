# step5.py
# Функция для шага 5: выбрасывает исключения и содержит все необходимые обработчики

def safe_division(a, b):
    """Raises exceptions for invalid division and handles them, including finally block"""
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numeric")
        return a / b
    except ZeroDivisionError as zde:
        print(f"Division error: {zde}")
    except TypeError as te:
        print(f"Type error: {te}")
    finally:
        print("Finished attempting division.")
