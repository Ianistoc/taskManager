# Import functions
import taskManagerFunctions

# If this variable is True, the program will keep running.
running = True

# The list that will contain all tasks
all_tasks = [['listName', 'number', False]]

while(running):

    print("1: Add a task \n2: Show task list \n3: Mark a task as completed \n4: Exit the program")
    # Registers the user's input
    user_input = str(input("Press 1, 2, 3 or 4: "))