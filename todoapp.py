def task():
    tasks = []  # Initialize the task list
    print("------Welcome to the task management app ------")
    
    # Get the number of tasks from the user
    total_task = int(input("Enter how many tasks you want to add = "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")  # Dynamically update the task number
        tasks.append(task_name)  # Add each task to the tasks list

    print(f"Today's tasks are:\n{tasks}\n")

    while True:
        # Ask for operation choice
        operation = int(input("Enter 1-ADD\n2-UPDATE\n3-DELETE\n4-VIEW\n5-EXIT: "))
        
        if operation == 1:
            # Add a new task
            add_task = input("Enter task you want to add: ")
            tasks.append(add_task)
            print(f"Task '{add_task}' has been successfully added.\n")
        
        elif operation == 2:
            # Update an existing task
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                update_new = input("Enter new task: ")
                ind = tasks.index(updated_val)  # Find index of the task to update
                tasks[ind] = update_new  # Update the task
                print(f"Task updated to '{update_new}'.\n")
            else:
                print(f"Task '{updated_val}' not found.\n")
        
        elif operation == 3:
            # Delete an existing task
            delete_task = input("Enter the task name you want to delete: ")
            if delete_task in tasks:
                tasks.remove(delete_task)  # Remove task from list
                print(f"Task '{delete_task}' has been deleted.\n")
            else:
                print(f"Task '{delete_task}' not found.\n")
        
        elif operation == 4:
            # View all tasks
            if tasks:
                print("Today's tasks are:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks available.\n")
        
        elif operation == 5:
            # Exit the program
            print("Exiting the task manager. Goodbye!")
            break  # Exit the loop and stop the program
        
        else:
            print("Invalid option. Please select a valid operation (1-5).\n")

# Call the function to run the task manager
task()
