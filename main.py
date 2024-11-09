# main.py
from modules.step1 import validate_positive, check_length
from modules.step2 import divide_numbers
from modules.step3 import access_database
from modules.step4 import convert_to_int, access_list_element, process_dict_key
from modules.step5 import safe_division
from modules.step7 import check_positive_number
from modules.step8 import square_root, open_file, multiply_strings

def run_all_functions():
    # Шаг 1
    try:
        validate_positive(-5)
    except ValueError as e:
        print(f"Caught error in validate_positive: {e}")

    try:
        check_length("hi", 5)
    except ValueError as e:
        print(f"Caught error in check_length: {e}")

    # Шаг 2
    divide_numbers(10, 0)

    # Шаг 3
    access_database(-1)

    # Шаг 4
    convert_to_int("abc")
    access_list_element([1, 2, 3], 5)
    process_dict_key({'a': 1}, 'b')

    # Шаг 5
    safe_division(10, "a")

    # Шаг 7
    check_positive_number(-10)

    # Шаг 8
    try:
        square_root(-1)
    except ValueError as e:
        print(f"Caught error in square_root: {e}")

    open_file("non_existent_file.txt")
    try:
        multiply_strings("Hello", "5")
    except TypeError as e:
        print(f"Caught error in multiply_strings: {e}")

if __name__ == "__main__":
    run_all_functions()
