# calculate is the number are odd or even using dictionary
n = int(input(""))
nums = dict()
for i in range(0,n):
  number = int(input(""))
  if number%2 == 0:
    nums[number] = "even"
  else:
    nums[number] = "odd"

print(nums)
