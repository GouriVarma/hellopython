#if the array is  [1,2, 3], find[1+2,2+3]=[3,5]. Further, [3+5]=[8].Pyramid sum of array is  8.
def pyramidsum(arr):
  
  while len(arr)>1:
    new_arr = []
    for i in range(len(arr)-1):
      new_arr.append(arr[i]+arr[i+1])
    arr = new_arr 
  if arr:
   return arr[0]
  else:
   return 0



array = list(map(int,input("enter array elements: ").split()))
print(f"Pyramid sum of the array is {pyramidsum(array)}")