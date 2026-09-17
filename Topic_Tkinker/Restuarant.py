import tkinter as tk

root = tk.Tk()
root.title("Order Food")
root.geometry("1920x1080")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=2)
root.grid_columnconfigure(1, weight=1)

def create_food(label1_text,d1,d2,r, c):
    f_rame = tk.Frame(foods, border=2, background="black")
    f_rame.grid_rowconfigure(r, weight=1)
    f_rame.grid_columnconfigure(c, weight=1)
    f_rame.grid(row=r, column=c, sticky="w", padx=15, pady=8)
    ca = tk.Canvas(f_rame, width=240,height=160, background="white")
    ca.create_oval(50,10,180,140, fill="white")
    ca.pack(fill="x")
    l = tk.Label(f_rame, text=label1_text, height=1, font=("Times New Roman", 13),bg="black", fg="white")
    l.pack(anchor="w", pady=4)
    l = tk.Label(f_rame, text=d1, height=1, font=("Times New Roman", 11),bg="black", fg="white")
    l.pack(anchor="w")
    l = tk.Label(f_rame, text=d2, height=1, font=("Times New Roman", 11),bg="black", fg="white")
    l.pack(anchor="w")
    n = tk.Button(f_rame, text="Add to order", font=("Times New Roman", 12), height=1, bd=2, bg="grey", fg="white")
    n.pack(anchor="w", pady=15)

left = tk.Frame(root, background="black")
left.grid(row=0, column=1, sticky="nsew")

l3 = tk.Label(left, text="Roblox King", font=("Times New Roman", 15), bg="black", fg="white")
l3.pack(anchor="w", padx=8, pady=5)
l1 = tk.Label(left, text="Our Menus", font=("Times New Roman", 27), bg="black", fg="white")
l1.pack(anchor="w", padx=7)

right = tk.Frame(root, background="black")
right.grid(row=0, column=0, sticky="nsew")

l2 = tk.Label(right, text="Your Order", font=("Times New Roman", 22), background="black", fg="white")
l2.pack(anchor="center", pady=10, padx=8)
check = tk.Button(right, text="Checkout",font=("Times New Roman", 19))
check.pack(anchor="s",side="bottom")

foods = tk.Frame(left, background="black")
foods.pack(pady=20)

create_food("Heirloom Beet & Goat Cheese Crudo", "Roasted golden beets", "whipped artisanal goat, cheese, micro-basil" ,0,0)
create_food("Pan-Seared U10 Sea Scallops","Wild mushroom fricassee, sunchoke purée, ","black truffle emulsion micro-sorrel." ,0,1)
create_food("Crisp Heritage Pork Belly", "Compressed watermelon, pickled ","aged balsamic glaze, smoked sea salt.",0,2)
create_food("Pan-Seared Duck Breast","Juniper-infused parsnip purée wilted" , "blackberry gastrique, toasted hazelnuts.",0,3)

create_food("Crisp Heritage Pork Belly", "Compressed watermelon, pickled ","aged balsamic glaze, smoked sea salt.",1,0)
create_food("Heirloom Beet & Goat Cheese Crudo", "Roasted golden beets", "whipped artisanal goat, cheese, micro-basil" ,1,1)
create_food("Pan-Seared Duck Breast","Juniper-infused parsnip purée wilted" , "blackberry gastrique, toasted hazelnuts.",1,2)
create_food("Pan-Seared U10 Sea Scallops","Wild mushroom fricassee, sunchoke purée, ","black truffle emulsion micro-sorrel." ,1,3)

root.mainloop()
