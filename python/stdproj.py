def add_task(tasks, task, priority):
    tasks[task] = priority
    print(f"Task '{task}' added.")

def delete_task(tasks, task):
    if task in tasks:
        del tasks[task]
        print(f"Task '{task}' has been deleted.")
    else:
        print(f"Task '{task}' not found.")

def rearrange_order(tasks):
    
    sorted_tasks = [task for task, _ in sorted(tasks.items(), key=lambda item: item[1], reverse=True)]
    return sorted_tasks

def display_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nCurrent To-Do List:")
        for task in tasks:
            print(f"Task: {task}")

def main():
    tasks = {}

    while True:
        print("\n1. Add task")
        print("2. Delete task")
        print("3. Rearrange tasks by priority")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            priority = int(input("Enter priority (higher number means higher priority): "))
            add_task(tasks, task, priority)
        elif choice == "2":
            task = input("Enter the task to delete: ")
            delete_task(tasks, task)
        elif choice == "3":
            tasks = rearrange_order(tasks)
            print("Tasks have been rearranged by priority.")
        elif choice == "4":
            display_tasks(tasks)
        elif choice == "5":
            print("Goodbye!")
            break 
        else:
            print("Invalid option. Please try again.")


main()
