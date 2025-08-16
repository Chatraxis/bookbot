
def count_characters(text):
    character_dict = {}
    lower_text = text.lower()
    for c in lower_text:
        if c in character_dict:
         character_dict[c] += 1
        else:
         character_dict[c] = 1
    return character_dict

def sort_on(items):
    return items["num"]

def order_dict(dict):
    dict_list = []
    for key in dict:
        dict_list.append({"char": key, "num":dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return(dict_list)



def count_words(text):
    word_list = text.split() 
    number_of_words = len(word_list)
    return number_of_words


# Test_text = "sadplföm lpmasflöpm aösldfma"
# test_dict = {}
# for c in Test_text:
#     if c in test_dict:
#         test_dict[c] += 1
#     else:
#         test_dict[c] = 1
# print(test_dict)
# dict_list = []
# for key in test_dict:
#     dict_list.append({"char": key, "num":test_dict[key]})
# print(dict_list)


# dict_list.sort(reverse=True, key=sort_on)
# print(dict_list)
