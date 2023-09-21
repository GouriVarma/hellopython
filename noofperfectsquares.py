#Count the no of perfect squares in a given array
import math
def perfectsquares(arr):
  count = 0
  for x in arr:
    if math.sqrt(x).is_integer():
      count +=1
  return count



array = []
n = int(input("enetr number of elements in the array: "))
for i in range(n):
  num = int(input(f"enter element {i+1}: "))
  array.append(num)

print(F"The number of perfect squares in the array is: {perfectsquares(array)}")