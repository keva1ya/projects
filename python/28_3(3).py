import unicodedata

def bitwise_operation(a, b, op):
    if op not in {'&', '|', '^', '<<', '>>'}:
        print("Invalid operator. Please use one of: &, |, ^, <<, >>")
        return
    
    if op in {'<<', '>>'} and b < 0:
        print("Invalid shift value. It should be a non-negative integer.")
        return
    
    if op == '&':
        result = a & b
    elif op == '|':
        result = a | b
    elif op == '^':
        result = a ^ b
    elif op == '<<':
        result = a << b
    elif op == '>>':
        result = a >> b
    
    print(f"Result: {result}")

try:
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    op = input("Enter bitwise operator (&, |, ^, <<, >>): ")
    bitwise_operation(a, b, op)
except ValueError:
    print("Invalid input. Please enter integers only.")

def number_pattern(n):
    if n <= 0 or n % 2 == 0:
        print("Please enter a positive odd number.")
        return
    
    num = 1
    for i in range(1, n + 1, 2):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()

try:
    n = int(input("Enter an odd number: "))
    number_pattern(n)
except ValueError:
    print("Invalid input. Please enter a positive odd integer.")

def is_palindrome(s):
    cleaned_s = ''.join(c for c in unicodedata.normalize('NFKD', s) if c.isalnum()).lower()
    return cleaned_s == cleaned_s[::-1]

s = input("Enter a string: ")
print(is_palindrome(s))
