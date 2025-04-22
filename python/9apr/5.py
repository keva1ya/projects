f = open("h3.txt", "w+")
f.writelines(["this is python file methods\n", "we can use truncate to limit the size of file\n"])  # more than 5 characters
f.truncate(10000) #edits the file to 5 characters and deletes the rest
