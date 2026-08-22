import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get().strip()

    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter a task.")

def delete_task():
    selected = listbox.curselection()

    if selected:
        listbox.delete(selected[0])
    else:
        messagebox.showwarning("Warning", "Select a task.")

root = tk.Tk()
root.title("CODTECH To-Do List")
root.geometry("400x450")

title = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

entry = tk.Entry(root, font=("Arial", 14), width=28)
entry.pack(pady=10)

add_button = tk.Button(
    root,
    text="Add Task",
    command=add_task,
    width=15
)
add_button.pack(pady=5)

listbox = tk.Listbox(
    root,
    font=("Arial", 13),
    width=35,
    height=12
)
listbox.pack(pady=15)

delete_button = tk.Button(
    root,
    text="Delete Task",
    command=delete_task,
    width=15
)
delete_button.pack(pady=5)

root.mainloop()
