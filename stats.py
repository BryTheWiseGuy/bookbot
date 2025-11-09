def word_count(text):
    words = text.split()
    return len(words)
        
def character_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sorted_dict(char_dict):
    dict_list = []
    for key, value in char_dict.items():
        dict_list.append({"char": key, "num": value})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list