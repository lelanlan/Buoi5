
from builtins import print

# Bài 1
# Cách 1
def demkitu(str):
    Upper = sum(1 for c in str if c.isupper())
    Lower = sum(1 for c in str if c.islower())
    number = sum(1 for c in str if c.isnumeric())
    LETTERS = sum(1 for c in str if c.isupper()) + sum(1 for c in str if c.islower())
    dict = {"LETTERS": LETTERS, "CASE": {"UPPER CASE": Upper, "LOWER CASE": Lower}, "DIGITS": number}
    return dict


# cách 2
def demkitu1(str):
    Upper1 = sum(1 for c in str if c in (chr(x) for x in range(65, 91)))
    Lower1 = sum(1 for c in str if c in (chr(x) for x in range(97, 123)))
    number1 = sum(1 for c in str if c in (chr(x) for x in range(48, 58)))
    LETTERS1 = sum(1 for c in str if c in (chr(x) for x in range(97, 123)) or c in (chr(x) for x in range(65, 91)))
    dict1={"LETTERS":LETTERS1, "CASE": {"UPPER CASE":Upper1, "LOWER CASE":Lower1}, "DIGITS":number1}
    return dict1

print(demkitu("Hello World! 123"))
print(demkitu1("Hello World! 123"))



