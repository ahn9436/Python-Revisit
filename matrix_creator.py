# Create your own matrix with this code
m = int(input(""))
n = int(input(""))
list = []
for i in range(0,m):
  list.append([])
  for j in range(0,n):
    number = int(input(""))
    list[i].append(number)
for s in range(0,len(list)):
  print(list[s])

# And this code also count the number 0 for you in each collumn
for b in range(n):
  count = 0
  for c in range(m):
    if list[c][b] == 0:
      count +=1
  print(count, end=" ")
