f= open("s.txt","w")
f.write("hello world")
f.flush()#writes the buffer immidieately into the file
f.close()