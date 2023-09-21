#.Given A=X+Y and B=X-Y , X and Y values are entered by the user then return Z=X*Y


def calculate_z(a,b):
  x = (a+b)/2
  y = (a-b)/2
  z = x*y 
  return z

a = float(input("Enter the value of A: "))
b = float(input("Enter the value of B: "))
result = calculate_z(a, b)
print(f"Z = {result}")