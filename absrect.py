#Given an array of n elements. Consider  the consecutive pairs of the array as  length and breadth of a rectangle. If the area < perimeter, then it is type A, else if area > perimeter, then it is type B. 
#Find the absolute difference between the number of type A and type B rectangles.

# Initialize counters for type A and type B rectangles
count_type_a = 0
count_type_b = 0

# Input the number of elements in the array
n = int(input("Enter the number of elements in the array: "))

# Input the array of elements
arr = []
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

# Iterate through consecutive pairs in the array
for i in range(n - 1):
    length = arr[i]
    breadth = arr[i + 1]

    # Calculate area and perimeter for the rectangle
    area = length * breadth
    perimeter = 2 * (length + breadth)

    # Check if it's type A or type B based on the area and perimeter
    if area < perimeter:
        count_type_a += 1
    elif area > perimeter:
        count_type_b += 1

# Calculate the absolute difference
difference = abs(count_type_a - count_type_b)

# Display the result
print(f"Absolute difference between type A and type B rectangles: {difference}")
