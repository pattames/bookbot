from typing import TypedDict

# Count words from book's text
def count_words(book_str: str) -> int:
    word_list = book_str.split()
    return len(word_list)

# Count each character from book's text
def count_each_char(book_str: str) -> dict[str, int]:
    count_per_char = {}
    text_lower = book_str.lower()

    for char in text_lower:
        if char not in count_per_char:
            count_per_char[char] = 1
        else:
            count_per_char[char] += 1

    return count_per_char

## Transform count_each_char's dictionary into a sorted list of tuples: (char, count)
## helper function for sorted()
def sort_on(char_count_pair: tuple[str, int]) -> int:
    return char_count_pair[1]

def chars_dict_to_sorted_list(char_count_dict: dict[str, int]) -> list[tuple[str, int]]:
    char_count_tuple_list: list[tuple[str, int]] = []

    for char, count in char_count_dict.items():
        char_count_tuple_list.append((char, count))

    return sorted(char_count_tuple_list, reverse=True, key=sort_on)

# Deprecated previous approach for sorting: transform count_each_char's dictionary into a sorted list of dictionaries
class CharacterCount(TypedDict):
    char: str
    num: int

# helper function for .sort()
def get_num(e: CharacterCount) -> int:
    return e["num"]

def format_char_count(char_count_dict: dict[str, int]) -> list[CharacterCount]:
    char_count_list: list[CharacterCount] = []

    for key, value in char_count_dict.items():
        char_count_list.append({"char": key, "num": value})

    char_count_list.sort(reverse=True, key=get_num)

    return char_count_list
