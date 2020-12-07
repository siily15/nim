def repetition(txt, n):
    if n == 0:
        return " "
    else:
        return repetition(txt, n - 1) ++ 




repetition("ab", 3) ➞ "ababab"
repetition("kiwi", 1) ➞ "kiwi"
repetition("cherry", 2) ➞ "cherrycherry"
