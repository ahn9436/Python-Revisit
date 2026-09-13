import tkinter as tk

radius = 15
location = []
count = 0

root = tk.Tk()
root.title("Appear and Remove")
root.geometry("450x300")

def create(event):
    global radius
    global location
    global count
    x1 = event.x
    y1 = event.y

    tag_name = f"ID:{count}{count+5}{count-2}"
    canva.create_oval(x1+radius, y1 + radius, x1-radius,y1 - radius, outline="black", tags=tag_name)
    location.append(x1+radius)
    location.append(y1 + radius)
    location.append(x1-radius)
    location.append(y1 - radius)
    location.append(tag_name)
    count += 1
    print(location)

def delete(event):
    global radius
    global location
    global count
    x1 = event.x
    y1 = event.y
    if location:
        for i in range(0,len(location),5):
            if location[i+2] < x1 < location[i] and location[i+3] < y1 < location[i+1]:
                canva.delete(location[i+4])
                del location[i:i+5]
                print(location)
                return

canva = tk.Canvas(root, width=450, height=300)
canva.bind("<Button-1>", create)
canva.bind("<Button-3>", delete)
canva.pack()

root.mainloop()
