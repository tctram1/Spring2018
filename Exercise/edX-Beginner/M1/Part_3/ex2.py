# Function Return Value

def msg_double(phrase):
    double = phrase + " " + phrase
    return double
msg_2x = msg_double("let's go")
print(msg_2x + "!")


def half_value(value):
    return value/2
print(half_value(44))


# Task 1
def make_doctor(phrase):
    display = "Doctor " + phrase
    return display
name = make_doctor(input("Enter your name: ").capitalize())
print("Hi," , name)



# Function with Multiple Parameters

def make_schedule(period1, period2):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title())
    return schedule
student_schedule = make_schedule("mathematics", "history")
print("SCHEDULE: " + student_schedule)

def format_info(name, age, school):
    return "Student: " + name + "\nAge: " + str(age) + "\nSchool " + school
print(format_info("Yumie Hwang", 23, "WCU"))


# Task 2
def make_sched(period1, period2, period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title())
    return schedule
student_sched = make_sched(input("Enter 1st period class: "), input("Enter 2nd period class: "), input("Enter 3rd period class: "))
print("SCHEDULE: " + student_sched)