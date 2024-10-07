# Import functions
import taskManagerFunctions

# If this variable is True, the program will keep running.
running = True

# The list that will contain all tasks
all_tasks = []

while(running):

    print("1: Add a task \n2: Show task list \n3: Mark a task as completed \n4: Exit the program")
    # Registers the user's input
    user_input = str(input("Press 1, 2, 3 or 4: "))
    match user_input:
        case '1':
            taskManagerFunctions.addTask(input("Enter the name of the task: "), all_tasks)
        case '2':
            print(f"")
        case '3':
            taskManagerFunctions.completeTask(all_tasks, int(input("What task do you want to mark as completed ? (enter task number): ")))
        case '4':
            running = False