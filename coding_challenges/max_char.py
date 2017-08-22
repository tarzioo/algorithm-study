def max_char(str):
    char_dict = {}
    for char in str:
        char_dict[char] = char_dict.get(char, 0) + 1
    
    char_count = char_dict.values()

    keys = char_dict.keys()

    highest = char_count[0]
    place_in_dict = 0
    for i, item in enumerate(char_count):
        if item > highest:
            highest = item
            place_in_dict = i

    return keys[place_in_dict]
