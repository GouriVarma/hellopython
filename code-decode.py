"""
1. rev string word by word
2.replace even index char to uppercase and odd index char to lowercase
3.replace even index space with # and odd index spaces with *
4.any other char in even index we need to replace with @ and any other char in odd index is replaced with :
"""
 
string = input()
words = string.split()
rev_words = [word[::-1] for word in words]
rev_string = ' '.join(rev_words)

modified_string = ''

for i in range(len(rev_string)):
  char = rev_string[i]
  if i%2==0:
    modified_string += char.upper()
  else:
    modified_string += char.lower()
    
for i in range(len(modified_string)):
  if modified_string[i] == ' ' and i % 2 == 0:
        modified_string = modified_string[:i] + '#' + modified_string[i + 1:]
  elif modified_string[i] == ' ':
        modified_string = modified_string[:i] + '*' + modified_string[i + 1:]

final_result = ''
for i in range(len(modified_string)):
    char = modified_string[i]
    if i % 2 == 0 and  not char.isalpha():
        final_result += '@'
    elif not char.isalpha():
        final_result += ':'
    else:
        final_result += char
print(final_result)
