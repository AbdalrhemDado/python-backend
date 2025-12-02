#int list
pending_tasks =[]
completed_tasks=[]

available_id=1

#boolean dict
is_deleted={}
is_completed={}

#str dict
tasks_name={}
tasks_description={}



def print_tasks_list(list,type):
    # type=False -> Pending Tasks List
    # type=True -> Completed Tasks List
    if not type:
     print("Pending Tasks List :-\n\n")
    else :
     print("Completed Tasks List :-\n\n")

    #print("Task ID",10*" ","Task Name",30*" ","Task Description")

    print(f"{'Task ID':<20}{'Task Name':<40}",'Task Description')
    print(150 * "-")


    new_list=[]
    for id in list:
        if not is_deleted[id] and is_completed[id] == type:
            print(f"{id:<20}{tasks_name[id]:<40}", tasks_description[id])
            print(id)
            new_list.append(id)

    list[:]=new_list
    print("\n")


#1
def task_list():
    print("Enter one of these by first character:-")
    print("a. Show Pending Tasks List.")
    print("b. Show Completed Tasks List.")
    print("c. Show Pending Tasks List and Completed Tasks List.")
    print("0. Return to Main Menu.")
    x=str(input("-->"))
    print('\n\n')
    if x=='a' :
        print_tasks_list(pending_tasks,False)
    elif x=='b':
        print_tasks_list(completed_tasks,True)
    elif x=='c':
        print_tasks_list(pending_tasks,False)
        print_tasks_list(completed_tasks,True)
    elif x=='0':
        return
    else :
        print("it's wrong input please try again :")
        task_list()



#2
def add_task():


    new_task_name=str(input("Enter the name of new task :\n"))
    if len(new_task_name)==0:
        print('it\'s empty enter try again:-')
        add_task()

    new_task_description=str(input("Enter the description of new task :\n"))

    if len(new_task_description)==0:
        print('it\'s empty enter try again:-')
        add_task()

    global available_id
    pending_tasks.append(available_id)
    is_deleted[available_id]=False
    is_completed[available_id]=False
    tasks_name[available_id]=new_task_name
    tasks_description[available_id]=new_task_description
    available_id+=1
    return



#3
def mark_task():
    id=int(input("Enter task ID to mark as completed:\n-->"))
    print('\n\n')
    if id>=available_id or id<=0 or is_deleted[id]:
        print("This task does not exist.\n")
        return
    is_completed[id]=True
    completed_tasks.append(id)
    return

#4
def delete_task():
    id = int(input("Enter task ID to delete:\n-->"))
    print('\n\n')
    if id>=available_id or id<=0 or is_deleted[id]:
        print("This task does not exist.\n")
        return
    is_deleted[id]=True
    del tasks_name[id]
    del tasks_description[id]
    return




print("-----------------Command Line Interface------------------\n\n")

while(True):
    print("Enter one of these by first character:-\n")
    print("1. Show Tasks Lists.")
    print("2. Add Task.")
    print("3. Mark Task As Completed.")
    print("4. Delete Task.")
    print("5. Exit.\n")
    choice=int(input("-->"))
    print('\n\n')
    if choice==1 :
        task_list()
    elif choice==2:
        add_task()
    elif choice==3:
        mark_task()
    elif choice==4:
        delete_task()
    elif choice==5:
        break
    else :
        print("it's wrong input please try again.\n")



print("\n\n--------------The Command Line Interface has been Closed--------------\n")
