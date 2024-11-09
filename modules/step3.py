# step3.py
# Функция для шага 3: выбрасывает исключение, содержит обработчик и блок finally

def access_database(record_id):
    """Simulates accessing a database. Raises ValueError if record_id is invalid"""
    try:
        if record_id < 0:
            raise ValueError("Record ID must be non-negative")
        # Simulated access logic
        print(f"Accessing record with ID: {record_id}")
        return f"Record {record_id}"
    except Exception as e:
        print(f"Exception in access_database: {e}")
    finally:
        print("Closing database connection.")
