from typing import List, Dict


def get_list_dict_digits(matrix: List[List[int]]):
    list_dict_digits: List[Dict[str, int]] = []
    for list_digits in matrix:
        dict_digits = {f"k{digit}": digit for digit in list_digits}
        list_dict_digits.append(dict_digits)
    return list_dict_digits


if __name__ == "__main__":
    get_list_dict_digits([[1, 2, 3], [4, 5, 6]])
