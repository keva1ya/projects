#write a program to create a package that defines some functions and based on the need and based on the needs those functions are called by some other files in the same package  
from package.calc  import add
from package.lowerupper import lowtoup
print (add(10, 20))
print (lowtoup("hello"))
