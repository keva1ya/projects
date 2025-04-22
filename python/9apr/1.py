#f=open("hello.txt","w") #w,r,a write read and append 
#f.write("file methods in python") #can also use append to write at end write overwrites everything
#f.close("hello.txt") #close the file
f=open("hello.txt","r") #open the file in read mode
print(f.read()) #read the file
