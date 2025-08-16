from stats import *



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents



def main():
    text = get_book_text("/home/chatraxis/bookbot/books/frankenstein.txt")
    num_words = count_words(text)
    #print(count_characters(text))
    dict_list = order_dict(count_characters(text))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key in dict_list:
        if key["char"].isalpha():
            print(f"{key["char"]}: {key["num"]}")

    return


#--------------main-----------------#

main()