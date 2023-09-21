# Product of Numbers from Given Sum and Difference:

"""x = (s+d)/2
   y = (s-d)/2
"""

def num_product(sum,diff):
  x = (sum+diff)/2
  y = (sum-diff)/2
  product = x*y
  return x,y,product

sum = int(input("enter sum of the numbers: "))
diff = int(input("enter difference of the numbers: "))
x,y,product = num_product(sum,diff)
print(f"The numbers are {x} and {y} and their product is {product}")

