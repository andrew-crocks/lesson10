import re

def is_palindrome():
  
    sentence = input("Введіть речення: ")

    sentence = re.sub(r'[^\w\s]', '', sentence).lower()

    return sentence == sentence[::-1]

result = is_palindrome()
print(result)