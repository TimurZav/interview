from typing import List


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
    concatenation_words: ConcatenationWords = ConcatenationWords()
    print(concatenation_words.concatenate_words())
