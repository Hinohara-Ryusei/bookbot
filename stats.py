from collections import Counter

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    count = len(words)
    return count

def character_count(text):
    char_count = {}

    for char in text:
        if char.isalpha():
            c = char.lower()
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1
    
    return char_count

def get_num_for_char_sort(temp_dict):
    return temp_dict["num"]

def character_sort(text):
    char_count = character_count(text)
    result_list = []
    for char,num in char_count.items():
        temp_dict = {"char":char, "num":num}
        result_list.append(temp_dict)
    result_list.sort(key=get_num_for_char_sort,reverse=True)
    return result_list

