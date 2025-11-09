# -*- coding: utf-8 -*-
import sys
from stats import word_count, character_count, sorted_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    num_words = word_count(text)
    char_dict = character_count(text)
    count_dict = sorted_dict(char_dict)
    
    print("============ BOOKBOT ============\n"
    f"Analyzing book found at {sys.argv[1]}\n"
    "----------- Word Count ----------\n"
    f"Found {num_words} total words\n"
    "--------- Character Count -------")
    
    for item in count_dict:
        char = item["char"]
        if char.isalpha():
            count = item["num"]
            print(f"{char}: {count}")
            
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
        
main()