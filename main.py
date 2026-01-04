from Task import Task

pending_tasks= {}
completed_tasks= {}
available_id=1


def print_tasks_list(list,type):
    if type=="pending":
     print("Pending Tasks List :-\n\n")
    else :
     print("Completed Tasks List :-\n\n")

    print(f"{'Task ID':<20}{'Task Name':<40}",'Task Description')
    print(150 * "-")

    for task in list.values():
            print(task)

    print("\n")

#1
def task_list():
    print("Enter one of these by first character:-")
    print("a. Show Pending Tasks List.")
    print("b. Show Completed Tasks List.")
    print("c. Show Pending Tasks List and Completed Tasks List.")
    print("0. Return to Main Menu.")
    choice=str(input("-->"))
    print('\n\n')
    if choice=='a' :
        print_tasks_list(pending_tasks,"pending")
    elif choice=='b':
        print_tasks_list(completed_tasks,"complete")
    elif choice=='c':
        print_tasks_list(pending_tasks,"pending")
        print_tasks_list(completed_tasks,"complete")
    elif choice=='0':
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
    new_task = Task(available_id,new_task_name,new_task_description)
    pending_tasks[available_id]=new_task
    available_id+=1


#3
def mark_task():
    try:
      id=int(input("Enter task ID to mark as completed:\n-->"))
    except:
      print("invalid input\n")
      return

    if id not in pending_tasks:
      print("This task does not exist or has already been completed.\n")
      return

    completed_tasks[id]=pending_tasks.pop(id)


#4
def delete_task():

    try :
       id = int(input("Enter task ID to delete:\n-->"))
    except:
       print("invalid input\n")
       return

    print('\n\n')
    if id in pending_tasks:
        del pending_tasks[id]
    elif id in completed_tasks:
        del completed_tasks[id]
    else :
        print("This task does not exist.\n")

    return



print(12*"-","Command Line Interface",12*"-","\n\n")

while(True):
    print("Enter one of these by first character:-\n")
    print("1. Show Tasks Lists.")
    print("2. Add Task.")
    print("3. Mark Task As Completed.")
    print("4. Delete Task.")
    print("5. Exit.\n")
    try :
       choice=int(input("-->"))
    except:
       print("invalid input\n")
       continue

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


print("\n")
print(12*"-","The Command Line Interface has been Closed",12*"-")