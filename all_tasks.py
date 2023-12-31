import copy
import os
import glob
import pprint
import pandas as pd
from pandas import DataFrame
from typing import List, Dict, Tuple
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
    def find_same_letters_and_indexes(input_word: str, word: str) -> Dict[int, str]:
        """
        We find the same letters from right to left.
        :param input_word: Input word.
        :param word: Current word in list.
        :return: Index of letter.
        """
        word_copy: str = word
        dict_index_letters: Dict[int, str] = {}
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
        return dict_index_letters

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
            dict_index_letters: Dict[int, str] = self.find_same_letters_and_indexes(input_word, word)
            str_same_letters: str = self.sort_dict_by_keys(dict_index_letters)
            if len(dict_index_letters) > 1 and input_word.endswith(str_same_letters) \
                    and word.startswith(str_same_letters):
                concat_words.append(input_word.replace(str_same_letters, '') + word)
        return concat_words


#  Задание 5. Другое решение
class ConcatenationWordsTwo:

    @staticmethod
    def read_file(file_name: str) -> List[str]:
        """
        Read file from directory.
        :param file_name: Name of file with words.
        :return: List of words.
        """
        with open(file_name, "r") as file:
            return file.read().splitlines()

    @staticmethod
    def convert_words_to_dicts(words: List[str]) -> dict:
        """
        Converting words in the dictionary from letters. For example,
            Content of file
            кабала
            карась
            ->
            'к': {'а': {'б': {'а': {'л': {'а': {}}}}, '': {}, 'р': {'а': {'с': {'ь': {}}}}}}
        :param words: Words from file.
        :return: A dictionary where the keys are letters.
        """
        dict_nested_letters: dict = {}
        for word in words:
            current_dict: dict = dict_nested_letters
            list_same_and_words: list = []
            for letter in word:
                if letter not in current_dict:
                    if list_same_and_words and all(list_same_and_words):
                        current_dict[''] = {}
                    current_dict[letter] = {}
                    list_same_and_words.append(False)
                current_dict = current_dict[letter]
                list_same_and_words.append(True)
        return dict_nested_letters

    @staticmethod
    def get_list_letters_from_dict(dict_nested_letters: dict) -> List[List[str]]:
        """
        We get a list of letters from the dictionary. For example,
            {'к': {'': {}, 'о': {'в': {'к': {'а': {}}}}}} -> [['к'], ['к', 'о', 'в', 'к', 'а']].
        :param dict_nested_letters: A dictionary where the keys are letters.
        :return: А list with letters for later connection and deletion.
        """
        all_letters: List[List[str]] = []
        letters: List[str] = []
        while dict_nested_letters:
            letter: str = next(iter(dict_nested_letters.keys()))
            if letter:
                letters.append(letter)
                dict_nested_letters = dict_nested_letters[letter]
            else:
                dict_nested_letters.pop(letter)
                all_letters.append(letters.copy())
        all_letters.append(letters)
        return all_letters

    @staticmethod
    def merge_list_and_dict(same_letters: list, current_dict: dict) -> dict:
        """
        Combines the list and dictionary into a single dictionary.
        For example,
            ['с', 'т', 'ы'] AND {'к': {'о': {'в': {'к': {'а': {}}}}}}
            -> {'с': {'т': {'ы': {'к': {'о': {'в': {'к': {'а': {}}}}}}}}}.
        :param same_letters: Same letters.
        :param current_dict: A dictionary where the keys are letters.
        :return: Combines the dictionary. For example, {'с': {'т': {'ы': {'к': {'о': {'в': {'к': {'а': {}}}}}}}}}.
        """
        for letter in same_letters:
            if letter not in current_dict:
                current_dict[letter] = {}
            current_dict = current_dict[letter]
        return current_dict

    def get_dict_with_letters(self, same_letters: list, dict_nested_letters: dict) -> dict:
        """
        Getting a dictionary with letters to delete it.
        :param same_letters: Same letters.
        :param dict_nested_letters: A dictionary where the keys are letters.
        :return: Combines the dictionary. For example, {'с': {'т': {'ы': {'к': {'о': {'в': {'к': {'а': {}}}}}}}}}.
        """
        result_dict: dict = {}
        current_dict: dict = result_dict

        current_dict = self.merge_list_and_dict(same_letters, current_dict)
        for same_letters in self.get_list_letters_from_dict(dict_nested_letters):
            current_dict = self.merge_list_and_dict(same_letters, current_dict)

        return result_dict

    def remove_keys_in_order(self, dict_nested_letters: dict, same_letters: list) -> dict:
        """
        This method is needed to remove the appropriate keys (letters) for later adding them to the results list.
        :param dict_nested_letters: A dictionary where the keys are letters.
        :param same_letters: Same letters.
        :return: Dictionary with deleted letters, since this word was included in the results list.
        """
        if not same_letters:
            return dict_nested_letters
        key: str = same_letters.pop(0)
        if key in dict_nested_letters:
            dict_nested_letters[key] = self.remove_keys_in_order(dict_nested_letters[key], same_letters)
            if not dict_nested_letters[key]:
                del dict_nested_letters[key]
        return dict_nested_letters
    
    @staticmethod
    def find_same_letters(input_word: str, dict_nested_letters: dict) -> Tuple[list, dict]:
        """
        This method finds the same letters from the entered word in the dictionary with letters.
        For example, лаСТЫ -> {'к': {'': {}, 'о': {'в': {'к': {'а': {}}}}}}, where same letters is ['с', 'т', 'ы'].
        :param input_word: The word entered by the user.
        :param dict_nested_letters: A dictionary where the keys are letters.
        :return: Same letters in list and remains letters in dict.
        For example,
            ['с', 'т', 'ы'] AND {'к': {'': {}, 'о': {'в': {'к': {'а': {}}}}}},
            that formed words ['стык', 'стыковка'].
        """
        current_dict: dict = dict_nested_letters
        same_letters: List[str] = []
        for letter in input_word:
            if letter in current_dict:
                current_dict = current_dict[letter]
                same_letters.append(letter)
            else:
                current_dict = dict_nested_letters
                same_letters = []
                if letter in dict_nested_letters:
                    current_dict = current_dict[letter]
                    same_letters.append(letter)
        return same_letters, current_dict

    def main(self, input_word: str, results: list, dict_nested_letters: dict) -> None:
        """
        The main method that runs the code.
        :param input_word: The word entered by the user.
        :param results: Suitable words are added here. For example, ласты -> ['ластык', 'ластыковка'].
        :param dict_nested_letters: A dictionary where the keys are letters.
        For example, {'л': {'а': {'с': {'т': {'ы': {}}}}}}.
        :return:
        """
        dict_nested_letters: dict = copy.deepcopy(dict_nested_letters)
        same_letters, current_dict = self.find_same_letters(input_word, dict_nested_letters)
        if len(same_letters) <= 1:
            return None
        list_same_letters: list = self.get_list_letters_from_dict(current_dict)
        for letters in list_same_letters:
            new_word: str = input_word + "".join(letters)
            result_dict: List[List[str]] = self.get_list_letters_from_dict(
                self.get_dict_with_letters(same_letters, current_dict)
            )
            for list_letters in result_dict:
                self.remove_keys_in_order(dict_nested_letters, list_letters)
            self.main(input_word, results, dict_nested_letters)
            if new_word != input_word:
                results.append(new_word)


if __name__ == "__main__":
    print("Задание 1")
    print(save_unique_data())  # Задание 1
    print("\nЗадание 2")
    pprint.pprint(calculate([{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]))  # Задание 2
    print("\nЗадание 3")
    pprint.pprint(get_list_dict_digits([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Задание 3
    print("\nЗадание 4")
    pprint.pprint(list(remove_file_by_date(1)))  # Задание 4
    # print("\nЗадание 5")
    # concatenation_words: ConcatenationWords = ConcatenationWords()
    # list_words: List[str] = concatenation_words.read_file("task5.txt")
    # print(concatenation_words.concatenate_words(list_words))  # Задание 5

    print("\nЗадание 5. Другое решение")
    concatenation_words_two: ConcatenationWordsTwo = ConcatenationWordsTwo()
    list_words: List[str] = concatenation_words_two.read_file("task5.txt")
    dict_nested_letters_ = concatenation_words_two.convert_words_to_dicts(list_words)

    for _ in range(3):
        results_concat_words: List[str] = []
        custom_word: str = input("Введите любое слово из файла task5.txt: \n<<< ")
        concatenation_words_two.main(custom_word, results_concat_words, dict_nested_letters_)  # Задание 5
        print(results_concat_words)
