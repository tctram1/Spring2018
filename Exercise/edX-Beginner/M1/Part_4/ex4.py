#Conditionals: Comparison Operators with 'if'

position = 19

trap_value = 18

print(position)
if position != trap_value:
    print("...keep playing!")
else:
    print("Position is" , trap_value , ". You're Trapped! ... GAME OVER!")

print("-----------------------------------------")

position = 18

trap_value = 18

print(position)
if position != trap_value:
    print("...keep playing!")
else:
    print("Position is" , trap_value , "... You're Trapped! ... GAME OVER!")

print("-----------------------------------------")

#Task 2
#Create an if/else statement that tests if y is >= x + x
x = 3
y = x + 8

print("x =" , x)
print("y =" , y)
if y >= x:
    print("y >= x --" , y >= x)
else:
    print("y is smaller than x")

print("-----------------------------------------")

x = 3
y = x - 8

print("x =" , x)
print("y =" , y)
if y >= x:
    print("y >= x --" , y >= x)
else:
    print("y is smaller than x")