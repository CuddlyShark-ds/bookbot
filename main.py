import re

file_path = "books/frankenstein.txt"

def main():
    with open(file_path) as f:
        file_contents = f.read()
        
    total_words_found = word_counter(file_contents)
    #print(f"total words found: {total_words_found}")
    
    letters_dict = tally_of_all_letters(file_contents)
    #print(letters_dict)
    
    report(letters_dict, total_words_found)
        
def word_counter(text_file):
    word_count = 0
    word_count = text_file.split()
    word_total = 0
    
    for word in word_count:
        word_total += 1
    
    return word_total

def tally_of_all_letters(text_file):
    letters_dict = {}
    text = text_file.lower()
    
    for char in text:
        if char in letters_dict:
            letters_dict[char] += 1
        else:
            letters_dict[char] = 1
            
    return letters_dict
        
def report(letter_dict, word_count):
    for pair in letter_dict:
        if pair.isalpha():
            print(f"The '{pair}' character was found {letter_dict[pair]} times")
        
main()