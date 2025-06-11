#if,elif and else statements

marks = float(input("Enter your percentage: "))
if(marks >= 40.0):
    print("You have passed the exam. Congratulations!")
elif(marks < 10.0):
    print("Very poor academic performance. You have failed and need to work extra hard.")
else:
    print("You have failed the exam. Work hard.")

