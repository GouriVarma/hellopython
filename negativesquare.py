#Given an array. For the elements in an array <0 return the square of the negative numbers.

arr = list(map(int,input("enter array elements: ").split()))

negative_square = []

for x in arr:
  if x<0:
    result = x**2
    negative_square.append(result)

if negative_square:
  print(f"square of negative numbers is {negative_square}")
else:
  print("no negative squares")