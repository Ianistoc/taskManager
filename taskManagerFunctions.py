def addTask(taskName:str, list:list):
    '''The three values are:
    1st value: task number
    2nd value: task name
    3rd value: task completion (False = uncompleted ; True = completed)'''
    list.append([str(len(list)+1), taskName, False])