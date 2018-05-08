# this one is like yoiur scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} , arg2: {arg2}")
print_two("Hi" , "Bye")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} , arg2: {arg2}")
print_two_again("Hi2" , "Bye2")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
print_one("This is 1 argument.")

# this oe takes no argument
def print_none():
    print("I got nothing!")
print_none()