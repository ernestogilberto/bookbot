import sys
from stats import get_num_words



def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    with open(path_to_book) as f:
        file_contents = f.read()
        word_count = get_num_words(file_contents)


    # print(file_contents)
    # print(word_count)

    unique_characters = count_unique_characters(file_contents)
    # print(unique_characters)

    print_report(word_count, unique_characters)

def count_unique_characters(file_contents):
    counter = {}
    for character in file_contents.lower():
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter

def print_report(word_count, unique_characters):
    path_to_book = sys.argv[1]
    print(f"--- Begin report of {path_to_book} ---")
    message1 = f"Found {word_count} total words"
    print(message1)
    print("Unique characters found in the document")

    for character, count in unique_characters.items():
        if character.isalpha():
            print(f"{character}: {count}")
    print("--- End of report ---")

if __name__ == "__main__":
    main()