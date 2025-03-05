import re

def match_pattern(string):
    pattern = r"\b[A-Z][a-z]+\b"  
    return bool(re.fullmatch(pattern, string))  

user_input = input("Enter a string: ")
print(match_pattern(user_input))