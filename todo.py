import json
import os
from datetime import datetime
class FriendlyTodo:
    def __init__(self):
        self.filename = "my_tasks.json"
        self.tasks = self.load_my_tasks()
    def load_my_tasks(self):
        """Get my saved tasks"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            except:
                return []
        return []
    def save_my_tasks(self):
        """Save tasks for later"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)
    def add_task(self, task_name):
        """Add something new to do"""
        task = {
            "id": len(self.tasks) + 1,
            "task": task_name,
            "done": False,
            "added_on": datetime.now().strftime("%b %d, %Y")
        }
        self.tasks.append(task)
        self.save_my_tasks()
        print(f"\n Got it! Added: '{task_name}'")
    def show_my_tasks(self):
        """Show me what I need to do"""
        if not self.tasks:
            print("\n Nothing to do! Enjoy your free time!")
            return
        print("\n" + "="*50)
        print(" MY TO-DO LIST")
        print("="*50)
        pending = []
        done = []
        for task in self.tasks:
            if task["done"]:
                done.append(task)
            else:
                pending.append(task)
        if pending:
            print("\n STILL TO DO:")
            for task in pending:
                print(f"  [{task['id']}] {task['task']}")
                print(f"      Added: {task['added_on']}")
        if done:
            print("\n DONE:")
            for task in done:
                print(f"  [{task['id']}] {task['task']} ✓")
        total = len(self.tasks)
        completed = len(done)
        print("\n" + "-"*50)
        print(f" {completed}/{total} tasks done")
        if completed == total and total > 0:
            print(" Amazing! Everything is done!")
    def mark_done(self, task_number):
        """Check off a task"""
        for task in self.tasks:
            if task["id"] == task_number:
                if not task["done"]:
                    task["done"] = True
                    self.save_my_tasks()
                    print(f"\n Nice! '{task['task']}' is done!")
                else:
                    print("\n This task is already done!")
                return
        print("\n Hmm, couldn't find that task number.")
    def remove_task(self, task_number):
        """Remove a task from the list"""
        for task in self.tasks:
            if task["id"] == task_number:
                self.tasks.remove(task)
                self.save_my_tasks()
                print(f"\n Removed: '{task['task']}'")
                return
        print("\n Couldn't find that task.")
    def show_summary(self):
        """Quick summary of my tasks"""
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task["done"])
        pending = total - done
        print("\n QUICK SUMMARY")
        print(f"   Total tasks: {total}")
        print(f"   Done: {done}")
        print(f"   Still to do: {pending}")
        if total > 0:
            percent = (done / total) * 100
            print(f"   Progress: {percent:.0f}%")
            if percent == 100:
                print("   Perfect score!")
            elif percent >= 75:
                print("    Almost there!")
            elif percent >= 50:
                print("    Halfway through!")
            elif percent > 0:
                print("    Good start!")
            else:
                print("    Ready to begin!")
def main():
    my_list = FriendlyTodo()
    print("\n Welcome to Your To-Do List!")
    print("   Let's get organized together!")
    while True:
        print("\n" + "="*50)
        print("WHAT WOULD YOU LIKE TO DO?")
        print("="*50)
        print("1.  Add a new task")
        print("2.  See all my tasks")
        print("3.  Mark a task as done")
        print("4.  Remove a task")
        print("5.  See my progress")
        print("6.  Exit")
        choice = input("\nYour choice (1-6): ").strip()
        if choice == "1":
            task = input("\nWhat do you need to do? ").strip()
            if task:
                my_list.add_task(task)
            else:
                print("\n Oops! Can't add an empty task!")
        elif choice == "2":
            my_list.show_my_tasks()
        elif choice == "3":
            my_list.show_my_tasks()
            try:
                num = int(input("\nWhich task number is done? "))
                my_list.mark_done(num)
            except ValueError:
                print("\n Please enter a valid task number!")
        elif choice == "4":
            my_list.show_my_tasks()
            try:
                num = int(input("\nWhich task number to remove? "))
                confirm = input(f"Sure you want to remove task #{num}? (yes/no): ").strip().lower()
                if confirm in ['yes', 'y']:
                    my_list.remove_task(num)
                else:
                    print("\n Okay, kept it!")
            except ValueError:
                print("\n Please enter a valid task number!")
        elif choice == "5":
            my_list.show_summary()
        elif choice == "6":
            print("\n Bye! Have a productive day!")
            print("   Your tasks are saved for next time!\n")
            break
        else:
            print("\n That's not an option! Choose 1-6 please.")
if __name__ == "__main__":
    main()