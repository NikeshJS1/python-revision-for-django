# print("Yoyo")
#to comment out
'''
Character set: Letters: A to Z, a to z
digits: 0 to 9
special symbols: - + / * etc.
whitespaces, blank spaces, tab, carriage return, newline, formfeed
Py can process all ASCII and Unicode characters as part of data or literals
'''

print("My name is NJS." , "My age is 20.")
print(23)
print(35)
print(23,35)

name = "NJS"
print(name)

print("My name is : ", name)

print(type(name)) #value of 'name' is of the string type.

#strings can be represented in single, double or triple quote

# datatypes: int, str, float, bool, none

age = 23
old = False
a= None

print(type(old))
print(type(age))
print(type(a))
print(a)

#reserved: and,as,assert,break,class,continue,def,del,elif,else,except,finally,False,for,from,global,if,import,in,is,lambda,nonlocal,None,not,or,pass,raise,return,True,try,with,while,yield

#Python is case-sensitive language.

num = 10
num2 = num
num += 20
print(num)

#other operators are easy
#Logical Operators: and or not
print(not False)
#print((num2>num))

#Type conversion: Type conversion, type casting
e = 2
f = 4.25

sum = e + f # 2.0 + 4.25 = 6.25 (Implicit conversion)
print(sum)
g = "2"
h = 1
print(int(g) + h) # Type casting

#Inputs in python
heyy = input("Enter your name: ")
print("Hello, ", heyy)


i = int(input("Enter your first number: "))
j = float(input("Enter your second number: "))
add = i + j
print("The required result is: ", add)



