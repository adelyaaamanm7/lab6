import re

def match_pattern(string):
    pattern = r"^[a-z]+_[a-z]+$"  
    return bool(re.fullmatch(pattern, string))  

user_input = input("Enter a string: ")
print(match_pattern(user_input))
