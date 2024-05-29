def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Mark a Task as Completed")
    print("5. Exit")


def view_tasks(tasks):
    """
    Display the current to-do list tasks.

    Parameters:
    tasks (list of dict): The list of tasks.
    """
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['title']} [{status}]")


def add_task(tasks):
    """
    Add a new task to the to-do list.

    Parameters:
    tasks (list of dict): The list of tasks.
    """
    title = input("Enter the task title: ")
    tasks.append({'title': title, 'completed': False})
    print(f"Task '{title}' has been added to your to-do list.")


def remove_task(tasks):
    """
    Remove a task from the to-do list.

    Parameters:
    tasks (list of dict): The list of tasks.
    """
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['title']}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def mark_task_completed(tasks):
    """
    Mark a task as completed.

    Parameters:
    tasks (list of dict): The list of tasks.
    """
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['completed'] = True
            print(f"Task '{tasks[task_number - 1]['title']}' has been marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    """
    Main function to run the to-do list manager.
    """
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_task_completed(tasks)
        elif choice == '5':
            print("Exiting the to-do list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
