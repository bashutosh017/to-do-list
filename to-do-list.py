tasks=[]

def add_list():
    add_task=input("Enter Your Task: ")
    tasks.append(add_task)
    print("Task added successfully")

def remove_task():
    
    if len(tasks)==0:
        print("No task has been yet")
    else:
        try:
            index=(int(input("Enter the task no. want to remove: ")))-1
            if 0<=index<len(tasks):
                tasks.pop(index)
                print(f'{tasks[index]} is removed successfully')

            else:
                print("enter a correct index no.")
        except ValueError:
            print("enter a correct value")
    
def view_list():
    if len(tasks) == 0:
        print("No task added yet")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

if  __name__=='__main__':
    print("Welcome to your to-do-list")
    while True:
        print("""Enter The Option you want to proceed:
            1.To add a task
            2.To remove a task
            3.To view the tasks
            4.To exit""")
        
        
        
        try:
            option=int(input("Enter the Option here: "))
            if option==1:
                add_list()
            elif option==2:
                remove_task()
            elif option==3:
                view_list()
            elif option==4:
                break
            else:
                print("Enter a valid option")
        except ValueError:
            print("Please Enter Integer Only")