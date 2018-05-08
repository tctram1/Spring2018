#Conditionals, Types, and Mathematics extended
#Casting
# int(), str(), float()


weight1 = "60"
weight2 = 140

total = int(weight1) + weight2

print(total)


print("-----------------------------------------")


age_new_student = input("Enter age: ")

grad_age = float(age_new_student) + 3.75

print("Age upon graduation will be:" , grad_age)


print("-----------------------------------------")


grad_age_msg = "You will graduate at " + str(grad_age)

print(grad_age_msg)


print("-----------------------------------------")


student_age = input('Enter age: ')
age_next_year = int(student_age) + 1
print('Next year student will be',age_next_year)


print("-----------------------------------------")


student_age = int(input('enter student age (integer): '))

age_in_decade = student_age + 10

print('In a decade the student will be', age_in_decade)


print("-----------------------------------------")


#Task 3 Program: Adding Calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = num1 + num2

print("The sum is:" , total)