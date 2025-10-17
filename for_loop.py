my_heros = ["Dad","Mom","Grandpa","Grandma"]
for hero in my_heros:
    print("Thank you for everything", hero)



# Print only the even number from 1 t0 10 from the list
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    if (num%2==0):
        print(f"even number: {num}") # f string alllows us to embed expressions and variable inside string literals using {}
    else:
        print("Odd number:",num) 

# Calculate the sum of all numbers in the list
list_sum = 0
for num in numbers:
    list_sum += num
print("Sum of the list is:", list_sum)        

# for loops in strings
#my_string = "Hello World"
         #Or
for char in "Hello World":
    print(char) 

# tuples 
my_tuple = (1,2,3,4,5)
for item in my_tuple:
    print(item)    

#tuple unpacking in for loops or tuples inside a list
my_list_of_tuples = [(1,2),(3,4),(5,6)]
for (a,b) in my_list_of_tuples:
    print( a)
    print( b)


players_from_team = [("Messi",10),("Ronaldo",7),("Neymar",11)]
for (player,number) in players_from_team: 
    print(f"Goat Player: {player} their  Number: {number}")  



# Dictionary iteration
d = {"Gafadi":"Krishal","Bagwan":"Ramey","Loki":99}
# by default when you iterate through a dictionary it will give you only keys
for item in d:
    print(item)
#if you want to iterate keys and values both then you can use .items() method
for (key,value) in d.items():
    print(f"Key is: {key} and Value is: {value}")   

# if you want to print only values
for value in d.values():
     print("Value is:",value) 

# similar methods in dictionary are
# .keys() - to get all keys only
# .values() - to get all values only
# .items() - to get both keys and values   
#       
# for manxe in d:
#     # print("Key:",key)
#     # print("Value:",d[key])
#     # key lai chai variable le  access garxa tara value lai dictionary variable le access garxa 
#     # print(f"yo {manxe} {d[manxe]} ho")
#     break

# # another method for printing values only
# for (key,value) in d.values():
#     print("Value is:",value)
   