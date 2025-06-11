# List is a built-in datatype that stores set of values.
#It can store elements of different data types (in a single list)

#marks = [1,2,3,4,5] is a list. Similar to array

marks = [90.1, 87.5, 40.9, 87.8, 75.5]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[3])
#Strings are immutable in python (cannot be changed). List is mutable (can be changed)

#list slicing is also possible

print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])
#The ending index is not included while slicing
#In marks[1:4], value from index 0 to 3 is printed.

#List methods:
'''
list.append(4) ;adds one element at the end
list.sort() ;sorts in ascending order
list.sort(reverse = True) ;sorts in descending order
list.reverse() ;reverses list
list.insert(index, element) ;inserts element at the given index
list.remove(1) ;removes first occurrence of given element
list.pop(index) ;removes element at given index
sorting is possible in strings too
'''


#Tuples is a built-in datatype that lets us created immutable sequence of values.
tup = (87, 64, 33, 95, 76) #tup[0], tup[1]
#tup[0] = 43 not allowed
tup1 = ()
tup2 = (1,) #single value tuple, comma compulsory
tup3 = (1,2,3)
#tuple methods
'''
tup.index(element) ;returns index of first occurrence of element
tup.count(element) ;counts total occurrences of element
'''



