# mylist = [1,2,3,4,5]

# mylist.pop()
# print(mylist)
# # Output: [1, 2, 3, 4]

# mylist.insert(4)
# print(mylist)
# Output: [1, 2, 3, 4, 4]

#def keyword
# sanke casing is all lowercase with underscores between words
# def name_of _function():
name = "nischal"
def say_hello(name):
    '''A function that prints Hello ''' # optional: multiline comment to describe function
    print(f"Hello, {name}")  
say_hello(name)
# Output: Hello


# add function
def add(n1, n2):
    return n1 + n2
result = add(5, 7)
print(result)