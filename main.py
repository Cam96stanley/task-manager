from ui import user_display
from task_operations import add_task, view_tasks, delete_task
  
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