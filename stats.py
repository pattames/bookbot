from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int

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

# .sort() helper function
def get_num(e: CharacterCount) -> int:
    return e["num"]

# Transform count_each_char's dictionary into a sorted list of dictionaries
def format_char_count(char_count_dict: dict[str, int]) -> list[CharacterCount]:
    char_count_list: list[CharacterCount] = []

    for key, value in char_count_dict.items():
        char_count_list.append({"char": key, "num": value})

    char_count_list.sort(reverse=True, key=get_num)

    return char_count_list
