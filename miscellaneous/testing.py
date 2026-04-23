class TooYoungError(Exception):
    pass

def check_entry(age):
    if age < 18:
        raise TooYoungError("Must be 18+")
    else:
        print("Welcome")
        return age

try:
    check_entry(17)
except TooYoungError as t:
    print(t)
