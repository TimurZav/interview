import os
import glob
import pprint
import pandas as pd
from pandas import DataFrame
from typing import List, Dict
from datetime import datetime, timedelta


#  Задание 1
def save_unique_data():
    df: DataFrame = pd.read_csv("task1.csv")
    df.drop_duplicates(inplace=True)
    df.to_csv("task1_without_dupl.csv", index=False)
    return "Unique data is written to a file."


#  Задание 2
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


#  Задание 3
def get_list_dict_digits(matrix: List[List[int]]):
    list_dict_digits: List[Dict[str, int]] = []
    for list_digits in matrix:
        dict_digits = {f"k{digit}": digit for digit in list_digits}
        list_dict_digits.append(dict_digits)
    return list_dict_digits


#  Задание 4
def remove_file_by_date(days):
    for file in glob.glob("dir_files/*"):
        creation_day_file: datetime = datetime.fromtimestamp(os.stat(file).st_ctime)
        if datetime.now() - creation_day_file > timedelta(days=days):
            os.remove(file)
            yield f"file {os.path.basename(file)} are deleted because N days have passed"
        else:
            yield f"file {os.path.basename(file)} have been left because N days have not passed"


#  Задание 5
class ConcatenationWords:
    def __init__(self):
        self.input_word: str = input("Введите любое слово из файла task5.txt: ")

    def concatenate_words(self) -> list:
        """
        Read file and concatenate the words by the same letters in the right order.
        :return:
        """
        with open("task5.txt", "r") as file:
            words: List[str] = file.read().splitlines()
        concat_words: list = []
        for word in words:
            if word == self.input_word:
                continue
            list_letters: list = []
            self.find_same_letters_right_order(word, list_letters)
            if len(list_letters) > 1:
                is_suit = [letter == self.input_word[-i] for i, letter in enumerate(reversed(list_letters), 1)]
                concat_words.append(self.input_word.replace(''.join(list_letters), '') + word) if all(is_suit) else None
        return concat_words

    def find_same_letters_right_order(self, word: str, list_letters: list) -> None:
        """
        We find the same letters from right to left.
        :param word: Current word in list.
        :param list_letters: A list with matching letters.
        :return:
        """
        for letter in self.input_word[::-1]:
            if letter in word:
                indexes: list = [n for n, x in enumerate(word) if x == letter]
                for index in indexes:
                    if not list_letters:
                        list_letters.insert(0, letter)
                    elif index + 1 in [n for n, x in enumerate(word) if x == list_letters[0]]:
                        list_letters.insert(0, letter)


if __name__ == "__main__":
    print("Задание 1")
    print(save_unique_data())  # Задание 1
    print("\nЗадание 2")
    pprint.pprint(calculate([{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]))  # Задание 2
    print("\nЗадание 3")
    pprint.pprint(get_list_dict_digits([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Задание 3
    print("\nЗадание 4")
    pprint.pprint(list(remove_file_by_date(1)))  # Задание 4
    print("\nЗадание 5")
    print(ConcatenationWords().concatenate_words())  # Задание 5
