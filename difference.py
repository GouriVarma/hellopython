#Absolute Difference Between the Largest and Smallest Prime Number in an Array:

def isprime(n):
  if n<=1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

def difference(arr):
  primes =[]
  for i in arr:
    if isprime(i):
      primes.append(i)
    if not primes:
      return 0
  
  smallest = min(primes)
  largest = max(primes)
  return abs(largest-smallest)
  
array = []
n = int(input("enter number of elements in the array: "))

for i in range(n):
  num = int(input(f"enter element {i+1}: "))
  array.append(num)

result = difference(array)
print(f"Absolute Difference Between the Largest and Smallest Prime Number in the Array is {result}")
