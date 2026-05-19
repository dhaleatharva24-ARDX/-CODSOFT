import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime
class SimpleTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do List")
        self.root.geometry("500x500")
        # Load tasks
        self.tasks = self.load_tasks()
        # Create the layout
        self.create_widgets()
        self.show_tasks()
    def load_tasks(self):
        if os.path.exists("my_tasks.json"):
            try:
                with open("my_tasks.json", 'r') as file:
                    return json.load(file)
            except:
                return []
        return []
    def save_tasks(self):
        with open("my_tasks.json", 'w') as file:
            json.dump(self.tasks, file, indent=2)
    def create_widgets(self):

        title = tk.Label(self.root, text="📝 My To-Do List", 
                        font=("Arial", 16, "bold"))
        title.pack(pady=10)

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        self.task_input = tk.Entry(input_frame, width=40, font=("Arial", 12))
        self.task_input.pack(side=tk.LEFT, padx=5)
        add_btn = tk.Button(input_frame, text="Add", 
                           command=self.add_task,
                           bg="#4CAF50", fg="white",
                           font=("Arial", 10, "bold"))
        add_btn.pack(side=tk.LEFT)

        self.task_listbox = tk.Listbox(self.root, width=50, height=15,
                                       font=("Arial", 11))
        self.task_listbox.pack(pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        done_btn = tk.Button(btn_frame, text="✓ Done", 
                            command=self.mark_done,
                            bg="#2196F3", fg="white",
                            font=("Arial", 10))
        done_btn.pack(side=tk.LEFT, padx=5)
        delete_btn = tk.Button(btn_frame, text="Delete", 
                              command=self.delete_task,
                              bg="#f44336", fg="white",
                              font=("Arial", 10))
        delete_btn.pack(side=tk.LEFT, padx=5)
    
        self.progress_label = tk.Label(self.root, text="", 
                                      font=("Arial", 10))
        self.progress_label.pack(pady=10)
    def add_task(self):
        task_name = self.task_input.get().strip()
        if task_name:
            task = {
                "id": len(self.tasks) + 1,
                "task": task_name,
                "done": False,
                "date": datetime.now().strftime("%b %d")
            }
            self.tasks.append(task)
            self.save_tasks()
            self.task_input.delete(0, tk.END)
            self.show_tasks()
            messagebox.showinfo("Success", "Task added! ✨")
        else:
            messagebox.showwarning("Oops", "Please type something!")
    def mark_done(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task_name = self.task_listbox.get(index)

            for task in self.tasks:
                if task["task"] in task_name and not task["done"]:
                    task["done"] = True
                    self.save_tasks()
                    self.show_tasks()
                    messagebox.showinfo("Nice!", "Task completed! ✅")
                    return
            messagebox.showinfo("Info", "Task is already done!")
        else:
            messagebox.showwarning("Oops", "Please select a task first!")
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if selection:
            index = selection[0]
            task_name = self.task_listbox.get(index)
            if messagebox.askyesno("Delete?", "Remove this task?"):
                for task in self.tasks:
                    if task["task"] in task_name:
                        self.tasks.remove(task)
                        self.save_tasks()
                        self.show_tasks()
                        break
        else:
            messagebox.showwarning("Oops", "Please select a task first!")
    def show_tasks(self):
        self.task_listbox.delete(0, tk.END)

        for task in self.tasks:
            if not task["done"]:
                self.task_listbox.insert(tk.END, f"○ {task['task']}")

        for task in self.tasks:
            if task["done"]:
                self.task_listbox.insert(tk.END, f"✓ {task['task']} (done)")
    
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["done"])
        if total > 0:
            percent = (done / total) * 100
            self.progress_label.config(
                text=f"Progress: {done}/{total} tasks done ({percent:.0f}%)"
            )
        else:
            self.progress_label.config(text="No tasks yet. Add one! 📝")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTodoApp(root)
    root.mainloop()