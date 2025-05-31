def anagrams (a : str, b : str) -> bool :
    if sorted(a) == sorted (b) :
        return True

    return False

def palindrome (word : str) :
    reverse = word[::-1]

    if reverse == word :
        print (f"{word} is a palidrome")
    else :
        print (f"{word} is not a palindrome")

if __name__ == "__main__" :
    # print(anagrams("tame", "meta")) # True
    # print(anagrams("tame", "mate")) # True
    # print(anagrams("tame", "team")) # True
    # print(anagrams("tabby", "batty")) # False
    # print(anagrams("python", "java")) # False

    palindrome ("python")
    palindrome ("java")
    palindrome ("oddoreven")
    palindrome ("neveroddoreven")
    palindrome ("12321")
