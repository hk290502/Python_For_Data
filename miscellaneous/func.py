def subtract_numbers(a, b): 
     return b - a

print(subtract_numbers(10, 17))

def multiply_numbers(a, b): 
     return a * b

print(multiply_numbers(5,30))

def check_positive(num):
     if num > 0:
          return "Positive"
     else:
          return "Negative"
     
print(check_positive(3))


def count_vowels(word):
    count = 0
    vowels = ["a", "e", "i", "o", "u"]

    for letter in word.lower():
        if letter in vowels:
            count = count + 1

    return count


print(count_vowels("Seven"))

def find_smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c


print(find_smallest(10, 13, 11))


def calculate_area(length, width):
    return f"The area of a rectangle is {length}cm multiplied by {width}cm so it is {length*width}cm"
    

print(calculate_area(4,3))

def convert_to_uppercase(text):
    return f"The upper case for {text} is {text.upper()}!"

print(convert_to_uppercase("greetings my name is hamza"))

