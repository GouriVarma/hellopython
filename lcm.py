#Given array S, find LCM of pair of numbers in the same order and display the largest LCM value

def lcm(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1

def largest_lcm(S):
    if len(S) < 2:
        return None
    
    largest = 0
    for i in range(len(S) - 1):
        for j in range(i + 1, len(S)):
            current_lcm = lcm(S[i], S[j])
            largest = max(largest, current_lcm)

    return largest

# Example usage:
S = [12, 18, 24, 36]
result = largest_lcm(S)

if result is not None:
    print(f"The largest LCM of pairs in the array is: {result}")
else:
    print("The array does not contain enough elements to compute an LCM.")
