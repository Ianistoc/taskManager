def addTask(taskName:str, list:list):
    '''The three values are:
    1st value: task number
    2nd value: task name
    3rd value: task completion (False = uncompleted ; True = completed)'''
    list.append([len(list)+1, taskName, False])
def completeTask(list:list, taskNumberSearch:int):
    for element in list:
        if element[0] == taskNumberSearch:
            element[2] = True
def boolToReadable(boolean:bool):
    if boolean:
        return "Completed"
    else:
        return "Not completed"