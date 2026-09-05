text = input("Enter some text: ").strip()

list__al = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
list__al2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
sum = 0

for i in range(0,len(list__al)):
    if text.count(list__al[i]) == 0: continue
    list__al[i] = text.count(list__al[i])
    sum = sum + list__al[i]

special = len(text) - sum
percent = round(100 / len(text), 3)


print("-- Character Frequency Table -")
print("char percentages (character count / string length)")
for j in range(0,len(list__al)):
    if str(list__al[j]).isdigit():
        print(f"{list__al2[j]}          {list__al[j] * percent:.2f}%")
    else: continue
if special != 0:
    print(f"Special    {special * percent:.2f}%")