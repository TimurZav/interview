import pprint


def calculate(list_digits: list):
    count_digits: int = sum(len(dict_digits) for dict_digits in list_digits)
    sum_digits: int = sum(sum(dict_digits) for dict_digits in list_digits)
    average_digits: float = sum_digits / count_digits

    digits: list = []
    for dict_digits in list_digits:
        digits.extend(iter(dict_digits))
    tuple_digits: tuple = tuple(digits)

    return {
        "count_digits": count_digits,
        "sum_digits": sum_digits,
        "average_digits": average_digits,
        "tuple_digits": tuple_digits
    }


if __name__ == "__main__":
    pprint.pprint(calculate([{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]))
