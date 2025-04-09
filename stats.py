def num_words(text):
    words = text.split()
    return len(words)

def count_each_char(text):
    chars = {}
    for c in text:
        c = c.lower()
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

def sort_char(count_each_char):
    char_list = []
    for char, count in count_each_char.items():
        char_list.append({"char": char, "count": count})

    def sort_on(dict_item):
        return dict_item["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

