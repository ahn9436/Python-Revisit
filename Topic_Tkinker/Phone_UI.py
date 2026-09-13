import tkinter as tk

box_height = 2
box_width = 10
character__size = 15

root = tk.Tk()
root.title("Calling")
root.geometry("375x400")

number = ""
lenght = 0

def press(key):
    global number
    global lenght
    if lenght <= 15:
        number = number + key
        e1.delete(0, tk.END)
        e1.insert(tk.END, number)
        lenght += 1
    else:
        e1.delete(0, tk.END)
        e1.insert(tk.END, "Maximum Number Reach")
    

e1 = tk.Entry(root, text="Hello world dude",font=("Arial",18), justify="right")
e1.pack(fill="x", pady=10)

middle = tk.Frame(root)
middle.pack(expand=True)

def talk():
    global number
    e1.delete(0, tk.END)
    e1.config(justify="center")
    e1.insert(tk.END, f"Dialling {number}")

def delete():
    global number
    global lenght
    if lenght > 0:
        number = number[:-1]
        e1.delete(0, tk.END)
        e1.insert(tk.END, number)
        lenght -= 1

def button_creator(key, ro, co):
    bu = tk.Button(middle, text=key, width=box_width, height=box_height, font=("Arial",character__size), command=lambda: press(key))
    bu.grid(row=ro, column=co)

button_creator("1", 0, 0)
button_creator("2", 0, 1)
button_creator("3", 0, 2)
button_creator("4", 1, 0)
button_creator("5", 1, 1)
button_creator("6", 1, 2)
button_creator("7", 2, 0)
button_creator("8", 2, 1)
button_creator("9", 2, 2)
button_creator("*", 3, 0)
button_creator("0", 3, 1)
button_creator("#", 3, 2)

talk_btn = tk.Button(middle, text="Talk", width=box_width*2, height=box_height, font=("Arial",character__size), command=lambda:talk())
talk_btn.grid(row=4, column=0, columnspan=2)

bs3= tk.Button(middle, text="<", width=box_width, height=box_height, font=("Arial",character__size), command=lambda: delete())
bs3.grid(row=4, column=2)

root.mainloop()
