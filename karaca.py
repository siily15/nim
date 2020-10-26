def encrypt(word):

    vowels = {'a': '0', 'e': '1', 'i': '2', 'o': '2', 'u': '3'}

    encrypted = word[::-1]

    for char in encrypted:
        if char in vowels.keys():
            encrypted = encrypted.replace(char, vowels[char])

    return encrypted + 'aca'

print(encrypt("banana"))
print(encrypt("karaca"))
print(encrypt("burak"))
print(encrypt("alpaca"))
