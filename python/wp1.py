def listin():
    x = input("Enter a list of items separated by commas: ")
    y = x.split(",")
    list1 = []
    for item in y:
        list1.append(item.strip())
    return list1
def indexin():
    while True:
        try:
            return int(input("enter an index: "))
        except ValueError:
            print("enter an integer")
def main():
    list1 = listin()
    while True:
        try:
            index = indexin()
            print(f"element on index {index}: {list1[index]}")
            break
        except IndexError:
            print("index outside range, enter valid index")
main()
