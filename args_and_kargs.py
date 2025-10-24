def myfunc(a,b,c=0,d=0,e=0):
    #returns 5% of the sum of a and b
    return sum((a,b)) * 0.05
result = myfunc(40,600,200,30,50)
print(result)  # Output: 5.0    

def myfunc2(*args):  #we can also write (*spam) instead of args #takes parameter as argument 
    print(args)    # Output: (40, 600, 200, 30, 50)
    return sum(args) * 0.05
result = myfunc2(40,600,200,30,50)
print(result)  # Output: 44.0

def myfunc3(*args):
    for item in args:
        print(item)
result = myfunc3(1,2,3,4,5)
# Output:
# 1 
# 2
# 3
# 4
#   5           


#**kargs  we can pass key value pairs as arguments
def myfunc4(**kargs): # *kargs returns a dictionary
    print(kargs)  # Output: {'name': 'Nischal', 'age': 24}
    if 'name' in kargs:
        print(f"Hello, {kargs['name']},you are {kargs['age']} years old  ")  
    else:
        print("Hello")
result = myfunc4(name="Nischal", age=24)
print(result)  
# Output: Hello, Nischal,he is 24 years old

# using both args and kargs in a function
def myfunc5(*args, **kargs):
    print(args)  
    print(kargs)  
    print("Hello, i would like {} {}".format(args[0],kargs['food']))
   
result = myfunc5(10,20,30,fruit="apple", food="pizza", animal="dog")
# Output:   
# (10, 20, 30)
# {'fruit': 'apple', 'food': 'pizza', 'animal': 'dog'}
# Hello, i would like 10 pizza




