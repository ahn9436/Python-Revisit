import turtle
import tkinter as tk

def draw_tree():
    x = int(entry_x.get()) 
    
    tree.clear()
    tree.penup()
    tree.goto(0, -50) 
    tree.setheading(90)
    tree.pendown()
    tree.forward(100)
    
    def recursive_tree(len_val, n):
        if n == 0:
            return
        else:
            for i in range(2):
                if i == 0:
                    tree.left(40)
                    tree.forward(len_val)
                    recursive_tree((len_val * 2) / 3, n - 1)
                    tree.backward(len_val)
                    tree.right(40)
                else:
                    tree.right(40)
                    tree.forward(len_val)
                    recursive_tree((len_val * 2) / 3, n - 1)
                    tree.backward(len_val)
                    tree.left(40)               
    recursive_tree(50, x)

root = tk.Tk()
root.title("Recursive Tree")
root.geometry("600x700")

control_frame = tk.Frame(root)
control_frame.pack(side=tk.TOP, pady=10)

label_x = tk.Label(control_frame, text="Enter the depth : ", font=("Arial", 12))
label_x.pack(side=tk.LEFT, padx=5)

entry_x = tk.Entry(control_frame, font=("Arial", 12), width=5)
entry_x.pack(side=tk.LEFT, padx=5)

btn_draw = tk.Button(control_frame, text="Draw Tree", font=("Arial", 12), command=draw_tree)
btn_draw.pack(side=tk.LEFT, padx=5)

canvas_frame = tk.Frame(root)
canvas_frame.pack(side="top", fill="both", expand=True)

canvas = turtle.ScrolledCanvas(canvas_frame)
canvas.pack(fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas._canvas)

tree = turtle.RawTurtle(screen)
tree.speed(0)

root.mainloop()