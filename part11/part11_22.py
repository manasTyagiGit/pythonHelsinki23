def filter_forbidden(string: str, forbidden: str) :
    char_list = [char for char in string if char not in forbidden]
    return "".join(char_list)

sentence = "Once! upon, a time: there was a python!??!?!"
filtered = filter_forbidden(sentence, "!?:,.")
print(filtered)