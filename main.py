#int list
from unittest import expectedFailure

pending_tasks =[]
completed_tasks=[]

available_id=1

#boolean dict
is_completed={}

#str dict
tasks_name={}
tasks_description={}


def print_tasks_list(list,type):
    # type="pending" -> Pending Tasks List
    # type="complete" -> Completed Tasks List
    if type=="pending":
     print("Pending Tasks List :-\n\n")
    else :
     print("Completed Tasks List :-\n\n")

    print(f"{'Task ID':<20}{'Task Name':<40}",'Task Description')
    print(150 * "-")

    new_list=[]
    for id in list:
        if (id in is_completed) and (is_completed[id] == (type=='complete')):
            print(f"{id:<20}{tasks_name[id]:<40}", tasks_description[id])
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
    pending_tasks.append(available_id)
    is_completed[available_id]=False
    tasks_name[available_id]=new_task_name
    tasks_description[available_id]=new_task_description
    available_id+=1
    return



#3
def mark_task():
    try:
      id=int(input("Enter task ID to mark as completed:\n-->"))
    except:
      print("invalid input\n")
      return
    if id not in is_completed:
      print("This task does not exist.\n")
      return

    is_completed[id]=True
    completed_tasks.append(id)
    return

#4
def delete_task():

    try :
       id = int(input("Enter task ID to delete:\n-->"))
    except:
       print("invalid input\n")
       return

    print('\n\n')
    if id not in is_completed:
        print("This task does not exist.\n")
        return

    del is_completed[id]
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



print("\n\n--------------The Command Line Interface has been Closed--------------\n")
