# Conditional Statements

marks = int(input("Enter your mark to assess your grade : "))
if marks < 0 or marks > 100:
    print("Invalid input. Enter numbers from 0 to 100.")
elif marks >= 90 and marks <= 100:
    print("Your grade is : A")
elif marks >= 70:
    print("Your grade is : B")
elif marks >= 50:
    print("Your grade is : c")
else :
    print("Your grade is : F")