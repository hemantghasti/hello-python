age = 18
if age >= 18:
    print("you are an adult")
    password = "apple123"

user_input = input("Enter password: ")

if user_input == password:
    print("Access granted!")
else:
    print("Wrong password!")
marks = 75

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
age = 20
citizen = True

if age >= 18 and citizen:
    print("You can vote!")
if age >= 18 or citizen:
    print("You can apply!")
if age >= 18 or citizen:
    print("You can apply!")
