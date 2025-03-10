#6a
numbers = [10, 3, 25, 7, 8]
largest = max(numbers)
smallest = min(numbers)

print("Largest:", largest)
print("Smallest:", smallest)


#6b
str = ['abc', 'xyz', 'aba', '1221']
count = 0

for word in str:
    if len(word) >= 2 and word[0] == word[-1]:  # Check first and last character
        count += 1

print("Count:", count)


#6c
def is_toeplitz(matrix):
    for i in range(len(matrix) - 1):  # Loop through rows (except last)
        for j in range(len(matrix[0]) - 1):  # Loop through columns (except last)
            if matrix[i][j] != matrix[i + 1][j + 1]:  # Check diagonal elements
                return False  # If one diagonal is different, return False
    return True  # If all diagonals match, return True

matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
print("Is Toeplitz?", is_toeplitz(matrix))

