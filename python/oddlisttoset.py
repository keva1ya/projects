#write a py program to convert a list of odd numbers into a set using list compreshension (0-1000)
oddset=set ([x for x in range (1000) if x%2!=0])
print(oddset)