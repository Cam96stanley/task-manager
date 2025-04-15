def user_display():
  print("\n--- CLI Task Manager ---")
  print("1. Add task")
  print("2. View tasks")
  print("3. Delete task")
  print("4. Quit")
  
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
  
def main():
  tasks = []
  print("Welcome to the Task Manager")
  
  while True: 
    user_display()
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
      add_task(tasks)
    elif choice == "2":
      view_tasks(tasks)
    elif choice == "3":
      delete_task(tasks)
    elif choice == "4":
      print("Goodbye")
      break
    else:
      print("Invalid option. Please choose between 1 and 4")
      
if __name__ == '__main__':
  main()