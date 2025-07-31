this code is a sort of "organized version" of the "best version" file to make it easier to read the code
print("(TO DO LIST)")  #To do list is output
date = "8/3/2025"  #pre-set date
print(f"{date:>14}")  #right-aligning the date
tasks = ["Complete Homework", "Do the dishes", "Walk the dog", "Prepare your food"]  #already existing list of tasks
Time = ["18-20", "13-13.30", "12-13", "15-17"]  #pre-set time for each task
for item1, item2 in zip(Time, tasks):  #to allow lists to be displayed next to each other
    print(f"{item1.ljust(13)} {item2}")

#This is what the user sees on the initial code run
Date_Enter = input("Would you like to enter a new date? please answer with \"Yes\" or \"No\"\n")  #user is asked if he wants a new date
while Date_Enter != "Yes" and Date_Enter != "No":
    Date_Enter = input("Please make sure to only answer using \"Yes\" or \"No\"\n")
while True:  #loop the code infintely until break
    if Date_Enter == "Yes":
        date = input('Enter the date that you want to add: ')  #user adds a date
    
#user enters a new date if he/she wants to
        New_List = input("Would you like to enter a new list? Please answer with \"Yes\" or \"No\"\n") #user is asked if he wants to enter a new list
        while New_List != "Yes" and New_List != "No":  #validating the answer to making a new list
            New_List = input("Please answer using \"Yes\" or \"No\"\n")
        if New_List == "Yes":  #creating a new list
            tasks = []
            Time = []
            count_tasks = int(input("How many tasks would you like to enter?\n")) #user enters the number of tasks to add
            count = 0
            while count < count_tasks:
                print("Please enter task number:", count + 1)
                New_Task = input()
                tasks.append(New_Task)
                added_time = input("When would you like to do this certain task?\n")
                Time.append(added_time)
                count = count + 1

#user enters a new list and makes new task(s) if he/she wants to do so
    print(f"{date:>14}")
    choice = int(input('(TO DO LIST)\nChoose the following options: \n1 : Add a new task \n2 : Remove a task \n3 : view your tasks\n'))  #user selects an option
    while choice < 1 or choice > 3:  #validate the option chose
    	choice = int(input("Invalid option, try again\n"))  #user re-enters the choice when the choice entered is invalid
    if choice == 1:  #option 1 adds a new task at the end of the list
    	added_task = input("What is the task you want to add?\n")
    	tasks.append(added_task)
    	added_time = input("When would you like to do this certain task?\n")
    	Time.append(added_time)
    	print("Task is updated! Here is the new list:")
    	for item1, item2 in zip(Time, tasks):  #to allow lists to be displayed next to each other
            print(f"{item1.ljust(13)} {item2}")


#user adds a new task if he/she wants to
    elif choice == 2:  #removes a task from the list
    	print("point out the position of the task that you want to remove from the following list\n", tasks)
    	number_remove = int(input())  #user inputs the position of the task to remove
    	del tasks[number_remove - 1]  #task is deleted


#this what the user makes use of to remove a task
    else:  #option 3 is to view the tasks
        print('here is the following list of tasks:')
        for item1, item2 in zip(Time,tasks):
            print(f"{item1.ljust(13)} {item2}")


#the user outputs what the list of tasks contain
    continuation = input("Do you want to continue with further options? Enter \"Yes\" or \"No\"\n")  #user chooses whether to choose more options or stop the program
    while continuation != "Yes" and continuation != "No":
        continuation = input("Invalid response. Answer again, please\n")
    if continuation == "No":
        Date_Enter = input("Do you want to enter a new date? Answer with \"Yes\" or \"No\"\n")  #user is asked if he wants to enter a new date
        while Date_Enter != "Yes" and Date_Enter != "No":  #validate the answer of the user to enter a new date or not
            Date_Enter = input("please make use of options \"Yes\" or \"No\" with correct spelling and capitalization")
        if Date_Enter == "No":
            break

#user is asked to continue or not with the code and add a new date and the whole program cycle repeats after the "while True" part
