# range(start,stop,step )

# for num in range(1, 10, 2):
#     print(num)


print(list(range(5, 10, 2)))  #output : [5, 7, 9]

# format operator
index_count = 0
for letter in "abcde":
    print("At index {} the letter is: {}".format(index_count, letter))
    index_count += 1

# At index 0 the letter is: a
# At index 1 the letter is: b
# At index 2 the letter is: c
# At index 3 the letter is: d
# At index 4 the letter is: e

indexCount = 0
word = "abcde"
for letter in word:
    print(word[indexCount])
    indexCount += 1

# a
# b
# c
# d
# e

# enumerate() function  this funcction return index and value both
word = "abcde"
for item in enumerate(word):
    print(item)
# Output:
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

for index, letter in enumerate(word):
    print(f"At index {index} the letter is: {letter}")

    #output:
# At index 0 the letter is: a
# At index 1 the letter is: b
# At index 2 the letter is: c
# At index 3 the letter is: d
# At index 4 the letter is: e

# zip() function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [100, 200, 300]
for item in zip(list1, list2, list3):
    print(item)
# Output:
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)

print(list(zip(list1, list2, list3)))
# Output: [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300)]

for a, b, c in zip(list1, list2, list3):
    print(f"Numbers: {a}, Letters: {b}, Hundreds: {c}")
    # Output:
# Numbers: 1, Letters: a, Hundreds: 100
# Numbers: 2, Letters: b, Hundreds: 200
# Numbers: 3, Letters: c, Hundreds: 300
    print("Done with all the items!")

# in operators     

print('x' in [1,2,3]) #False
print('x' in ['x','y','z']) #True

d ={"myKey":21}
print(21 in d.values())  #True

print(21 in d.keys()) #False

# min() and max() functions
mylist = [10,20,30,40,50]
print(min(mylist))  #10
print(max(mylist))  #50

# to import function from a library use import statement
from random import shuffle
mylist = [1,2,3,4,5]
shuffle(mylist)
print(mylist)  #output will be random like [3, 5, 1, 4, 2]  

# grapping random number
from random import randint
print(randint(0,100))  #output will be random number between 0 to 100 like 57

#Taking input from user
result = input("Enter your  name: ")
print(f"Ohh your name is {result}")

# input function always return string value
num1 = input("Enter first number: ")
print(type(num1))  #str
print(int(num1) )  #error