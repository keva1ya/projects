input_string = input("Enter a string: ")
os = ""

for char in input_string:
    if char >= 'a' and char <= 'z': 
        os =os+ char.upper() 
    else:
        os =os+ char

print("Converted string:", os)
