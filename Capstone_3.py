# Libraries
import datetime
from datetime import datetime
from datetime import date


# Dictionaries
user_dict = {}
tasks_dict = {}

#Global - populating dictioary and setting today's date
count = 1
with open('tasks.txt', 'r+') as f2:

    for line in f2:
        newline = line.strip('\n') 
        split_line = newline.split(", ")  
        tasks_dict[count] = split_line 
        count += 1 

today = datetime.today()

with open("user.txt", "r") as user_file:
    for line in user_file:
        username, password = line.strip("\n").split(", ")
        user_dict[username] = password

# Functions

#Function to register a user if logged in as admin. 
# Checks for username already exisiting and that the password is entered twice correctly. 
def reg_user():
    if user_name == "admin":
        file = open("user.txt", "a")
        new_username = input("\nPlease enter your new username: ")
        while new_username in user_dict:
            print("Username already exisists. ")
            new_username = input("\nPlease enter your new username: ")

        new_password = input("\nPlease enter your new password: ")
        pass_check = input("\nPlease re-enter your new password: ")

        if new_password == pass_check:
            file.write("\n" + new_username + ", " + new_password)
            print("\nYour new details have been saved")

        elif new_password != pass_check:
            print("\nThe passwords you have entered do not match.")
            new_password = input("\nPlease enter your new password: ")
            pass_check = input("\nPlease re-enter your new password: ")
        
            if new_password == pass_check:
                file.write("\n" + new_username + ", " + new_password)
                print("\nYour new details have been saved")

        file.close()
            
    else:
        print("\nYou are not authorised to register new users.\n")

#Function to add a task requesting the name, titile, description and due date. 
#Formats the date and updates task list and dictionary. 
def add_task():
    print("Please enter the following information to add the task: ")
    name = input("\nTeam member the task is being assigned to: ")
    title = input("\nTitle of the task: ")
    description = input("\nDescription of the task: ")
    task_completed = "No"
    today = datetime.today()
    assigned_date = today.strftime('%d %b %Y')
    date_format = input("\nDue date (DD MM YYYY): ")
    date_list = date_format.split()
    numbers_date = [int(x) for x in date_list]
    due_date = date(numbers_date[2], numbers_date[1], numbers_date[0]).strftime('%d %b %Y')
    task_list = [name, title, description, assigned_date, due_date, task_completed]
    tasks_dict[f"Task {count} details:"] = task_list
   
    with open ('tasks.txt', 'r+') as f2:
        for key in tasks_dict:
            line_string = str(tasks_dict[key])
            
            bad_chars = ["[", "]", "\'"]

            for i in bad_chars:
                line_string = line_string.replace(i, "")

            f2.write(line_string + '\n')
    print("\nYour task has been added successfully. ")

#Function to view all tasks
def view_all():
    file = open("tasks.txt", "r+")
    task_count = 1

    lines = file.readlines()
    for line in lines:
        task_data = line.strip().split(", ")
        print(f"\n————————————Task number {task_count}————————————")
        print("\nTask:\t\t" + task_data[1] + "\nAssigned to:\t" + task_data[0] + "\nDate assigned:\t" + task_data[3] + "\nDue date:\t" + task_data[4] + "\nTask complete?\t" + task_data[5] +"\nTask description:\n" + task_data[2])
        task_count +=1
        file.close()
    print("\n————————————End of Tasks———————————————")

#Function to view numbered tasks assigned to the user logged in
#Allows the task to be selected by its number and edited to change the user, due date or completed value
def view_mine(user_name):
    task_count = 0
    for key in tasks_dict:
        task_count +=1
        if user_name == (tasks_dict[key][0]):

            print(f"\n———————————Task number:{task_count}——————————————")
            print(f"\nTask title: \t{str(tasks_dict[key][1])}\nAssigned to: \t{str(tasks_dict[key][0])}\nIs complete: \t{str(tasks_dict[key][5])}\nDue date: \t{str(tasks_dict[key][4])}\nTask Description: \n{str(tasks_dict[key][2])}")
            print("\n—————————————————————————")

    task_choice = int(input("\nSelect a task by entering the task number: "))

    user_task = int(input(f"\n———————[SELECT AN OPTION]———————\n1 - Edit due date\n2 - Mark as complete\n3 - Edit assigned to\n-1 - Return to main menu\n\nChoice: "))
    
    if user_task != -1:
        if tasks_dict[task_choice][-1] != "yes":
            if user_task == 1:
                new_due = input("\nPlease enter the new due date using the following format - DD MMM YYYY: ")
                tasks_dict[task_choice][-2] = str(new_due)
                all_task = [ ", ".join(t) for t in tasks_dict.values()]
                with open("tasks.txt", "w") as task_file:
                    task_file.write("\n".join(all_task))
                print("\nYour task has been update.")

            elif user_task == 2:
                tasks_dict[task_choice][-1] ="yes"
                all_task = [ ", ".join(t) for t in tasks_dict.values()]
                with open("tasks.txt", "w") as task_file:
                    task_file.write("\n".join(all_task))
                print("\nYour task has been updated.")

            elif user_task == 3:
                updated_user = input("\nEnter the name of the user the task is being reassigned to: ")
                tasks_dict[task_choice][0] = str(updated_user)
                all_task = [ ", ".join(t) for t in tasks_dict.values()]
                with open("tasks.txt", "w") as task_file:
                    task_file.write("\n".join(all_task))
                print("\nYour task has been updated.")
        else:
            print("\nThe task is already complete and cannot be edited.")

#User overview and task overview files are read and printed (they are generated first if they don't exist)
def stats():
    file = open("user.txt", "r+")
    data = file.read()
    line = data.splitlines()
    file.close()
    file = open("tasks.txt", "r+")
    data = file.read()
    line = data.splitlines()
    file.close()

    print("""\n____________________________________________________

The task overview report is as follows:
____________________________________________________\n""") 

    with open('task_overview.txt', 'r+') as f3:  
        for line in f3:
            print(line)  

    print("""\n_____________________________________________________

The user overview report is as follows:
_____________________________________________________\n""")  

    with open('user_overview.txt', 'r+') as f4: 
        for line in f4:
            print(line)  

    print("""\n______________________________________________________

End of Statistics Reports
______________________________________________________\n""") 

#Function to generate reports for all the tasks in the task.txt file
#Also generates a user overview file that shows all the tasks and the number compelte and incomplete for each user. 
def gen_reports():
    users = []
    task_file = open('tasks.txt', 'r')
    task_list = task_file.readlines()
    task_file.close()
    with open("tasks.txt", "r") as file1:
        tasks = [line.split(", ") for line in file1]
    with open("user.txt", "r") as file2:
        for line in file2:
            users.append(line.split(None, 1)[0].strip(","))

    given_user = []
    total_tasks = len(tasks)
    overdue = 0
    incomplete_tasks = 0
    complete_tasks = 0
    total_users = len(users)
    tasks_assigned = 0

    with open("user_overview.txt", "w") as f5:
        f5.write(f"The total number of users registered with task_manager.py is {total_users}.\nThe total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}.\n")
    
    for user in users:
        for line in task_list:
            data_list = line.strip("\n").split(', ')
           
            if user == data_list[0]:
                tasks_assigned += 1
                given_user.append(user)
                if data_list[-1] == "yes":
                    complete_tasks +=1
                else:
                    incomplete_tasks +=1
                    if datetime.strptime(data_list[-2], "%d %b %Y") < today:
                        overdue +=1
                    else:
                        continue
            else:
                continue

        if tasks_assigned != 0:
            percent_tasks = round((tasks_assigned/total_tasks) * 100, 2)
            percent_complete = round((complete_tasks/tasks_assigned) * 100, 2)
            percent_incomplete = round((incomplete_tasks/tasks_assigned) * 100, 2)
            percent_overdue = round((overdue/tasks_assigned)* 100, 2)

            with open("user_overview.txt", "a+") as f6:
                f6.write(str(given_user[0]) + " has " + str(tasks_assigned) + " tasks assigned to them.\nThey have " + str(percent_tasks) +"%" + " of the tasks assigned to them.\nThey have completed " + str(percent_complete) + "%" +"  of their tasks.\nThey sill have " + str(percent_incomplete) + "%" + " of their tasks to complete.\n" + str(percent_overdue) + "%" + " of their incomplete tasks are overdue.\n\n")
        
        else:
            with open("user_overview.txt", "a+") as f6:
                f6.write(str(user) + " does not have any tasks.\n")
                
        given_user = []
        overdue = 0
        incomplete_tasks = 0
        complete_tasks = 0
        tasks_assigned = 0
    
    tasks_percent_overdue = 0

    for line in task_list:
        data_list = line.strip("\n").split(', ')
        if data_list[5].lower() == "yes":
            complete_tasks += 1
        elif data_list[5].lower() == "no":
            incomplete_tasks += 1
            percent_incomplete = round(((incomplete_tasks/total_tasks)*100),2)
            due_date = data_list[4]
            due_date_object = datetime.strptime(due_date, "%d %b %Y")
            current_date = datetime.today()
            if due_date_object < current_date:
                overdue += 1
                tasks_percent_overdue = round(((overdue/total_tasks)*100),2)

    with open("task_overview.txt", "w") as task_ov:
        task_ov.write(f"The total number of tasks is {total_tasks}.\nThe number of complete tasks is {complete_tasks}.\nThe number of incomplete tasks is {incomplete_tasks}.\nThe number of incomplete and overdue tasks is {overdue}.\nThe percentage of overdue tasks is {tasks_percent_overdue}%.\nThe percentage of incomplete tasks is {percent_incomplete}%.")
        print("\nYour report is available to view.")


# Main - calls functions above based on user input.

while True:
    user_name = input("Please enter your username: ")
    resp = user_dict.get(user_name, "Invalid username")
    if resp != "Invalid username":
        user_password = input("Please enter your password: ")
        if user_password == user_dict[user_name]:
            print(f"Welcome {user_name}.")
            break
        else: 
            print("You have entered an invalid password.")
    else:
        print(resp)

while True:
    if user_name == "admin":
        menu = input("\nSelect one of the following options below:\ns - Statistics\nr - Registering a user\na - Adding a task\nva - View all tasks\nvm - View my task\ngr - Generate reports\ne - Exit\nChoice: ").lower()
    else:
        menu = input("\nSelect one of the following options below:\nr - Registering a user\na - Adding a task\nva - View all tasks\nvm - View my task\ne - Exit\nChoice: ").lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine(user_name)
    elif menu == 's':
        stats()
    elif menu == 'gr':
        gen_reports()
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")
        