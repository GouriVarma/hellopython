#Convert names into the format such that first letter is capital and the rest all are in lowercase Eg:Mark,Alice

name = input("enter name: ")
# print(name.capitalize())
# print(name.title())

if name:
  formatted_name = name[0].upper()+name[1:].lower()
  print(formatted_name)

if name: 
  words = name.split()
  capitalized_words = []
  for word in words:
    capitalized_word = word[0].upper()+word[1:].lower()
    capitalized_words.append(capitalized_word)
  formatted_name = ' '.join(capitalized_words)
  print(formatted_name)
