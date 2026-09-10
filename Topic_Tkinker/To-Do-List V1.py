import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To do List")

task = 0

def Add():
    value = e1.get()
    global task
    if value == "":
        messagebox.showwarning("Warning", "Please enter the to do list")
    else:
        todo.insert("end", value)
        task += 1
        remain.config(text= f"Remaining Tasks: {task}")

def Delete():
    global task
    value = todo.curselection()
    if value:
        text = todo.get(value[0])
        if text[0:4] != "Done":
            task -= 1 
            remain.config(text= f"Remaining Tasks: {task}")
        todo.delete(value[0])
    else:
        messagebox.showwarning("Warning", "Please select one task")

def Done():
    global task
    value = todo.curselection()
    if value:
        index = value[0]
        text = todo.get(index)
        if text[0:4] == "Done":
            messagebox.showinfo("Info", "This task is already done!")
            return
        todo.delete(index)   
        todo.insert(index, f"Done || {text}") 
        task -= 1 
        remain.config(text= f"Remaining Tasks: {task}")
    else:
        messagebox.showwarning("Warning", "Please select one task")

top_zone = tk.Frame(root)
top_zone.pack(pady=10)

l1 = tk.Label(top_zone, text="Welcome to To-Do-List App")
l1.pack()

e1 = tk.Entry(top_zone)
e1.pack()

b1 = tk.Button(top_zone, text="Add - Task", command=lambda:Add())
b1.pack()

# Bottom Zone
bottom_zone = tk.Frame(root)
bottom_zone.pack(pady=10)

todo = tk.Listbox(bottom_zone)
todo.pack()

bottom_bottom = tk.Frame(bottom_zone)
bottom_bottom.pack(pady=10)

done = tk.Button(bottom_bottom, text="Mark as Done", command=lambda:Done())
done.grid(row=0, column=0)

delete = tk.Button(bottom_bottom, text="Delete", command= lambda:Delete())
delete.grid(row=0, column=1)

remain = tk.Label(bottom_zone, text="Remaining Tasks: 0")
remain.pack(pady=10)

root.mainloop()