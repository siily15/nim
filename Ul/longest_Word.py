def longest_word(s):
    words = s.split()
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

print(longest_word("Margaret's toy is a pretty doll."))
print(longest_word("A thing of beauty is a joy forever."))
print(longest_word("Forgetfulness is by all means powerless!"))
