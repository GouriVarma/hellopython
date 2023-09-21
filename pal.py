# Given a string. It contains 4 letter and 5 letter palindromes. If the palindrome is 4 letter add 5 to output and if palindrome is 5 letter add 10 to output. Get the total output. If no palindromes in string get 0 as output.
#Eg: asdfg htth jklm rrtrr qwerty
#Output is 5+10= 15


s = input("enter string: ")
words = s.split()
print(words)
sum = 0
for x in words:
  if x == x[::-1]:
    if len(x)== 4:
      sum += 5
    elif len(x)== 5:
      sum += 10
print(sum)
   
