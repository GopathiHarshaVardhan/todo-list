todo_list=[]


def add_task():
    task=input('Enter the task:')
    todo_list.append({'task':task,'status':'pending'})
    print('new task added successfully')
def view_tasks():
    print('your todo list:')
    if len(todo_list)==0:
        print('no pending tasks')
    else:
        for index,task in enumerate(todo_list,1):
            print(f"{index}:{task['task']}-{task['status']}")
    print('\n')
    
    
def remove_task():
    if len(todo_list)==0:
        print('list is empty')
    else:
        try:
            search_index=int(input('Enter the task number that you want to remove:')) - 1
            if 0 <= search_index < len(todo_list):
                removed_task=todo_list.pop(search_index)
                print(f"Task Removed:{removed_task['task']} ")
            else:
                print('Invalid task number.')
        except ValueError:
            print('Please enter a valid task number')
            
            

def mark_done():
    if len(todo_list)==0:
        print('list is empty')
    else:
        try:
            search_index=int(input('Enter the task number that you want to mark as complete:')) - 1
            if 0 <= search_index < len(todo_list):
               todo_list[search_index]['status']='done'
               print(f"task {todo_list[search_index]['task']} has been marked as done")
                             
            
            else:
                print('Invalid task number.')
        except ValueError:
            print('Please enter a valid task number')    
    

    
                    
def menu():
    while(True):
        print('_____MAIN MENU_____')
        print('1. Add a new  task')
        print('2.view all tasks')
        print('3.remove a task')
        print('4.mark a task as completed')
        print('5.exit')
        
        choice=input('Enter your choice:')
        if choice=='1':
            add_task()
        elif choice=='2':
            view_tasks()
        elif choice=='3':
            remove_task()
        elif choice=='4':
            mark_done()
        elif choice=='5':
            print('Exiting the program....')
            exit()
            
        else:
            print('Invalid choice. Please try again.')
menu()