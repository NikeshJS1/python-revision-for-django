#Python program to input name and print its length

# name = input("Enter your name: ")
# print(len(name))
# print(name.count("$"))

#Python program to check if an input number is odd or even:
num = int(input("Enter your number: "))
if(num % 2 == 0):
    print(num," is an even number.")
else:
    print(num, " is an odd number.")


#Program to find greatest of three numbers input by the user:
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))
if(num1 > num2 and num1 > num3):
        print(num1, " is the greatest.")
elif(num2 > num3):
    print(num2, " is the greatest.")
else:
    print(num3, " is the greatest.")

#Program to check if a number is a multiple of 7 or not:
Num = int(input("Enter your beautiful number: "))
if(Num % 7 == 0):
    print(Num, " is a multiple of 7.")
else:
    print(Num, " is not a multiple of 7.")
