# #7a 

# variable and assignment
# a variable stores data value 
# python is dynamically typed language meaning u dont have to declare a data type explicitly 

# assignment 
# an operator is used to assign values to variables

# keyword 
# words in pyhon that hae special meanings like if , else ,elif while , etc

# built in functions 
# python provides built in functions to simplify tasks 
# ex: print, len, sum , max ,min etc 

# Indentation
# we use indentation  at the beginning of lines to define code blocks  instead of {} in other languages 
# standard indentation in python is 4 spaces 

# comments 
# comments are used to explain what the code does 
# comments dont affect the execution of the code 
# we use  # or """"   """" to comment 

# instead of writing complete code , built in function perform tasks quickly 
# they used optimized algortihms that require reduced memory
# they minimize the chances if bugs


#7b i 
def print_poem():
    user_input = input("Enter the poem lines in this format: spaces|line, spaces|line\n")  
    lines = user_input.split(",")  # Split input at commas

    for line in lines:
        parts = line.split("|")  # Split each part into spaces and text
        spaces = " " * int(parts[0])  # Convert spaces to an integer and create indentation
        text = parts[1]  # Get the actual text
        print(spaces + text)  # Print with correct indentation

print_poem()


#7b ii 
def is_isomorphic(s, t):
    mapping_s = {}  # Store character mappings for s -> t
    mapping_t = {}  # Store character mappings for t -> s

    for i in range(len(s)):  # Loop through each character
        char_s = s[i]
        char_t = t[i]

        if char_s in mapping_s and mapping_s[char_s] != char_t:
            return False  # If a character was mapped to something else before, return False
        if char_t in mapping_t and mapping_t[char_t] != char_s:
            return False  # If a character in t maps to multiple different letters, return False

        mapping_s[char_s] = char_t  # Store the mapping
        mapping_t[char_t] = char_s  # Store the reverse mapping

    return True  # If all characters are correctly mapped, return True

# Example test cases
print(is_isomorphic("egg", "add"))  # Output: True
print(is_isomorphic("foo", "bar"))  # Output: False


#7b iii
r = int(input("enter radius in metre"))
area = 3.14*(r**2)
print("area is: ",area)


#7c 
# How Indentation in Python is Different
# Unlike other languages like C or Java, Python does not use {} or ; for blocks of code.
# Instead, indentation (spaces) is used to define code blocks.

# Built-in Functions vs Custom Functions
# Built-in functions (print(), len(), sum()) save time.
# Custom functions are useful for special tasks not covered by built-in functions.
    
# When to Use Built-in vs Custom?

# Use built-in functions for common tasks like finding length, sum, etc.
# Write custom functions when built-in functions don’t solve your problem.