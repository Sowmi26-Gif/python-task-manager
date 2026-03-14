def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass

while True:

    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
       task = input("Enter a new task: ")
       tasks.append(task)
       save_tasks()
       print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks):
                print(i+1, ".", task)

    elif choice == "3":
      if len(tasks) == 0:
        print("No tasks to complete.")
      else:
        for i, task in enumerate(tasks):
            print(i+1, ".", task)

        num = int(input("Enter task number to complete: "))

        if 0 < num <= len(tasks):
            tasks.pop(num-1)
            save_tasks()
            print("Task completed!")
        else:
            print("Invalid number.")

    elif choice == "4":
     print("Goodbye!")
     break