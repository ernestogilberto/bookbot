def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)


    # print(file_contents)
    # print(word_count)

    unique_characters = count_unique_characters(file_contents)
    # print(unique_characters)

    print_report(word_count, unique_characters)

def count_words(file_contents):
    return len(file_contents.split())

def count_unique_characters(file_contents):
    counter = {}
    for character in file_contents.lower():
        if character in counter:
            counter[character] += 1
        else:
            counter[character] = 1
    return counter

def print_report(word_count, unique_characters):
    print("--- Begin report of books/frankenstein.txt ---")
    message1 = {f"{word_count} words found in the document"}
    print(message1)
    print("Unique characters found in the document")

    for character, count in unique_characters.items():
        if character.isalpha():
            print(f"The '{character}' was found {count} times")
    print("--- End of report ---")

if __name__ == "__main__":
    main()