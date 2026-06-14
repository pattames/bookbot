from stats import count_words, count_each_char, format_char_count, CharacterCount
import sys

def main() -> None:
    # Handle book path coming from command line argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        # Exit the program with a status code of 1
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_each_char(text)
    formatted_char_count = format_char_count(char_count)
    
    print_report(book_path, word_count, formatted_char_count)

# Get the book file and return it as a string
def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

# Print report in a pretty way
def print_report(book_path: str, word_count: int, formatted_char_count: list[CharacterCount]) -> None:
    print("============BOOKBOT============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for pair in formatted_char_count:
        if pair["char"].isalpha():
            print(f"{pair['char']}: {pair['num']}")
    print("============= END ===============")

main()
