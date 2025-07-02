# This program is the basic number counter 
# it count how many number user input into the program
x = int(input())
y = int(input())
d = int(input())
count = 0
for i in range(x,y+1):
  if i%d==0:
    print(i, end=' ')
    count = count+1

print(f'count={count}')

