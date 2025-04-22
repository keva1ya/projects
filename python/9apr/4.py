f=open("2.txt","r")
f.seek(0) #used to set the current file position (the number is the number of byte position, eg 0 means start of file)
f.tell() #returns the current file position
print(f.read(5)) #read one character from the file
print(f.tell())#prints position in file stream