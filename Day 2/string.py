str1 = "This is a string."
#Can be created in single quote, triple quote
str2 = "Hey! It's good to see you again. \nWe welcome you back."
print(str2)

#Concatenation
str3 = "NJS"
str4 = " Hancy"
print(str3 + str4)

#Accessing index : var[index]
#Can only be accessed, not modified

#Slicing: Accessing parts of a string
'''
str = "National College"
print(str[1:4])
str[:4] is similar to [0:4]
str[5:] is similar to [5:len(str)]

Negative index: Background counting
starts from -1 and decreased further
A   P  P  L  E
-5 -4 -3 -2 -1

str = "Apple"
str[-3:-1] is "pl"
'''

#String functions:
'''
str.endswith("er.") returns true if string ends with "er"
str.capitalize() capitalizes 1st char
str.replace("old", "new") replaces old value with new one
str.find(word) returns 1st index of 1st occurrence of that word and returns -1 if does not exist
str.count("am") counts the occurrence of passed substring
'''

str = "Nikesh Jung Shrestha"
print(str[1:5])


