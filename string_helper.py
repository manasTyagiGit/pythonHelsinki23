def change_case(orig_string: str) :    
    return orig_string.swapcase()

def split_in_half(orig_string: str) :
    mid = len(orig_string) // 2

    str1 = orig_string[0:mid]
    str2 = orig_string[mid:]

    return (str1, str2)

def remove_special_characters(orig_string: str) :
    true = []

    for char in orig_string :
        if char.islower() or char.isupper() or char == " " or char.isnumeric() :
            true.append(char)

    ret = ''.join(true)

    return ret
