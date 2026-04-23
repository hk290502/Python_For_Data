def greet_user():

    name = input("Enter your name: ")
    print(f"Hello {name}!")


def add_two_numbers():

    integer_one = int(input("Enter first number: "))
    integer_two = int(input("Enter second number "))
    print(f"Addition result: {integer_one + integer_two}")


def modulus():

    integer_three = int(input("Enter third number: "))
    integer_four = int(input("Enter fourth number "))
    print(f"Modulus result: {integer_three%integer_four}")

greet_user()
add_two_numbers()
modulus()
 
