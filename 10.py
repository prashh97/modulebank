# # 10.a
# 1. Purpose of Anonymous Functions (Lambda Functions)
# Lambda functions in Python are anonymous, single-expression functions that are used when a small function is required for a short period. They are particularly useful for:
# Passing as arguments in functions like map(), filter(), and sorted().
# Reducing code clutter, making the code concise and readable
# 2. Difference Between Fruitful and Non-Fruitful Functions
# Fruitful Functions: Return a value using the return statement
# 3. Recursive Functions and the Importance of a Base Case
# A recursive function is a function that calls itself to break down a problem into smaller subproblems.

# 10.b
# num = list(map(int, input("Enter numbers separated by spaces: ").split()))
# sum_of_numbers = sum(num)  # Using built-in sum()
# print("Sum:", sum_of_numbers)

# def calculate_average(numbers):
#     return sum(numbers) / len(numbers) if numbers else 0  # Avoid division by zero

# num_list = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print("Average:", calculate_average(num_list))

# def factorial(n):
#     if n == 0 or n == 1:  # Base case
#         return 1
#     return n * factorial(n - 1)  # Recursive case

# n = int(input("Enter a number: "))
# print("Factorial:", factorial(n))

# 10.c
#  Advantages of Lambda Functions:
# Concise and Readable – Lambda functions allow writing small functions in a single line, making the code compact.
# Useful in Higher-Order Functions – They work efficiently with functions like map(), filter(), and sorted(), eliminating the need for explicitly defined functions.
# No Need to Define a Named Function – Ideal for short-lived operations where defining a separate function would be unnecessary.
# Disadvantages of Lambda Functions:
# Limited Readability – Complex lambda expressions are difficult to understand, especially for beginners.
# Limited Functionality – They cannot contain multiple statements, loops, or docstrings, reducing their flexibility.
# Difficult Debugging – Since lambda functions are anonymous, debugging and tracing errors can be challenging.
# When to Use and Avoid Lambda Functions:
# Use them for simple, short operations where a full function definition is unnecessary.
# Avoid them for complex logic that requires multiple lines or needs documentation for maintainability.
# When Are Recursive Functions Inefficient or Problematic?
# Stack Overflow Due to Excessive Recursion Depth

# Python has a default recursion depth limit, and exceeding it results in a RecursionError.
# This issue arises when recursion does not have a proper base case or requires too many recursive calls.
# Repeated Computations (Overlapping Subproblems)

# Some recursive functions, such as computing Fibonacci numbers, recompute the same values multiple times, leading to inefficient performance.
# This causes an exponential increase in function calls, making execution slow.
# High Memory Usage

# Each recursive call adds to the call stack, consuming memory. Deep recursion can lead to excessive memory usage, slowing down or crashing the program.