#Program to enter names of movies and store them in a list
# print("Enter 3 of your favourite movies: ")
# mov1 = input()
# mov2 = input()
# mov3 = input()
# l1 = [mov1, mov2, mov3]
# print("Your 3 favourite movies are: ",l1)

print("Create your list: ")
a = input()
b =input()
c = input()
d = input()
l2 = [a,b,c,d]
l3 = l2.copy()
print(l2)
if(l3.reverse() == l2):
    print("The list is palindrome.")
else:
    print("The list is not palindrome.")
