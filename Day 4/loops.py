# while loop: 
'''
while condition:
    #some work
'''

count = 1
while count <= 5:
    if(count == 1):
        print("Printed", count, "time.")
    else:
        print("Printed", count, "times.")
    count += 1

#printing numbers from 1 to 100:
i = 1
while i <= 100:
    print(i)
    i += 1

#printing the multiplication table of a number n:
num = int(input("Enter a number: "))
j = 1
while j<=10:
    print(num, "*", j, "= ", num*j)
    j += 1

#break: used to terminate the loop when encountered
# continue: terminates execution in the current iteration and continues execution of the loop with the next iteration 


#for loops are used for sequential traversal. For traversing lists, tuples, strings etc

'''
for element in list:
    #some work

for element in list:
    #some work

else:
    #some work when loop ends
'''

list1 = [1,4,9,16,25,36,49,64,81,100]
for val in list1:
    print(val)
    if(val == 25):
        break

#range() function:
#range function returns a sequence of numbers, starting from 0 by default and increments by 1 (by default) and stops before a specified number.

#range(5): start 0, stop 5, step 1
#range(1,5): start 1, stop 5, step 1
#range(1,5,2): start 1, stop 5, step 2
# 
for i in range(10):
    print(i)

#pass is a null statement that does nothing. It is used as a placeholder for future code.

#sum of first n numbers using while loop:
num = 1
sum = 0
n = int(input("Enter your number: "))
while num <= n:
    sum += num
    num += 1
print(sum)


#factorial of first n numbers using for loop
n = int(input("Enter the number: "))
product = 1
for i in range(n,1,-1):
    product = product*i
print(product)



