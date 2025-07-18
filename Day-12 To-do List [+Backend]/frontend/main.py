# import tkinter as tk
# import requests
# from tkinter import messagebox


# BACKEND_URL = "http://127.0.0.1:5000/tasks"

# root=tk.Tk()

# root.title("To-Do List")
# root.geometry("400x500")
# root.configure(bg="#E3F2FD")

# container = tk.Frame(root, bg="#BBDEFB", bd=2, relief="groove", padx=20, pady=20)
# container.pack(padx=30, pady=30)

# task_entry=tk.Entry(container, font=("Arial",14))
# task_entry.pack(pady=10)
# task_entry.bind("<Return>", lambda event: add_task())

# btn_style = {"bg": "#1976D2", "fg": "white", "font": ("Arial", 12), "activebackground": "#1565C0"}


# task_frame = tk.Frame(root)
# task_frame.pack(pady=10)

# task_vars=[]

# def add_task_to_ui(task_text, done=False):
#     var = tk.BooleanVar(value=done)
#     checkbox = tk.Checkbutton(task_frame, text=task_text, variable=var, font=("Arial", 12))
#     checkbox.pack(anchor="w", pady=2)
#     task_vars.append((task_text, var, checkbox))


# def add_task():
#     task=task_entry.get()
#     if task:
#         # task_listbox.insert(tk.END, task)
#         # task_entry.delete(0, tk.END)
#         var=tk.IntVar()
#         cb=tk.Checkbutton(task_frame, text=task, variable=var, font=("Arial", 12), anchor='w')
#         cb.pack(fil='x', padx=10, pady=2, anchor='w')
#         task_vars.append((task,var,cb))
#         task_entry.delete(0, tk.END)

# def delete_task():
#     # selected_task=task_listbox.curselection()
#     # if selected_task:
#     #     task_listbox.delete(selected_task)

#     for task, var, cb in task_vars[:]:
#         if var.get()==1:
#             cb.destroy()
#             task_vars.remove((task, var, cb))

# def save_tasks():
#     task_list = []
#     for task, var in task_vars:
#         task_list.append({"task": task, "done": var.get()})
    
#     try:
#         response = requests.post("http://127.0.0.1:5000/tasks", json={"tasks": task_list})
#         if response.status_code == 200:
#             messagebox.showinfo("Success", "Tasks saved to server!")
#         else:
#             messagebox.showerror("Error", f"Failed to save tasks: {response.text}")
#     except Exception as e:
#         messagebox.showerror("Error", f"Could not connect to backend: {e}")

# for _, _, cb in task_vars:
#     cb.destroy()
# task_vars.clear()


# def load_tasks():
#     try:
#         response = requests.get("http://127.0.0.1:5000/tasks")
#         if response.status_code == 200:
#             task_list = response.json()
#             for widget in task_frame.winfo_children():
#                 widget.destroy()
#             task_vars.clear()
#             for task in task_list:
#                 add_task_to_ui(task["task"], task["done"])
#         else:
#             messagebox.showerror("Error", f"Failed to load tasks: {response.text}")
#     except Exception as e:
#         messagebox.showerror("Error", f"Could not connect to backend: {e}")


# def mark_all_done():
#     for task, var, cb in task_vars:
#         var.set(1)

# delete_btn=tk.Button(container, text="Delete Task", command=delete_task, font=("Arial", 12))
# delete_btn.pack(pady=5)
# root.bind("<Delete>", lambda event: delete_task())


# save_btn=tk.Button(container,text="Save Tasks", command=save_tasks, font=("Arial", 12))
# save_btn.pack(pady=5)

# load_btn=tk.Button(container, text= "Load Previous Tasks", command=load_tasks, font=("Arial", 12))
# load_btn.pack(pady=5)

# add_btn=tk.Button(container, text="Add Task", command=add_task,  **btn_style)
# add_btn.pack(pady=5)

# mark_all_btn = tk.Button(container, text="Mark All Done", bg="#d0f0c0", fg="#004d00",command=mark_all_done, font=("Arial", 12))
# mark_all_btn.pack(pady=5)




# root.mainloop()


import tkinter as tk
import requests
from tkinter import messagebox

BACKEND_URL = "http://127.0.0.1:5000/tasks"

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#E3F2FD")

container = tk.Frame(root, bg="#BBDEFB", bd=2, relief="groove", padx=20, pady=20)
container.pack(padx=30, pady=30)

task_entry = tk.Entry(container, font=("Arial", 14))
task_entry.pack(pady=10)
task_entry.bind("<Return>", lambda event: add_task())

btn_style = {"bg": "#1976D2", "fg": "white", "font": ("Arial", 12), "activebackground": "#1565C0"}

task_frame = tk.Frame(root)
task_frame.pack(pady=10)

task_vars = []

def add_task_to_ui(task_text, done=False):
    var = tk.BooleanVar(value=done)
    checkbox = tk.Checkbutton(task_frame, text=task_text, variable=var, font=("Arial", 12))
    checkbox.pack(anchor="w", pady=2)
    task_vars.append((task_text, var, checkbox))

def add_task():
    task = task_entry.get()
    if task:
        try:
            response = requests.post(BACKEND_URL, json={"task": task})
            if response.status_code == 201:
                add_task_to_ui(task)
                task_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", f"Failed to add task: {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not connect to backend: {e}")

def delete_task():
    for i in reversed(range(len(task_vars))):
        task_text, var, cb = task_vars[i]
        if var.get():
            try:
                response = requests.delete(f"{BACKEND_URL}/{i}")
                if response.status_code == 200:
                    cb.destroy()
                    task_vars.pop(i)
                else:
                    messagebox.showerror("Error", f"Failed to delete task: {response.text}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not connect to backend: {e}")

def save_tasks():
    for i, (task, var, _) in enumerate(task_vars):
        try:
            requests.put(f"{BACKEND_URL}/{i}", json={"done": var.get()})
        except Exception as e:
            messagebox.showerror("Error", f"Could not connect to backend: {e}")
    messagebox.showinfo("Success", "Tasks updated on server!")

def load_tasks():
    try:
        response = requests.get(BACKEND_URL)
        if response.status_code == 200:
            task_list = response.json()
            for widget in task_frame.winfo_children():
                widget.destroy()
            task_vars.clear()
            for task in task_list:
                add_task_to_ui(task["task"], task["done"])
        else:
            messagebox.showerror("Error", f"Failed to load tasks: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not connect to backend: {e}")

def mark_all_done():
    for _, var, _ in task_vars:
        var.set(True)

delete_btn = tk.Button(container, text="Delete Task", command=delete_task, font=("Arial", 12))
delete_btn.pack(pady=5)
root.bind("<Delete>", lambda event: delete_task())

save_btn = tk.Button(container, text="Save Tasks", command=save_tasks, font=("Arial", 12))
save_btn.pack(pady=5)

load_btn = tk.Button(container, text="Load Previous Tasks", command=load_tasks, font=("Arial", 12))
load_btn.pack(pady=5)

add_btn = tk.Button(container, text="Add Task", command=add_task, **btn_style)
add_btn.pack(pady=5)

mark_all_btn = tk.Button(container, text="Mark All Done", bg="#d0f0c0", fg="#004d00", command=mark_all_done, font=("Arial", 12))
mark_all_btn.pack(pady=5)

# Load tasks initially
load_tasks()

root.mainloop()
