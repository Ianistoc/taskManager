# Import functions
import taskManagerFunctions

# If this variable is True, the program will keep running.
running = True

# The list that will contain all tasks
allTasks = []

while(running):

    print("1: Add a task \n2: Show task list \n3: Mark a task as completed \n4: Exit the program")
    # Registers the user's input
    user_input = str(input("Press 1, 2, 3 or 4: \n"))
    match user_input:
        case '1':
            taskManagerFunctions.addTask(input("Enter the name of the task: \n"), allTasks)
        case '2':
            print("Here are your tasks:")
            for task in allTasks:
                print(f"{task[0]}. {task[1]} | {taskManagerFunctions.boolToReadable(task[2])} \n \n")
        case '3':
            taskManagerFunctions.completeTask(allTasks, int(input("What task do you want to mark as completed ? (enter task number): ")))
        case '4':
            running = False