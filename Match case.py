todos = []

while True:
    user_input = input("Enter Add, Show, Edit, Complete and Exit: ")

    match user_input:
        case 'Add':
            todo = input("Enter Todo: ")
            todos.append(todo)
        
        case 'Show':    
            for index,item in enumerate(todos): 
                row = f'{"index"}-{"item"}'
                print(row)

        case 'Edit':
            number = int(input("Enter Number of Todo to Edit: "))
            number = number - 1
            new_todos = input("Enter New Todo: ")
            new_todos = todos[number]
        
        case 'Complete': 
            number = int(input("Enter Number Of Todo Completed: "))
            number.pop(number - 1)

        case 'Exit':
            break
print("Bye")

        
        



        
            

        



    


        

    
  
    




            

       

            
            

