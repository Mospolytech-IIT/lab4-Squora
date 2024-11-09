# step4.py
# Функции для шага 4: три функции с разными типами исключений и несколькими обработчиками

def convert_to_int(value):
    """Converts value to int, handling TypeError, ValueError, and OverflowError"""
    try:
        return int(value)
    except TypeError:
        print("Cannot convert non-numeric type to int.")
    except ValueError:
        print("Cannot convert non-numeric string to int.")
    except OverflowError:
        print("Number is too large to convert to int.")

def access_list_element(lst, index):
    """Accesses an element in the list by index, handling IndexError and TypeError"""
    try:
        return lst[index]
    except IndexError:
        print("Index out of range.")
    except TypeError:
        print("List and index must be of correct types.")

def process_dict_key(dictionary, key):
    """Accesses a dictionary key, handling KeyError and TypeError"""
    try:
        return dictionary[key]
    except KeyError:
        print("Key not found in dictionary.")
    except TypeError:
        print("Provided argument is not a dictionary or key is not hashable.")
