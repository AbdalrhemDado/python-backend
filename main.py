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



def Pending_Tasks_List():
    print("Pending Tasks List :-\n\n")
    print("Task ID",10*" ","Task Name",30*" ","Task Description")
    print(150 * "-")

    global pending_tasks
    new_list=[]
    for id in pending_tasks:
        if is_deleted[id]==False and is_completed[id]==False:
            print(id, (17-len(str(id)))*" ", tasks_name[id],(39-len(tasks_name[id]))*" ", tasks_description[id])
            new_list.append(id)

    pending_tasks=new_list
    print("\n")



def Completed_Tasks_List():
    print("Completed Tasks List :-\n\n")
    print("Task ID",10*" ","Task Name",30*" ","Task Description")
    print(150*"-")

    global completed_tasks
    new_list = []
    for id in completed_tasks:
        if is_deleted[id] == False and is_completed[id] == True:
            print(id, (17-len(str(id)))*" ", tasks_name[id],(39-len(tasks_name[id]))*" ", tasks_description[id])
            new_list.append(id)

    completed_tasks = new_list
    print("\n")


#1
def Task_List():
    print("Enter one of these by first character:-")
    print("a. Show Pending Tasks List.")
    print("b. Show Completed Tasks List.")
    print("c. Show Pending Tasks List and Completed Tasks List.")
    print("0. Return to Main Menu.")
    x=str(input("-->"))
    print('\n\n')
    if x=='a' :
        Pending_Tasks_List()
    elif x=='b':
        Completed_Tasks_List()
    elif x=='c':
        Pending_Tasks_List()
        Completed_Tasks_List()
    elif x=='0':
        return
    else :
        print("it's wrong input please try again :")
        Task_List()



#2
def Add_Task():
    new_task_name=str(input("Enter the name of new task :\n"))
    new_task_description=str(input("Enter the description of new task :\n"))
    global available_id
    pending_tasks.append(available_id)
    is_deleted[available_id]=False
    is_completed[available_id]=False
    tasks_name[available_id]=new_task_name
    tasks_description[available_id]=new_task_description
    available_id+=1
    return



#3
def Mark_Task():
    id=int(input("Enter task ID to mark as completed:\n-->"))
    print('\n\n')
    if id>=available_id or id<=0 or is_deleted[id]:
        print("This task does not exist.\n")
        return
    is_completed[id]=True
    completed_tasks.append(id)
    return

#4
def Delete_Task():
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

while(1):
    print("Enter one of these by first character:-\n")
    print("1. Show Tasks Lists.")
    print("2. Add Task.")
    print("3. Mark Task As Completed.")
    print("4. Delete Task.")
    print("5. Exit.\n")
    x=int(input("-->"))
    print('\n\n')
    if x==1 :
        Task_List()
    elif x==2:
        Add_Task()
    elif x==3:
        Mark_Task()
    elif x==4:
        Delete_Task()
    elif x==5:
        break
    else :
        print("it's wrong input please try again.\n")



print("\n\n--------------The Command Line Interface has been Closed--------------\n")
