import re

def qa_is_correct(answer: str, key: str, normalize: bool = True) -> bool:
    """
    Compares two values, `answer` and `key`, ensuring that `answer` contains only integers
    (with or without commas) and that the last integer in `answer` matches `key`.

    Args:
        answer (str): A string to be compared with `key`.
        key (int): An integer to compare with the last number in `answer`.
        normalize (bool): If True, then normalize answer and key. Defaults to True.

    Returns:
        bool: True if the last integer in `answer` matches `key`, else False.
    """
    if answer is None:
        return False

    return compare_last_number(answer, key)

def normalize_number_string(number_str: str) -> int:
    """
    Normalizes a number string by removing commas and trailing '.0's, then converting to int.

    Args:
        number_str (str): A string representing a number, possibly with commas and trailing '.0's.

    Returns:
        int: The normalized integer value of the number string.

    Raises:
        ValueError: If the number has a decimal part with non-zero digits.
    """
    # Remove commas
    number_str = number_str.replace(',', '')

    # Check for decimal point
    if '.' in number_str:
        integer_part, decimal_part = number_str.split('.', 1)
        # If decimal part is all zeros, ignore it
        if set(decimal_part) == {'0'}:
            number_str = integer_part
        
        else:
            return None

    return int(number_str)

def compare_last_number(answer: str, key: str) -> bool:
    """
    Extracts the last number (integer) from the answer and compares it with the key.

    Args:
        answer (str): A string from which to extract and compare the last number.
        key (int): An integer to compare with the last number in the answer.

    Returns:
        bool: True if the last number in `answer` matches the key, else False.
    """
    # Check if there is any floating point number in the answer, if so return False

    # Match integers with or without commas
    answer_numbers = re.findall(r'[0-9.,]+', answer)
    # If no numbers found in `answer`, return False
    if not answer_numbers:
        return False

    # Normalize the last number in `answer` and compare with the key
    last_number = normalize_number_string(answer_numbers[-1])

    # Compare the last number with key
    return last_number == int(key)
