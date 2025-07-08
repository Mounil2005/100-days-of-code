import tkinter as tk

root=tk.Tk()

root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#E3F2FD")

container = tk.Frame(root, bg="#BBDEFB", bd=2, relief="groove", padx=20, pady=20)
container.pack(padx=30, pady=30)

task_entry=tk.Entry(container, font=("Arial",14))
task_entry.pack(pady=10)
task_entry.bind("<Return>", lambda event: add_task())

btn_style = {"bg": "#1976D2", "fg": "white", "font": ("Arial", 12), "activebackground": "#1565C0"}

# task_listbox = tk.Listbox(root, font=("Arial", 12), width=30, height=10)
# task_listbox.pack(pady=10)
task_frame = tk.Frame(root)
task_frame.pack(pady=10)

task_vars=[]

def add_task():
    task=task_entry.get()
    if task:
        # task_listbox.insert(tk.END, task)
        # task_entry.delete(0, tk.END)
        var=tk.IntVar()
        cb=tk.Checkbutton(task_frame, text=task, variable=var, font=("Arial", 12), anchor='w')
        cb.pack(fil='x', padx=10, pady=2, anchor='w')
        task_vars.append((task,var,cb))
        task_entry.delete(0, tk.END)

def delete_task():
    # selected_task=task_listbox.curselection()
    # if selected_task:
    #     task_listbox.delete(selected_task)

    for task, var, cb in task_vars[:]:
        if var.get()==1:
            cb.destroy()
            task_vars.remove((task, var, cb))

def save_tasks():
    with open("tasks.txt","w") as file:
        # tasks=task_listbox.get(0,tk.END)
        # for task in tasks:
        #     file.write(task + "\n")
        for task,var,_ in task_vars:
            if var.get()==0:
                file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt","r") as file:
            tasks=file.readlines()
            for task in tasks:
                # task_listbox.insert(tk.END, task.strip())
                var = tk.IntVar()
                cb = tk.Checkbutton(task_frame, text=task.strip(), variable=var, font=("Arial", 12), anchor='w')
                cb.pack(fill='x', padx=10, pady=2, anchor='w')
                task_vars.append((task.strip(), var, cb))
    except FileNotFoundError:
        pass 

def mark_all_done():
    for task, var, cb in task_vars:
        var.set(1)

delete_btn=tk.Button(container, text="Delete Task", command=delete_task, font=("Arial", 12))
delete_btn.pack(pady=5)
root.bind("<Delete>", lambda event: delete_task())


save_btn=tk.Button(container,text="Save Tasks", command=save_tasks, font=("Arial", 12))
save_btn.pack(pady=5)

load_btn=tk.Button(container, text= "Load Previous Tasks", command=load_tasks, font=("Arial", 12))
load_btn.pack(pady=5)

add_btn=tk.Button(container, text="Add Task", command=add_task,  **btn_style)
add_btn.pack(pady=5)

mark_all_btn = tk.Button(container, text="Mark All Done", bg="#d0f0c0", fg="#004d00",command=mark_all_done, font=("Arial", 12))
mark_all_btn.pack(pady=5)




root.mainloop()