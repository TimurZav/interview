def read_file(file_name: str) -> dict:
    """
    Read file from directory.
    :return:
    """
    with open(file_name, "r") as file:
        words = file.read().splitlines()

    dict_nested_letters: dict = {}
    for word in words:
        current_dict: dict = dict_nested_letters
        x = []
        for letter in word:
            if letter not in current_dict:
                if all(x) and x:
                    current_dict[''] = {}
                current_dict[letter] = {}
                x.append(False)
            current_dict = current_dict[letter]
            x.append(True)
    return dict_nested_letters


def get_word_from_nested_dict(nested_dict):
    words = []
    word = []
    current_dict = nested_dict
    while current_dict:
        letters = list(current_dict.keys())
        if letters[0]:
            letter = letters[0]
            word.append(letter)
            current_dict = current_dict[letter]
        elif letters[0] == '':
            current_dict.pop(letters[0])
            words.append(word.copy())
        else:
            break
    words.append(word)
    return words


def merge_list_dict(letters, nested_dict):
    result_dict = {}
    current_dict = result_dict

    for letter in letters:
        if letter not in current_dict:
            current_dict[letter] = {}
        current_dict = current_dict[letter]

    for letters in get_word_from_nested_dict(nested_dict):
        for letter in letters:
            if letter not in current_dict:
                current_dict[letter] = {}
            current_dict = current_dict[letter]

    return result_dict


def remove_keys_in_order(dct, keys):
    if not keys:
        return dct
    key = keys.pop(0)
    if key in dct:
        dct[key] = remove_keys_in_order(dct[key], keys)
        if not dct[key]:
            del dct[key]
    return dct


def find_word(start_word, nested_dict):
    current_dict = nested_dict
    x = []
    for letter in start_word:
        if letter in current_dict:
            current_dict = current_dict[letter]
            x.append(letter)
        else:
            current_dict = nested_dict
            x = []
            if letter in nested_dict:
                current_dict = current_dict[letter]
                x.append(letter)
    return current_dict, x


def main(start_word, nested_dict, results):
    current_dict, x = find_word(start_word, nested_dict)
    if len(x) <= 1:
        return None
    list_words = get_word_from_nested_dict(current_dict)
    for letters in list_words:
        word = start_word + "".join(letters)
        result_dict = merge_list_dict(x, current_dict)
        result_dict = get_word_from_nested_dict(result_dict)
        for list_letters in result_dict:
            nested_dict = remove_keys_in_order(nested_dict, list_letters)
        main(start_word, nested_dict, results)
        if word != start_word:
            results.append(word)


start_word = input("Введите любое слово из файла task5.txt: \n<<< ")
nested_dictionary = read_file("task5.txt")
results = []
main(start_word, nested_dictionary, results)
print(results)
