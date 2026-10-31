def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(item: tuple[str, int]) -> int:
    return item[1]


def chars_dict_to_sorted_list (num_chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    sorted_list = []
    for char, count in num_chars_dict.items():
        sorted_list.append((char, count))
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list