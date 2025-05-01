def add_task(tasks):
  task = input("Enter task description: ")
  tasks.append(task)
  print(f"Task added: '{task}'")
  
def view_tasks(tasks):
  if not tasks:
    print("No tasks found")
  else:
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, start=1):
      print(f"{i}. {task}")
      
def delete_task(tasks):
  view_tasks(tasks)
  if tasks:
    try:
      task_num = int(input("Enter the number of the task you want to delete: "))
      if 1 <= task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        print(f"Task deleted: '{removed}'")
      else:
        print("Invalid task number")
    except ValueError:
      print("Please enter a valid number.")