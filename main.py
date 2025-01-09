
def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str: int]:
    chars = {}
    for c in text:
        lowered = c.lower()
        chars[lowered] = chars.get(lowered, 0) + 1
    return chars


def sort_on(d):
    return d['count']


def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[dict]:
    sorted_list = []
    for char, count in num_chars_dict.items():
        sorted_list.append({'char': char, 'count': count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        char, count = item['char'], item['count']
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {count} times ")

    print("--- End report ---")


if __name__ == '__main__':
    main()
