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
            yield f"file {os.path.basename(file)} are deleted because {days} days have passed"
        else:
            yield f"file {os.path.basename(file)} have been left because {days} days have not passed"


#  Задание 5
class ConcatenationWords:

    @staticmethod
    def read_file(file_name: str) -> List[str]:
        """
        Read file from directory.
        :return:
        """
        with open(file_name, "r") as file:
            return file.read().splitlines()

    @staticmethod
    def sort_dict_by_keys(dict_index_letters: dict) -> str:
        """
        Sort dictionary by keys.
        :param dict_index_letters: Dictionary with
        :return:
        """
        sorted_list: list = sorted(dict_index_letters.items())
        sorted_dict: dict = {}
        for key, value in sorted_list:
            sorted_dict[key] = value
        return "".join(sorted_dict.values())

    @staticmethod
    def find_same_letters_right_order(input_word: str, word: str, dict_index_letters: dict) -> None:
        """
        We find the same letters from right to left.
        :param input_word: Input word.
        :param word: Current word in list.
        :param dict_index_letters:
        :return:
        """
        word_copy: str = word
        reverse_input_word: str = input_word[::-1]
        for i, letter in enumerate(reverse_input_word, start=1):
            indexes: list = [n for n, x in enumerate(word) if x == letter]
            letter_next: str = reverse_input_word[i] if len(reverse_input_word) > i else None
            for index in indexes:
                if not dict_index_letters and word[index - 1] == letter_next:
                    word_copy = word_copy[:index] + word_copy[index + 1:]
                    dict_index_letters[index] = letter
                elif index + 1 in dict_index_letters:
                    word_copy = word_copy[:index] + word_copy[index + 1:]
                    dict_index_letters[index] = letter

    def concatenate_words(self, words: List[str]) -> list:
        """
        Read file and concatenate the words by the same letters in the right order.
        :param words:
        :return:
        """
        concat_words: list = []
        input_word: str = input("Введите любое слово из файла task5.txt: \n<<< ")
        for word in words:
            if word == input_word:
                continue
            dict_index_letters: dict = {}
            self.find_same_letters_right_order(input_word, word, dict_index_letters)
            str_same_letters: str = self.sort_dict_by_keys(dict_index_letters)
            if len(dict_index_letters) > 1 and input_word.endswith(str_same_letters) \
                    and word.startswith(str_same_letters):
                concat_words.append(input_word.replace(str_same_letters, '') + word)
        return concat_words


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
    concatenation_words: ConcatenationWords = ConcatenationWords()
    list_words: List[str] = concatenation_words.read_file("task5.txt")
    print(concatenation_words.concatenate_words(list_words))  # Задание 5
