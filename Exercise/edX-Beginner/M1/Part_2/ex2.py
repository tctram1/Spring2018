# formatting string with Commas

name = "Yumie"
city = "Cullowhee"

# normal string
print("Hello " + name + "!")

# string with Commas
print("Hello to" , name , "who is from" , city + ".")


school = "WCU"
major = "IDES & CIS"

print("Hello! My name is", name + ". I'm currently attending" , school , "for" , major + ".")


# formatting string with Commas - with both string and number

# cannot add string and number together method
print("I will pick you up at " + "6" + " pm.")

# fixing it
print("I will pick you up at" , 8 , "pm.")

# another example
courses = 5
print("I am taking" , courses , "classes.")


# Task 2
print("I have" , 2 , "chickens and" , 3 , "dogs.")


#Task 3
st_number = input("Street Number: ")
st_name = input("Stree Name: ")
print("Please deliver this to" , st_number , st_name + ".")


# Task 5
owner = input("Enter contract person for this training session: ")
num_people = input("Enter the number of attendees: ")
training_time = input("Enter the training time: ")
date = input("Enter date (mm/dd/yy): ")
min_early = input("Early arrival time (minutes): ")

print("-----------------------------------------")
print("Reminder:" , owner , "training session will be on" , date , "at" , training_time + ". There will be a total of" , num_people , "attendees. Please arrive", min_early , "minutes before the session.")
