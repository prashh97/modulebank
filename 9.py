# 9.a
def contains_vowel():
    text = input("Enter a string: ")  # Take user input
    text = text.lower()  # Convert text to lowercase

    vowels = "aeiou"  # List of vowels
    for vowel in vowels:  # Check for each vowel
        if vowel in text:  # If any vowel is found, return True
            print(True)
            return  
          
    print(False)  # If no vowel is found, print False

contains_vowel()



# 9.b
text = input("Enter a string: ")  # Take user input
text = text.lower()  # Convert to lowercase

vowels = "aeiou"  # List of vowels
unique_vowels = set()  # Empty set to store unique vowels

for char in text:  # Loop through each character in text
    if char in vowels:  # If character is a vowel
        unique_vowels.add(char)  # Add it to the set (avoids duplicates)

print(len(unique_vowels))  # Print the number of unique vowels



#9.c
text = input("Enter a string: ")  # Take user input
text = text.lower()  # Convert to lowercase

vowels = "aeiou"  # List of vowels
vowel_counts = {}  # Dictionary to store vowel counts

# Initialize vowel counts to 0
for vowel in vowels:
    vowel_counts[vowel] = 0

# Count occurrences of each vowel
for char in text:
    if char in vowels:
        vowel_counts[char] += 1

# Check if all vowels are present
all_vowels_present = True
for vowel in vowels:
    if vowel_counts[vowel] == 0:  # If any vowel is missing
        all_vowels_present = False
        break  # No need to check further

if all_vowels_present:
    print(vowel_counts)  # Print vowel counts if all vowels are present
else:
    print("Not all vowels are present.")


# 9.d
text = input("Enter a string: ")  # Take user input
text = text.lower()  # Convert to lowercase

vowels = "aeiou"  # Ordered list of vowels
filtered_vowels = ""  # String to store vowels in the order they appear

# Extract only vowels in order of appearance
for char in text:  # Directly looping through input (no character filtering)
    if char in vowels:
        filtered_vowels += char  # Store vowels as they appear

index = 0  # Track which vowel we are looking for next
for char in filtered_vowels:  # Loop through extracted vowels
    if char == vowels[index]:  # If it matches the next expected vowel
        index += 1  # Move to the next vowel
        if index == len(vowels):  # If we have found all vowels in order
            print(True)
            break
else:
    print(False)  # If the sequence "aeiou" is never completed


