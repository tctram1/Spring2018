#If Statement
#Conditionals: Boolean String test methods with 'if'

# .isalpha()
# .isalnum()
# .istitle()
# .isdigit()
# .islower()
# .startswith()

favorite_book = input("Enter the title of your favorite book: ")

if favorite_book.istitle():
    print(favorite_book , "- nice capitalization in that title!")
else:
    print(favorite_book , "- Tip: capitalize each word for book titles.")


#Task 2
string1 = "welcome"
string2 = "I have $3"

if string1.islower() and string2.islower():
    print("These strings are both in lowercase.")
else:
    print("String 1:" , string1 , "and String 2:" , string2)

string1 = "welcome"
string2 = "i have $3"

if string1.islower() and string2.islower():
    print("These strings are both in lowercase.")
else:
    print("String 1:" , string1 , "and String 2:" , string2)