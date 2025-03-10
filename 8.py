# 8.a
numbers = input("Enter numbers separated by spaces: ").split()  # Take input as a space-separated string
numbers = [int(num) for num in numbers]  # Convert each element to an integer

range_start = int(input("Min value: "))  # Get the minimum value of the range
range_end = int(input("Max value: "))  # Get the maximum value of the range

found = False  # Variable to track if a number is in range

for num in numbers:  # Loop through the list of numbers
    if range_start <= num <= range_end:  # Check if the number is in range
        found = True
        break  # Exit loop once a valid number is found

print(found)  # Print True if found, otherwise False



# 8.b
numbers = input("Enter numbers separated by spaces: ").split()  # Take input as a space-separated string
numbers = [int(num) for num in numbers]  # Convert input to a list of integers

range_start = int(input("Min value: "))  # Get minimum value
range_end = int(input("Max value: "))  # Get maximum value

index = None  # Variable to store the index of the first matching number

for i in range(len(numbers)):  # Loop through the list using indices
    if range_start <= numbers[i] <= range_end:  # Check if number is in range
        index = i  # Store the index
        break  # Exit loop after finding the first match

print(index)  # Print the index (or None if not found)


# 8.c
numbers = input("Enter numbers separated by spaces: ").split()  # Take input as space-separated numbers
numbers = [int(num) for num in numbers]  # Convert input to a list of integers

range_start = int(input("Min value: "))  # Get minimum value
range_end = int(input("Max value: "))  # Get maximum value

indices = []  # List to store indices of matching numbers

for i in range(len(numbers)):  # Loop through the list using indices
    if range_start <= numbers[i] <= range_end:  # Check if number is in range
        indices.append(i)  # Add index to the list

print(indices)  # Print list of indices (empty if none found)


# 8.d
num_lists = int(input("Enter number of lists: "))  # Number of lists to input

lists = []  # Store all lists

# Take input for each list
for i in range(num_lists):
    numbers = input(f"Enter numbers for list {i+1} separated by spaces: ").split()
    numbers = [int(num) for num in numbers]  # Convert input to integers
    lists.append(numbers)  # Add the list to our main list

range_start = int(input("Min value: "))  # Get range start
range_end = int(input("Max value: "))  # Get range end

filtered_lists = []  # Store valid lists

# Check each list
for lst in lists:
    for num in lst:  # Loop through numbers in the list
        if range_start <= num <= range_end:  # If any number is in range
            filtered_lists.append(lst)  # Keep this list
            break  # Stop checking this list

print(filtered_lists)  # Print the filtered lists



