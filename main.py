from stats import *
import sys



def get_book_text(filepath):
    if len(filepath) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    with open(filepath[1]) as f:
        file_contents = f.read()
    return file_contents



def main():
    try:
        text = get_book_text(sys.argv)
    except Exception as e:
        print(e)
    num_words = count_words(text)
    #print(count_characters(text))
    dict_list = order_dict(count_characters(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key in dict_list:
        if key["char"].isalpha():
            print(f"{key["char"]}: {key["num"]}")

    return


#--------------main-----------------#

main()