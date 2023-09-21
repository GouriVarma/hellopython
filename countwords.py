#Take an array of input B=[‘Daa’, ‘aaB’ , ‘AcB’] give the count of  words starting with either ‘a’ or ‘A’

b =['Daa','aab','Acb']
count =0
for x in b:
  if x[0]=='a' or x[0]=='A':
    count += 1
print(count)