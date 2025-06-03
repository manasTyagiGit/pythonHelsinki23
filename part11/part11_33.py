# This is not a correct version for balance parenthesis, so please do not refer to this
# for any sort of algorithmic value, this is just for practice

def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')') :
        if not (my_string[0] == '[' and my_string[-1] == ']') :
            return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])

ok = balanced_brackets("([([])])")
print(ok)

# this is no good, the closing bracket doesn't match
ok = balanced_brackets("(()]")
print(ok)

# different types of brackets are mismatched
ok = balanced_brackets("([bad egg)]")
print(ok)