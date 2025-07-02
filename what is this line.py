# This program callulate the line type which user input them or those number is invalid
x1 = float(input(""))
y1 = float(input(""))
x2 = float(input(""))
y2 = float(input(""))
if x1==x2 and y1==y2:
   print("Single Point")
elif x1==x2 and y1!=y2:
   print("Vertical Line")
elif x1!=x2 and y1==y2:
   print("Horizontal Line")
else:
  slope = (y2 - y1) / (x2 - x1)
  if slope > 0:
    print("Positive Slope")
  if slope < 0:
    print("Negative Slope")
