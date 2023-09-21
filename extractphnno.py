#Given a string S. A phone number is hiding in it. S can contain alphabet numerical and characters.Write the fuction which extracts the phone number only as a string.The last 10 numeric digits are the phone number.

s = input("enter string with hidden phone number : ")

def extractphnno(str):
  phnno =''
  for char in str[::-1]:      #reversed()
    if char.isdigit():            #if '0'<= char <= '9'
      phnno = char + phnno
      if len(phnno)==10:
        break

  return phnno

print(f"Phnno is {extractphnno(s)}")