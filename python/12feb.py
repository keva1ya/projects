# write a program to create the emoji :)
dict = {"happy": ":)", "sad": ":("}
m=input("enter the mood:").lower()  
if m=="happy":
    print(dict["happy"])
elif m=="sad":
    print(dict["sad"])
else:
    print("change ur moood")
x=input()