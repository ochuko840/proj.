#programme to check mark of a student and return appropriate grade.
#A=75-100
#B=60-74
#C=55-59
#D=45-54
#E=35-44
#F=0-34

value = input("Enter your score between 0-100: ")
value = int(value)
if value <= 34:
    print("Your grade is an F, and sadly you failed.")
elif value <= 44:
    print("You passed the exam and your grade is E.")
elif value <= 54:
    print("You passed the exam and your grade is a D, well done.")
elif value <= 59:
    print("You have passed the exam and your grade is a C, well done.")
elif value <= 74:
    print("You have done excellently well, and your grade is a B.")
elif value<= 100:
    print("Congratulations! You scored an A.")
else:
    print("Please, follow instructions by entering a score between 0 and 100.")










