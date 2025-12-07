from stats import count_words, count_characters, sort_counts
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f'Found {count_words(file_contents)} total words')
    print("--------- Character Count -------")

    char_count = count_characters(file_contents)
    sorted_count = sort_counts(char_count)
    for i in sorted_count:
        print(f'{i["char"]}: {i["num"]}')
    print("============= END ===============")

main()