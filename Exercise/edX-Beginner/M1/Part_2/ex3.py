# Quotes inside a string

# Single quotes inside double quotes
print("It's time to save your code!")

#Double quotes inside single quotes
print('I said, "Class, Save your code now!"')


# Task 1
print("Where's the homework?")

print('"Education is what remains after one has forgotten what one has learned in school." ~ Albert Einstein')


#Testing with Boolean String Method
#Boolean only runs one string -- not integer
"Python".isalpha()
print('"Python" is alphabet value:' , "Python".isalpha())

"3rd".isalnum()
print('"3rd" is alpha-numeric value:' , "3rd".isalnum())

"Save".startswith("s")
print('"Save" starts with "s":' , "Save".startswith("s"))

"Save".startswith("S")
print('"Save" starts with "S":' , "Save".startswith("S"))

"HEY".islower()
print('"HEY" is lowercase:' , "HEY".islower())

"HEY".isupper()
print('"HEY" is uppercase:' , "HEY".isupper())

"The End".istitle()
print('"The End" is title:' , "The End".istitle())

height = "150"
height.isdigit()
print("Height of" , height , "is all digits:" , height.isdigit())