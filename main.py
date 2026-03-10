import json
from task import Task 
from datetime import datetime, date

tasks = list()
behaviour_stadistics = {"skipped_hard": 0, "postponed_hard": 0, "completed_hard":0}

# Opening the ("behaviour_stats.json") 
# However, if file is not found, a new behaviour_stadistics dictionary is created.
try:
    with open("behaviour_stats.json", "r") as f:
        behaviour_stadistics = json.load(f)
except FileNotFoundError:
    behaviour_stadistics = {"skipped_hard": 0, "postponed_hard": 0, "completed_hard": 0}

# Visual representation of the number of skipped/postponed/completed tasks at the beginning of the day.
print("Behaviour stats at start of day:", behaviour_stadistics)

number_of_tasks = int(input("Please eneter the number of tasks you would like to plan: "))

# For loop asks the user for all essential information 
for i in range(1,number_of_tasks+1):
    print(f"TASK NUMBER {i}")
    name = str(input(f"Task name nº{i}: "))
    hours = int(input("Enter number number of hours this task is expected to take: ")) * 60 
    minutes = int(input("Enter number number of minutes this task is expected to take: "))
    duration_minutes = hours + minutes
    difficulty = int(input("Enter the level of difficulty of the task (1 = Effortless - 5 = Extremely Hard): "))
    while True:
        if 1 <= difficulty <= 5:
            break
        else:
            difficulty = int(input("Please enter a number between  1 = Effortless & 5 = Extremely Hard"))
    deadline = str(input("Please enter the deadline date of this task (DD/MM/YYYY): "))
    while True:
        try:
            if len(deadline) == 10: 
                future = datetime.strptime(deadline, '%d/%m/%Y').date()
                break
            else: 
                deadline = str(input("Please enter the date in the correct format (DD/MM/YYYY): "))
        except ValueError:
             deadline = str(input("Please enter the date in the correct format (DD/MM/YYYY): "))

    today = date.today()
    days_left = (future - today).days
    # Create new instance named (new_task) for the Task class.
    new_task = Task(name, duration_minutes, difficulty, deadline, days_left)
    # Appends this task to a lists
    tasks.append(new_task)

# Iterates over the list of tasks, and checks for deadlines with days greater or equal to 0
tasks_to_do = [t for t in tasks if t.days_left >= 0]

# Sorts the list (tasks_to_do) in ascending order. Smaller number first/ Closer deadline first.
sorted_tasks = sorted(tasks_to_do, key=lambda t: t.priority(behaviour_stadistics))

# Prints all tasks with their information in the order of priority
print(" ")
print("Recommended Task Order:")
for t in sorted_tasks:
    print(t)
    print(" ")

# Update of the status. From "pending" to "Completed", "Skipped" or "Postponed".
print("End of day update:")
for t in sorted_tasks:
    print(t.name)
    update = str(input("What is the actual status of the task (Completed/Skipped/Postponed)?")).lower()
    while True:
        if update in ["completed", "skipped", "postponed"]:
            break
        else:
           update = str(input("What is the actual status of the task (Completed/Skipped/Postponed)?")).lower()     
    t.update_status(update)
    print(f"Status: {update}")
    print(" ")

# Checks for the difficulty of task, and updates the behaviour statistics dictionary for long-term memory.
for t in sorted_tasks:
    if t.difficulty >= 4:
        if t.status == "skipped":
            behaviour_stadistics["skipped_hard"] += 1
        elif t.status == "postponed":
            behaviour_stadistics["postponed_hard"] += 1
        elif t.status == "completed":
            behaviour_stadistics["completed_hard"] += 1

# Simple print statement representing the final number of "Completed", "Skipped" and "Postponed" tasks.
print("End-of-day behaviour statistics:", behaviour_stadistics)

# Updates the (behaviour_stats.json) to keep track of the behaviour for the upcoming days.
with open("behaviour_stats.json", "w") as f:
    json.dump(behaviour_stadistics, f)