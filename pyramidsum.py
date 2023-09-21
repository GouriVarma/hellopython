#Find the pyramid sum of an array 

"""
array = [3, 1, 4, 1, 5]
We'll calculate the pyramid sum for this array:

For the first element (3) at index 0, its distance from the top is 1. So, we add 3 * 1 to the sum.

For the second element (1) at index 1, its distance from the top is 2. So, we add 1 * 2 to the sum.

For the third element (4) at index 2, its distance from the top is 3. So, we add 4 * 3 to the sum.

For the fourth element (1) at index 3, its distance from the top is 4. So, we add 1 * 4 to the sum.

For the fifth element (5) at index 4, its distance from the top is 5. So, we add 5 * 5 to the sum.

Now, let's calculate the sum:

Sum = (3 * 1) + (1 * 2) + (4 * 3) + (1 * 4) + (5 * 5) = 3 + 2 + 12 + 4 + 25 = 46
So, the pyramid sum of the array [3, 1, 4, 1, 5] is 46.



ie The pyramid sum of an array is typically defined as the sum of all elements in the array, where each element is multiplied by its distance from the top of the pyramid (considering the top element as having a distance of 1).
"""
def pyramidsum(arr):
  sum = 0
  n = len(arr)
  for i in range(n):
    sum += arr[i]*(i+1)
  return sum


array = []
array = list(map(int,input("enter elements of the array: ").split()))


print(F"The pyramid sum of the array is: {pyramidsum(array)}")