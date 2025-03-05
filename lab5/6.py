import re

def replace_ch(string):
    pattern = r"[ ,.]"  
    return re.sub(pattern, ":", string)  


user_input = input("Enter a string: ")
print(replace_ch(user_input))
