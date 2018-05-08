def add(a, b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} + {b}")
    return a + b

def multiply(a, b):
    print(f"Multiplying {a} + {b}")
    return a + b

def divide(a, b):
    print(f"Dividing {a} + {b}")
    return a + b

print("Let's do some math with these functions!")

dog = add(30, 5)
cat = subtract(20, 2)
mouse = multiply(5, 7)
cow = divide(100, 2)

print(f"""
Add Dogs: {dog};
Subtract Cats: {cat};
Multiply Mouse: {mouse};
Divide Cow: {cow};
""")