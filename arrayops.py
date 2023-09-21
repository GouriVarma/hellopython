#Given an array(integers). Remove an element from the array if it is an even number or a duplicate number. Return the count of elements in the array after removing the same.

arr = list(map(int,input("enter array elements: ").split()))
unique =[]
for x in arr:
  if x%2!=0 and x not in unique:
    unique.append(x)
print(unique)
count = len(unique)
print(f"Count of elements in the array after removing is {count}.")
