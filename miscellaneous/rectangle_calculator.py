def user_name():
    name = str(input("Enter your name: "))
    print(f"Hello, {name}!\n")

def area():
    
    length = int(input("Enter Length: "))
    width = int(input("Enter Width: "))

    print(f"\nArea: {length*width}")
    print(f"Perimeter: {2 * (length + width)}")

    return area

user_name()
area()




