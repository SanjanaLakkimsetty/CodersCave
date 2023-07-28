def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the to-do list.")

def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def mark_completed(todo_list):
    view_tasks(todo_list)
    if not todo_list:
        return

    task_num = int(input("Enter the number of the task you want to mark as completed: "))
    if 1 <= task_num <= len(todo_list):
        completed_task = todo_list.pop(task_num - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task number.")

def main():
    print("Simple To-Do App")
    todo_list = []

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            print("Exiting the to-do app.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
