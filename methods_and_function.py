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

#even and odd number check using function
def even_odd_checker(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
result = even_odd_checker(4)
print(result)
# Output: Even    

# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST
def check_even_list(num_list):
    for n in num_list:
        if n % 2 == 0:
            return True
    return False    
result = check_even_list([1,3,5,10,7])
print(result)


#return all the even numbers in a list
def return_even_numbers(num_list):
    even_numbers = []
    for n in num_list:
        if n % 2 == 0:
            even_numbers.append(n)
        else:
            pass    
    return even_numbers
result = return_even_numbers([1,2,3,4,5,6,7,8,9,10])
print(result)

#tuples unopacking in functions
# find the employee of the month from a list of tuples

work_hours = [("Nischal", 100), ("Loki", 200), ("Thor", 150)]
def employee_of_the_month(work_hours):
    current_max = 0
    employee_of_month = ""
    for (employee, hours) in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass    
    return (employee_of_month, current_max)
result = employee_of_the_month(work_hours)
print(f"Employee of the month is: {result[0]} with hours: {result[1]}")