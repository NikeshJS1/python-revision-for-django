# Dictonaries are used to store data in key:value pairs. They are unordered, mutable(changeable) and don't allow duplicate keys.

dict = {
    "name" : "Nikesh",
    "gpa" : 4.0,
    "marks" : [90,80,95]
}

#dict["key"] = "value"   to assign or add new

print(dict["name"])

#keys can be of any datatype. Keys cannot be duplicated.

#Nested dictonaries
student = {
    "name" : "Nikesh",
    "score" : {
        "chem" : 98,
        "phy" : 95,
        "bio" : 90
    }
}
print(student["score"]["phy"])


'''
Dictionary methods:
myDict.keys() --> returns all keys
myDict.values() --> returns all values
myDict.items() --> returns all (key,val) pairs as tuples
myDict.get("key") --> returns the key according to value
myDict.update(newDict) --> inserts the specified items to the dictionary

In real life scenario, prefer get() method to get a certain key value.
'''



#SETS IN PYTHON
#Set is the collection of the unordered items. Each element in the set must be unique and immutable.
#Set as a datatype is mutable. But, the elements of sets are immutable.
#Lists and dictonaries cannot be stored inside set because they are mutable datatypes. Sets can contain items of int, float, tuple type but not these.

collection = {1,2,2,2,"hello","world","world",4}
print(collection)
print(len(collection))

coll = set()   #empty set
coll2 = {}   #empty dictionary

'''
Set Methods:
set.add(element) --> adds an element
set.remove(element) --> removes the element
set.clear() --> empties the set
set.pop() --> removes a random value
set.union(set2) --> combines both set values and returns new
set.intersection(set2) --> combines common values and returns new
'''

dictionary = {
    "cat" : "an animal",
    "table" : ["a piece of furniture", "list of facts and figures"]
}

