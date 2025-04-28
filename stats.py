def count(text):
    text = text.split()
    return len(text)

def count_characters(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict  # DO NOT sort here

def sort_characters_by_count(char_dict):
    sorted_list = sorted(
        [{"char": char, "num": count} for char, count in char_dict.items()],
        key=lambda x: x["num"],
        reverse=True
    )
    return sorted_list
