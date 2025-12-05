from stats import *

def main():
    book_path = '/home/momoka/workspace/bookbot/books/frankenstein.txt'
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_count = character_count(text)
    char_sort = character_sort(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sort:
        ch = item["char"]
        count = item["num"]
        print(f"{ch}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

