# Create the Simplest Function

# def -- to declare a function
def say_hi():
    print("Hello there!")
    print("Goodbye!")
say_hi() #call the function


# Task 2
def yell_it():
    message = input("Enter your message: ")
    print(message.upper() + "!")
yell_it()


# Function with parameters
def say_this(phrase):
    print(phrase)
say_this("Hello")

def yell_this(phrase):
    print(phrase.upper() + "!")
yell_this("stop it")

# With Default Value
def yell_this(phrase = "ready ... go"):
    print(phrase.upper() + "!")
yell_this("stop it")
yell_this()