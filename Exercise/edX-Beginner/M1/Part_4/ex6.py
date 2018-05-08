#String Comparison

msg = "Save the notebook"

if msg == "save the notebook":
    print("message as expected")
else:
    print("message not as expected")

print("-----------------------------------------")

msg = "Save the notebook"
prediction = "save the notebook"

if msg.lower() == prediction.lower():
    print("message as expected")
else:
    print("message not as expected")

print("-----------------------------------------")

#Task 2
answer = input("What is 8 + 13? ")
correct_answer = "21"

print("Your answer:" , answer)
if answer == correct_answer:
    print("Correct!")
else:
    print("Wrong! The correct answer: 21")


print("-----------------------------------------")

#Task 3
user_answer = input("Japan is in Asia. (T/F): ")
correct = "T"

print("Your answer:" , user_answer)
if user_answer == correct:
    print("Correct!")
else:
    print("Wrong!")