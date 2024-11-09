# step2.py
# Функция для шага 2: выбрасывает исключение и содержит один обработчик Exception

def divide_numbers(a, b):
    """Raises ZeroDivisionError if b is zero and handles it"""
    try:
        return a / b
    except Exception as e:
        print(f"Error in divide_numbers: {e}")
        return None
