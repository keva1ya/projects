f=open("2.txt","w")
f.write("hello world") #enters in a single line
f.writelines(["\nhello\n","this is python\n","file methods\n"]) #lines get entered in multiple lines as entered in different strings 
f.close()