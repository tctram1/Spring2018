#Conditionals, Types, and Mathematics extended
#Conditionals: 'elif'

weather = input("Enter weather (sunny, rainy, snowy): ")

if weather.lower() == "sunny":
    print("Wear a T-shirt.")
elif weather.lower() == "rainy":
    print("Bring an umbrella!")
elif weather.lower() == "snowy":
    print("STAY INDOOR!!!")
else:
    print("Sorry, not sure what to suggest for" , weather)

print("-----------------------------------------")

shirt_size = input("Enter shirt size (S, M, L): ")
S = 6
M = 7
L = 8

if shirt_size.upper() == "S":
    print("The price for size S: $" , S)
elif shirt_size.upper() == "M":
    print("The price for size M: $" , M)
elif shirt_size.upper() == "L":
    print("The price for size L: $" , L)
else:
    print("Sorry We don't have size" , shirt_size , "available!")