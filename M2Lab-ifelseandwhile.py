# Olivia Bertinelli
# Module 2 Lab - Case Study: if else and while
# This program is intended to accept student names and GPAs to determine if the student
# qualifies for the Dean's List or Honor Roll
last_name = input("Enter student's last name or enter ZZZ to quit: ")
if last_name == "ZZZ":
    print("Quit")
else:
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA (grade point average: )"))
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Deans List and Honor Roll!")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made Honor Roll!")
    else:
        print(f"{first_name} {last_name} has not made Honor Roll or Dean's List.")
