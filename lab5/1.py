import re

def match_ab_pattern(string):
    pattern = r"ab*" 
    return bool(re.fullmatch(pattern, string)) 

user_input = input("Enter a string: ")
print(match_ab_pattern(user_input))
