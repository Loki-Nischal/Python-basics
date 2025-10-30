

while True:
    user_action = input("type add,show,edit,complete or exit: ")
    user_action = user_action.strip() #it (strip) remove any whitespace from the user input

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"
            file = open('todos.txt','r')
            todos = file.readlines() #readlines function returns a list
            file.close()

            todos.append(todo)

            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()

 
        case "show":
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()

            for index,item in enumerate(todos): #enumerate function returns both the index and the item from the list
                print( f"{index+1}.{item}")

        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)  #subtracting 1 because list index starts at 0
                


        case "edit":
            number = int(input("Number of the todo to edit: "))
            existing_todo = todos[number - 1]
            print(f"You are editing: {existing_todo}")
            new_todo = input("Enter the new todo: ") + "\n"
            file = open('todos.txt','r')
            todos = file.readlines()
            file.close()

            todos[number - 1] = new_todo 
      

        case "exit":
            break

print ("Bye!")  


#Note strings are immutable, meaning you cannot change them in place. Instead, you create a new string and assign it to the same variable name if needed.
#But list are mutable, meaning you can change their content without changing their identity.