# Is the number divisible by 3 or 7
# Is it positive or not
# Is it end with one


x = int(input())
if x > 0:
  print("x is positive")
else:
  print("x is not positive")

if x%3==0 and x%7==0:
  print("x is divisible by 3 and 7")
else:
  print("x is not divisible by 3 and 7")
#x=25
if x%10==1:
  print("x is ending with 1")
else:
  print("x is not ending with 1")
