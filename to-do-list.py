import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "Done" if task.completed else "Pending"
                print(f"{i}. {task.description} - {status}")

    def mark_task_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print(f"Task '{self.tasks[task_index - 1].description}' marked as completed.")
        else:
            print("Invalid task index.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Removed task: '{removed_task.description}'")
        else:
            print("Invalid task index.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.completed}\n")
        print(f"Tasks saved to {filename}.")

    def load_from_file(self, filename):
        if os.path.exists(filename):
            self.tasks.clear()  # Clear existing tasks
            with open(filename, 'r') as file:
                for line in file:
                    description, completed = line.strip().split(',')
                    task = Task(description)
                    task.completed = completed == 'True'
                    self.tasks.append(task)
            print(f"Tasks loaded from {filename}.")
        else:
            print("No existing tasks file found.")

def main():
    todo_list = ToDoList()

    # Load tasks from a file if it exists
    todo_list.load_from_file("tasks.txt")

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to remove: "))
            todo_list.remove_task(task_index)
        elif choice == "5":
            todo_list.save_to_file("tasks.txt")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

