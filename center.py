#Get center value from list of elements
n = int(input("enter number of elemnts: "))
lst=[]
lst = list(map(int,input().split()))

def bubble_sort(arr):
  l = len(arr)
  for i in range(l):
    for j in range(0,l-i-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]

bubble_sort(lst)
if len(lst)%2==0:
  c = (lst[len(lst)//2]+lst[(len(lst)//2)-1])/2
else:
  c = lst[len(lst)//2]
print(lst)
print(c)
