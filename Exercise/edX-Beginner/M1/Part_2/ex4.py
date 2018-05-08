# String Format Methods

# .upper() -- .lower() -- .capitalize()
print("ms. Smith is in her school office.".capitalize())
print("You don't have to yell.".lower())
print("but i am yelling!".upper())

# .title() -- .swapcase()
print("time to SAVE everything".title())
print("time to SAVE everything".swapcase())



# Format String Input

# format on input
fav_color = input("What is your favorite color?: ").lower()
print(fav_color)

fav_color = input("What is your favorite color?: ").upper()
print(fav_color)

# format after input
fav_color = input("What is your favorite food?: ")
print(fav_color.capitalize())



# Boolean "in" keyword
menu = "salad pasta sandwich pizza drinks dessert"
print("The menu is:" , menu)
print("Is 'Pizza' in the menu?" , 'Pizza' in menu)
print("Is 'Pizza' in the menu?".lower().capitalize() , 'Pizza'.lower() in menu.lower())
print("Is 'Soup' in the menu?".lower().capitalize() , 'Soup'.lower() in menu.lower())
print("Is 'Dessert' in the menu?".lower().capitalize() , 'Dessert'.lower() in menu.lower())

user_menu = input("Add items to menu: ").lower()
print("The user menu is:" , user_menu)
new_menu = menu + " " + user_menu
print("The new menu is:" , new_menu)
check_menu = input("Is this item on new menu?: ").lower()
print("Is" , check_menu , "in the new menu?".lower().capitalize() , check_menu.lower() in new_menu.lower())