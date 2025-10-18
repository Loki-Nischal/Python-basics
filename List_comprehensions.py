# List comprehensions are a unique way of quicjkly creating lists in Python.
# if you find yourself using a for loop to create a list, you can probably use a list comprehension instead.

mystring = "hello"
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
# Output: ['h', 'e', 'l', 'l', 'o']

Mylist =[letter for letter in mystring]
print(Mylist)
# Output: ['h', 'e', 'l', 'l', 'o']


My_list =[x for x in 'word']
print(My_list)
# Output: ['w', 'o', 'r', 'd']

My_numbers = [num for num in range(0,11)]
print(My_numbers)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Mlist = [num**2 for num in range(0,11)]
print(Mlist)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_numbers = [num for num in range(0,11) if num%2==0]
print(even_numbers)
# Output: [0, 2, 4, 6, 8, 10]

#Converting celcius to fahrenheit
celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp +32) for temp in celcius]
print(fahrenheit)
# Output: [32.0, 50.0, 68.0, 94.1]

# all we are doing here is faltening append functionality and getting rid of this append functionality
# if we use append functionality then 
Farenhite = []
for temp in celcius:
    Farenhite.append((9/5)*temp +32)
print(Farenhite)
# Output: [32.0, 50.0, 68.0, 94.1] gives same result

# we can use if and else statements inside list comprehensions as well but the order will be different
results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

# example of nested loop in list comprehensions
LList = []
for x in [2,4,6]:
    for y in [100,210,300]:
        LList.append(x*y)
print(LList)
# Output: [200, 420, 600, 400, 840, 1200, 600, 1260, 1800]  
# 
# Using list comprehension for the same nested loop
LLlist = [x*y for x in [2,4,6] for y in [100,210,300]]
print(LLlist)   
# Output: [200, 420, 600, 400, 840, 1200, 600, 1260, 1800]   

st ="print only the words that start with s in this sentence"
for word in st.split():
      if word[0]=='s':
        print(word)
# Output:
# start
# s
# sentence

s_t = "Print every word in this sentence that has an even number of letters"
for word in s_t.split():
    if len(word)%2==0:
        print(f"{word} is even!")


text = "apple banana orange"
result = text.split()  # Splits the string into a list of words
print(result)  # Output: ['apple', 'banana', 'orange']        