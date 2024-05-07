def main():
    book_path = "books/frankenstein.txt"
    try:
        text = read_text_from_file(book_path)
        num_words = count_words(text)
        chars_frequency = count_alpha_characters(text)
        sorted_chars_frequency = sorted(chars_frequency.items(), key=lambda item: item[1], reverse=True)

        print(f"--- Begin report of {book_path} ---")
        print(f"{num_words} words found in the document")
        print()

        for char, count in sorted_chars_frequency:
            print(f"The character '{char}' was found {count} times")

        print("--- End report ---")
    except FileNotFoundError:
        print(f"Error: The file {book_path} cannot be found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def read_text_from_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_alpha_characters(text):
    chars_count = {}
    for char in text.lower():
        if char.isalpha():
            if char in chars_count:
                chars_count[char] += 1
            else:
                chars_count[char] = 1
    return chars_count


main()
