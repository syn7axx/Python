#The application doesn’t support saving state to local storage.
saved = {}

#add task function        
def addtask(task,status='Pending!'):
        save = saved[task] = status
        print('Task added sucessfully!')
        return save

#task deleting function
def delete():
        del saved[input('Task name>> ')]
        print('Deleted Sucessfully!')

while True:        
    print('\nWhat you want to do?\n----------------------------\nAdd / Remove / Clear / Quit\n [M] to mark task ad done!\n----------------------------')
    action = str(input('> ')).upper()
    if (action=="ADD"):
        task = str(input('Add task> '))
        addtask(task)
        for x,i in enumerate(saved.items(),start=1):
            print(x,i)
        
    elif (action=='REMOVE'):
            if saved:
                delete()
            else:
                print('No task found!\n')
            for x,i in enumerate(saved.items(),start=1):
                print(x,i)
    
    elif (action=='M'):
        print('\nPut Task Name Or Type [all] to mark all tasks as done!')
        item_name = str(input('>>  '))
        if saved:
            if (item_name=='All' or item_name=='all'):
                cop = saved.copy()
                for i in cop.keys():
                              saved.clear()
                              done = saved[i] = 'done'
                              print('Currunt Tasks!')
                              print(saved)
                              
            else:
                saved[item_name] = 'Done!'
                for x,i in enumerate(saved.items(),start=1):
                        print(x,i)
        else:
            print('No Task Found!')
        
    elif (action=='CLEAR'):
        saved.clear()
        print('Current Tasks! ')
        print(saved)
        
    elif (action=='QUIT'):
        break
    
    else:
        print('Invalid Input!\n')