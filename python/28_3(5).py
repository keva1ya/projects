import unicodedata

def is_palindrome(s):
    cleaned_s = ''.join(c for c in unicodedata.normalize('NFC', s) if c.isalnum()).lower()
    return cleaned_s == cleaned_s[::-1]
s = input("Enter a string: ")
print(is_palindrome(s))
