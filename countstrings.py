# Return the count of strings containing only consonants from an array of strings

def contains_only_consonants(s):
    vowels = 'AEIOUaeiou'
    for char in s:
        if char.isalpha() and char not in vowels:
            continue
        else:
            return False
    return True

array = input("Enter an array of strings separated by spaces: ").split()
count_consonant_strings = 0
for s in array:
    if contains_only_consonants(s):
        count_consonant_strings += 1
print(f"Number of strings containing only consonants: {count_consonant_strings}")
