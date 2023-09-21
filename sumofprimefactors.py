#Sum of Prime Factors of a Given Number:


def isprime(n):
  if n<=1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

def sumofprimefactors(n):
  sum = 0
  for i in range(2,n+1):
    if n%i==0 and isprime(i):
      sum += i 
  return sum

number = int(input("enter number: "))
result = sumofprimefactors(number)
print(f"sum of prime factors of {number} is {result}")
