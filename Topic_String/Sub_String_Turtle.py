import turtle as t

text = input("Enter some text: ").strip()
height_multiplier = 20

list__al = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list__al2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
sum = 0

for i in range(0,len(list__al)):
    if text.count(list__al[i]) == 0: continue
    list__al[i] = text.count(list__al[i])
    sum = sum + list__al[i]

max = 0
width = 0
for j in range(0,len(list__al)):
    if str(list__al[j]).isdigit():
        width += 1
        if list__al[j] > max:
            max = list__al[j]
    else: continue

t.teleport(-30 * width,-max * 6)
t.left(90)
t.forward(max * 20)
t.stamp()
t.right(180)
t.forward(max * 20)
t.left(90)

for j in range(0,len(list__al)):
    if str(list__al[j]).isdigit():
        t.forward(55)
        t.penup()
        t.right(90)
        t.forward(20)
        t.write(str(list__al2[j]), align="right", font=("Arial", 12, "normal"))
        t.backward(20)
        t.left(90)
        t.pendown()
        t.forward(5)
        for b in range(0,2):
            t.left(90)
            t.forward(list__al[j] * height_multiplier)
            t.left(90)
            t.forward(15)
    else: continue

t.forward(60)
t.stamp()
t.hideturtle()
t.done()