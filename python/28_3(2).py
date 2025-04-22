def transform_string(s, n):
    if n <= 0 or n > len(s):
        print("Invalid value for n. It should be between 1 and the length of the string.")
        return
    
    result = "".join(c.upper() if (i + 1) % n == 0 else c.lower() for i, c in enumerate(s))
    print(result)


s = input("Enter a string: ")
n = int(input("Enter an integer n: "))
transform_string(s, n)
