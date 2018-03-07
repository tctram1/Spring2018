def feetToInches():
    feet = int(input("> Feet: "))
    inches = int(input("> Inches: "))

    totalInches = (feet * 12) + inches

    print("-->" , str(feet) + "'" , str(inches) + '" is' , totalInches , "inches.")


def inchesToFeet():
    inches = int(input("> Inches: "))

    totalFeet = inches / 12

    print("-->" , str(inches) + '" is' , "%.2f feet." % totalFeet)


def meterToFeet():
    pass


def start():
    print("""
    Choose a converter:
    1. ft+in - in
    2. in - ft
    3. m - ft+in
    """)

    choice = input("> ")

    if choice == "1":
        feetToInches()
    elif choice == "2":
        inchesToFeet()
    elif choice == "3":
        meterToFeet()
    else:
        print("Choose one of the above!")


start()