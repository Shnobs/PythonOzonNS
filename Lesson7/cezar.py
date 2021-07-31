def encrypt(text, shift):
    encryption = ''
    for symbol in text:
        if symbol.isalpha():
            symbol = symbol.lower()
            c_unicode = ord(symbol)
            c_index = ord(symbol) - ord('a')
            new_index = (c_index+shift) % 26
            new_unicode = new_index + ord('a')
            new_char = chr(new_unicode)
    return encryption
print(encrypt('abcdef', 3))
# print(ord('a'))
# print(ord('z'))
# for i in range(97, 123):
#     print(chr(i))
# for i in range(65, 91):
#     print(chr(i))