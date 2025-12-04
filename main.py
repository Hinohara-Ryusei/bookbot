def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    count = len(words)
    return count

def main():
    text = get_book_text('/home/momoka/workspace/bookbot/books/frankenstein.txt')
    num_words = word_count(text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()

