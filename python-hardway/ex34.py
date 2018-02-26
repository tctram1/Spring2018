animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

i = 0

print(f"Animals: {animals}")

for animal in animals:
    print(f"index [{i}] -- The animal is {animal}")
    i = i + 1

print("___________________________________________________________________________")

animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']

print(f"Animals: {animals}")

for animal in animals:
    if animal == "python3.6":
        i = 0
        i = i + 1
        print(f"The animal at {i} is the 2nd animal -- It is {animal}.")
    elif animal == "peacock":
        i = 0
        i = i + 2
        print(f"The animal at {i} is the 3rd animal -- It is {animal}.")
    elif animal == "bear":
        i = 0
        print(f"The animal at {i} is the 1st animal -- It is {animal}.")
    elif animal == "kangaroo":
        i = 0
        i = i + 3
        print(f"The animal at {i} is the 4th animal -- It is {animal}.")
    elif animal == "platypus":
        i = 0
        i = i + 5
        print(f"The animal at {i} is the 6th animal -- It is {animal}.")
    else:
        i = 0
        i = i + 4
        print(f"The animal at {i} is the 5th animal -- It is {animal}.")